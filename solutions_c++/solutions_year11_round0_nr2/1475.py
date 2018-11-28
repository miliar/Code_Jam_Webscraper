#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

int main()
{
   int T;

   cin >> T;

   for (int i = 0; i < T; ++i)
   {
      int C;
      cin >> C;

      map <char, map <char, char> > combine;

      for (int j = 0; j < C; ++j)
      {
	 string s;
	 cin >> s;

	 combine[s[0]][s[1]] = s[2];
	 combine[s[1]][s[0]] = s[2];
      }

      int D;
      cin >> D;

      map <char, set<char> > oppose;

      for (int j = 0; j < D; ++j)
      {
	 string s;
	 cin >> s;
	 oppose[s[0]].insert(s[1]);
	 oppose[s[1]].insert(s[0]);
      }

      int N;
      cin >> N;
      string s;
      cin >> s;

      vector<char> result;
      for (int j = 0; j < s.size(); ++j)
      {
	 if (result.size() > 0)
	 {
	    char prev = result.back();

	    map<char, char>::const_iterator cit;
	    if ((cit = combine[prev].find(s[j])) != combine[prev].end())
	    {
	       result.pop_back();
	       result.push_back(cit->second);
	       continue;
	    }
	 }

	 bool clear = false;
	 for (vector<char>::const_iterator cit = result.begin(); cit != result.end(); ++cit)
	 {
	    if (oppose[s[j]].find(*cit) != oppose[s[j]].end())
	    {
	       clear = true;
	       break;
	    }
	 }
	 if (clear)
	 {
	    result.clear();
	    continue;
	 }

	 result.push_back(s[j]);
      }

      cout << "Case #" << i + 1 << ": [";
      for (vector<char>::const_iterator cit = result.begin(); cit != result.end(); ++cit)
      {
	 if (cit != result.begin())
	 {
	    cout << ", ";
	 }

	 cout << *cit;
      }
      cout << "]" << endl; 

   }

   return 0;
}

