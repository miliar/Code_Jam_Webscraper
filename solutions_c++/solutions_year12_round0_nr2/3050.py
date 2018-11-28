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

int main()
{
 //freopen("inp.in","r",stdin);
 //freopen("out.in","w",stdout);
 int tt,c=0,N,S,p,count;
 int arr[1000];
 cin>>tt;
 while(tt--)
 {
  cin>>N>>S>>p;
  for(int i=0;i<N;i++)
   cin>>arr[i];
  count=0;
  c++;
  for(int k=0;k<N;k++)
   {
       bool cn=false,flag=false;
       for(int i=0;i<=10;i++)
        {
         for(int j=0;j<=10;j++)
         {
         for(int l=0;l<=10;l++)
           {
            if(i+j+l==arr[k] && max(i,max(j,l))>=p)
             {
                 if(max(i,max(j,l))-min(i,min(j,l))<=2)
                   {

                       if(S &&  max(i,max(j,l))-min(i,min(j,l))==2 )
                         cn=true;
                       if(max(i,max(j,l))-min(i,min(j,l))<2 )
                         flag=true;
                   }
             }
            if(flag)break;
           }
            if(flag)break;
           }
           if(flag)break;
        }
       if(flag)count++;
       else if(!flag && cn){count++;S--;}
   }
  cout<<"Case #"<<c<<": "<<count<<"\n";
 }
 return 0;
}
