#include <iostream>
#include <algorithm>
#define i(c)  (c) -'a'
using namespace std;


char map[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int ini()
{
  int c;
  cin >> c;
  if(c)
  {
    string s;
    getline(std::cin,s);
  }
  return c;
}

void in(string* cases, int n)
{
  for(int i = 0; i<n; i++)
    getline(std::cin,cases[i]);
}

void create_map(string* cases, string* rcases , int n)
{
  for(int j = 0; j<26; j++)
      map[j] = '#';
  for(int i = 0; i<n; i++)
  {
    int l = cases->length();
    for(int j = 0; j<l; j++)
      if(cases[i].c_str()[j]!=' ')
      map[ cases[i].c_str()[j]  - 'a' ] = rcases[i].c_str()[j];
  }
  for(int j = 0; j<26; j++)
      cout << ",'" << map[j] << "'"; 
    
}




int main()
{
  int n = ini();
  string cases[n];
  in(cases,n);
  
  for(int i = 0; i<n; i++)
  {
    int l = cases[i].length();
    cout << "Case #" << i+1 << ": ";
    for(int j = 0; j < l; j++)
    {
      char c = cases[i].c_str()[j];
      
      if(c==' ') cout << ' ';
      else cout << map[c-'a'];
    }
    cout << endl;
  }
  
  return 0;
}