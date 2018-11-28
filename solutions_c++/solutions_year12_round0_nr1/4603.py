#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

int main ()
{
  map<char,char> all;
  int N = 0;
  cin >> N;
  cin.ignore(256, '\n');
  for (int i = 0; i < N; i++)
  {
    string tmp;
    string tmp2;
    getline (cin,tmp);
    getline (cin,tmp2);
    for (int j = 0; j < tmp.size(); j++)
    {
       if (tmp[j] != ' ')
       all[tmp[j]] = tmp2[j];
    }
  }
  all['z'] = 'q';
  all['q'] = 'z'; 
  /*map<char,char>::iterator p;
  for (p = all.begin(); p != all.end(); ++p)
  {
    cout << p->first << " -> " << p->second << endl;
  }*/

  int M = 0; cin >> M;
  cin.ignore(256,'\n');
  for (int i = 0; i < M; i++)
  {
    string tmp;
    getline (cin,tmp);
    for (int j = 0; j < tmp.size(); j++)
    {
      if (tmp[j] != ' ')
      {
        tmp[j] = all[tmp[j]];
      }
    }
    cout << "Case #" << i + 1 << ": " << tmp << endl;
  }

  return 0;
}
