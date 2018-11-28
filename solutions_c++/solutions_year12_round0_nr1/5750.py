#include <iostream>
#include <cstdio>
#include <vector>
#include <string.h>

using namespace std;

char lan[] =     {'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z'};
char eng_lan[] = {'y' , 'h' , 'e' , 's' , 'o' , 'c' , 'v' , 'x' , 'd' , 'u' , 'i' , 'g' , 'l' , 'b' , 'k' , 'r' , 'z' , 't' , 'n' , 'w' , 'j' , 'p' , 'f' , 'm' , 'a' , 'q'};

string f(string s)
{
  string res = "";
  for (int i = 0; i < (int)s.length(); i++)
   {
    bool ok = false;
    for (int j = 0; j < 27 && !ok; j++)
     if (s[i] == lan[j])
      res += eng_lan[j],
      ok = true;
    if (!ok) res += s[i];
   }
  return res;
}

int main()
{
  freopen("A-small-attempt0.in","r",stdin);
  freopen("A-small-attempt0.out","w",stdout);

  int n , l = 1;
  string s;

  cin>>n; getline(cin,s);
  for (int i = 0; i < n; i++)
   {
     getline(cin,s);
     cout<<"Case #"<<i+1<<": "<<f(s)<<endl;
   }
  return 0;
}
