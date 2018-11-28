#include <iostream>
#include <vector>
#include <utility>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
  int T;
  cin >> T;

  for(int i = 0; i < T; i++)
  {
    int C;
    cin >> C;
    
    map<pair<char, char>, char> combinations;

    for(int j = 0; j < C; j++)
    {
      char E1, E2, R;
      cin >> E1 >> E2 >> R;
      combinations.insert(make_pair(make_pair(E1, E2), R));
      combinations.insert(make_pair(make_pair(E2, E1), R));
    }

    int D;
    cin >> D;

    vector<vector<char> > opposed(26, vector<char>(0, 'A'));
    for(int j = 0; j < D; j++)
    {
      char E1, E2;
      cin >> E1 >> E2;
      
      opposed[E1 - 65].push_back(E2);
      opposed[E2 - 65].push_back(E1);
    }

    int l;
    cin >> l;
    string s;
    cin >> s;

    for(int j = 1; j < s.length(); j++)
    {
      // if we have a combination
      
      map<pair<char, char>, char>::iterator it;
      it = combinations.find(make_pair(s[j], s[j - 1]));
      if(it != combinations.end())
      {
	s.replace(j-1, 2, string() + it->second);
	j--;
      }

      // if we have an opposition
      
      for(int k = 0; k < j; k++)
      {
	for(int m = 0; m < opposed[s[k] - 65].size(); m++)
	{
	  if(opposed[s[k] - 65][m] == s[j])
	  {
	    s.erase(0, j + 1);
	    j = 0;
	    break;
	  }
	}

      }	
    }
   
    cout << "Case #" << i + 1 << ": [";
    
    if(s.length() > 0)
    {
      for(int j = 0; j < s.length() - 1; j++)
      {
	cout << s[j] <<  ", ";
      }

      if(s.length() > 0)
	cout << s[s.length() - 1];
    }
    cout << "]" << endl;
  }
}
