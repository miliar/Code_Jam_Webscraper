#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <sstream>

using namespace std;

int minimal_switches(set<string>& search_eng, 
		     vector<string>& queries)
{
  int res = 0;
  set<string> current; // saves the current search engines we have used.

  for (vector<string>::iterator it = queries.begin();
       it != queries.end(); ++it)
    {
      if (current.find(*it) == current.end())
	{
	  current.insert(*it);
	  if (current.size() == search_eng.size())
	    {
	      ++res;
	      current.clear();
	      current.insert(*it);
	    }
	}
    }

  return res;
}

int main()
{
  int N;
  string temp;
  getline(cin, temp);
  stringstream in(temp);
  in >> N;

  for (int i = 0; i < N; ++i)
    {
      set<string> search_eng;
      vector<string> quearies;

      int S;
      getline(cin, temp);// skip the rest of the line
      stringstream in(temp);
      in >> S;

      for (int j = 0; j < S; ++j)
	{
	  string s_e;
	  getline(cin, s_e);
	  search_eng.insert(s_e);
	}

      int Q;
      getline(cin, temp);// skip the rest of the line
      stringstream in2(temp);
      in2 >> Q;

      for (int j = 0; j < Q; ++j)
	{
	  string q;
	  getline(cin, q);
	  quearies.push_back(q);
	}

      cout << "Case #" << i + 1 << ": " << 
	minimal_switches(search_eng, quearies) << endl;
    }

  return 0;
}
