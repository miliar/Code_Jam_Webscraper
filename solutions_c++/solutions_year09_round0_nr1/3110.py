// A. Alien Language
// Google Code Jam Sept 2009
// George Vafiadis

#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
using namespace std;

bool match(const list<string> & pattern, const string & word);
list<string> makePattern(const string & lang);

const int MaxWordSize = 16;

int main (int argc, char * const argv[]) 
{
	int L; // Number of letters in each world
	int D; // Number of words in the dictionary
	int N; // Number of Patterns/test cases
	vector<string> dict;
	
	cin >> L >> D >> N;
    
	cin.ignore();
	
	for(int i = 0; i < D; ++i)
	{
	   string word;
	   getline(cin, word);
	   dict.push_back( word );
	}

	for(int i = 0; i < N; ++i)
	{
		int nMatches;
		string pattern;
		
		getline(cin, pattern);
		
		const list<string> & plist = makePattern(pattern);
	
		vector<string>::const_iterator iter;
		
		nMatches = 0;
		
		for(iter = dict.begin(); iter != dict.end(); ++iter)
			if( match(plist, *iter) ) ++nMatches;
		
		cout << "Case #" << (i+1) << ": " << nMatches << endl;
	}
	
    return 0;
}

bool match(const list<string> & pattern, const string & word)
{
	list<string>::const_iterator iter;

	if( pattern.size() != word.size() ) return false;
	
	int cursor = 0;
	
	for(iter = pattern.begin(); iter != pattern.end(); ++iter)
	{
	 string pLetter = *iter;
		
	 if( pLetter.find(word[cursor]) != string::npos)
		 ++cursor;
	 else
		 return false;
	}

   return true;
}

list<string> makePattern(const string & lang)
{
  list<string> plist;
  string bound;
  bool insideBound = false;
	
  for(int i = 0; i < lang.size(); ++i)
  {
	  if( lang[i] == '(' )
	  {
		insideBound = true;
		bound = "";
	  }
	  else if( lang[i] == ')' )
	  {
		  insideBound = false;
		  if( bound != "" ) plist.push_back(bound);
	  }
	  else if( insideBound )
		  bound = bound + lang[i];  
	  else
	  {
		  string singleLetter;
		  singleLetter.push_back( lang[i] );
		  plist.push_back( singleLetter );
	  }
  }
  
  return plist;
}

