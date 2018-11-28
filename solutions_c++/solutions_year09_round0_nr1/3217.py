#include <iostream>
#include <fstream>
#include <iterator>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#include <boost/lexical_cast.hpp>
#include <boost/foreach.hpp>

using namespace boost;

typedef unsigned long long uint64;
typedef long long int64;

vector<string> words;
vector<string> tests;

# define foreach BOOST_FOREACH


class comparator
{
public:
  bool operator () (const string & lhs, const string & rhs)
  {
    if (lhs.size() == rhs.size())
      {
	return (lhs < rhs);
      }
    string small;
    string big;
    if (lhs.size() < rhs.size())
      {
	small = lhs;
	big   = rhs;
      }
    else 
      {
	small = rhs;
	big   = lhs;
      }
    if (big.find(small) != string::npos)
      {
	return false;
      }
    return lhs < rhs;
  }

 };


bool checkifthere(string tmp)
{
  comparator obj;
  if (false == binary_search(words.begin(),
				  words.end(),
				  tmp,
				   obj
				   )
      )
    {
      return false;
    }
  else
    {
      return true;
    }
}

string gettoken(string pattern, const uint64 index)
{
  string val;
  uint64 count = 0;
  bool inside = false;
  foreach( char ch, pattern)
    {
      if (')' == ch)
	{
	  if (index == count)
	    {
	      return val;
	    }
	  ++count;
	  val.clear();
	  inside = false;
	  continue;
	}
      if ('(' == ch)
	{
	  val.clear();
	  inside = true;
	  continue;
	}
      
      val += ch;
      if (false == inside)
	{
	  if (index == count)
	    {
	      return val;
	    }
	  ++count;
	}
    }
}


int main(int argc, char ** argv)
{
  vector<string> svec;
  ifstream ifile(argv[1]);
  ofstream ofile(argv[2]);
  copy( istream_iterator<string>(ifile),
	istream_iterator<string>(),
	back_inserter(svec));
  uint64 index = 0;
  uint64 L = lexical_cast<uint64>(svec[index++]);
  uint64 D = lexical_cast<uint64>(svec[index++]);
  uint64 N = lexical_cast<uint64>(svec[index++]);
  for (uint64 i = 0; i < D; ++i)
      words.push_back(svec[index++]);
  sort(words.begin(),
       words.end(),
       comparator());
  for (uint64 i = 0; i < N; ++i)
      tests.push_back(svec[index++]);
  uint64 testcounter = 1;
  foreach(string test, tests)
    {
      bool pat1 = true;
      bool first = true;
      bool none = false;
      vector<string> pattern1;
      vector<string> pattern2;
      for (uint64 i = 0; i < L; ++i)
	{
	  string token = gettoken(test, i);
	  vector<string> & refin  = (pat1 == true)? pattern1: pattern2;
	  vector<string> & refout = (pat1 == true)? pattern2: pattern1;
	  refout.clear();
	  foreach (char ch, token)
	    {
	      if (true == first)
		{

		  string tmp1;
		  tmp1 += ch;
		  if (checkifthere(tmp1))
		    {
		      refout.push_back(tmp1);
		    }
		}
	      else
		{
		  foreach(string word, refin)
		    {
		      word += ch;
		      if (checkifthere(word))
			{
			  refout.push_back(word);
			}
		    }
		} // first check
	    } // Looping through each char in a token
	  first = false;
	  pat1 = !pat1;
	}// Looping through L tokens

      ofile << "Case #" << testcounter << ": ";

      if (true == pat1)
	{
	  ofile << pattern1.size() << endl;
	}
      else
	{
	  ofile << pattern2.size() << endl;
	}
            
      testcounter++;

    } // Looping through Tests
  return 0;
}
