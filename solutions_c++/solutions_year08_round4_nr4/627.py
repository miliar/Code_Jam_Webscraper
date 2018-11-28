#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <sstream>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define forv(i,v) for(int i=0;i<v.size();++i)   
#define forn(i,n) for (int i=0;i<n;++i)   
#define fors(i,s) for (int i=0;i<s.size();++i)   
#define all(a) a.begin(),a.end()   
#define pb push_back   
#define INF 10000000   
#define VI vector<int>   



int main()
{
     freopen("D-small-attempt1.in", "r", stdin);
     freopen("D-small-attempt1.out", "w", stdout);
     int n;
     cin >> n;
forn(i,n){
     cout<<"Case #"<<i+1<<": ";
     int n;
     string s;
     VI fuck(n);

     cin >> n;
     cin >> s;
     forn(i,n) fuck[i]=i;
     int ans=0x10000000;
     do {
          string s2="";
          for (int i=0;i<s.length();i+=n)
          {
               string ss="";
               forn(j,n) ss+=" ";
               forn(j,n) ss[j]=s[fuck[j]+i];
               s2+=ss;
          }
          int cur=0;
          forn(i,s2.length()) if ((i)&&(s2[i]!=s2[i-1]))cur++;
          ans=min(ans,cur+1);

     }
     while (next_permutation(all(fuck)));
     cout<<ans<<endl;
}
   return 0;
}
