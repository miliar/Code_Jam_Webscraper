//convert stl string to char array{string stl, char    *arr=stl.c_str()}
//convert char array to string{char arr[]; string str; str.assign(arr)}
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<cstring>
using namespace std;
#define REP(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,a,b) for(int (i)=a;(i)<(b);(i)++)
#define INF 2000000000
#define INFLL (1LL<<62)
//#define SS ({int x;scanf("%d", &x);x;})
//#define SSL ({LL x;scanf("%lld", &x);x;})
#define _mp make_pair
#define MOD 1000000007
#define MAXN 90000000000LL
map<char,char>mp;
void create()
{
    mp['a']='y';
    mp['b']='h';
    mp['c']='e';
    mp['d']='s';
    mp['e']='o';
    mp['f']='c';
    mp['g']='v';
    mp['h']='x';
    mp['i']='d';
    mp['j']='u';
    mp['k']='i';
    mp['l']='g';
    mp['m']='l';
    mp['n']='b';
    mp['o']='k';
    mp['p']='r';
    mp['q']='z';
    mp['r']='t';
    mp['s']='n';
    mp['t']='w';
    mp['u']='j';
    mp['v']='p';
    mp['w']='f';
    mp['x']='m';
    mp['y']='a';
    mp['z']='q';
}
int main()
{
 //freopen("inp.in","r",stdin);
 //freopen("out.in","w",stdout);
 create();
 char ss[1000];
 int tt,c=0;
 cin>>tt;
 gets(ss);
 while(tt--)
 {
 gets(ss);
 c++;
 int n=strlen(ss);
 for(int i=0;i<n;i++)
     {
      if(ss[i]==32)continue;
       ss[i]=mp[ss[i]];
     }
  cout<<"Case #"<<c<<": "<<ss<<"\n";
 }
 return 0;
}
