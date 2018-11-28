#include <iostream>
#include <vector>
#include <cstdlib>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <set>
#include <string>
#include <map>
#define mp make_pair
#define pii pair(int,int)
#define all(v) v.begin(),v.end()
#define ll long long

using namespace std;

string w="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
string t="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

int main()
{map <char,char> alp;
 int i,j;
 freopen("A-small-attempt2.in","rt",stdin);
 freopen("out.txt","wt",stdout);
 for(i=0;i<w.size();i++)
 alp[w[i]]=t[i];
 //alp['q']='z';
 alp['e']='o';
 alp['y']='a';
 alp['q']='z';
 int t;cin >> t;cin.get();
 for(int tc=1;tc<=t;tc++)
 {string s;
  getline(cin,s);
  for(i=0;i<s.size();i++)
  s[i]=alp[s[i]];
  for(i=0;i<s.size();i++)
  if(s[i]==NULL) s[i]='q';
  cout << "Case #" << tc << ": " << s << endl; }
}
