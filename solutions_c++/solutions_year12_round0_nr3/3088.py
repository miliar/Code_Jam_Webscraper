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
int checker(int ll,int A,int B,string num1)
{
    int n=num1.length();
    int kk=0,count=0;
    int arr[10010];
    memset(arr,0,10010);
    //cout<<"**********"<<ll<<"****************\n";
    for(int i=n-1;i>0;i--)
     {
         kk=0;
         bool cn=true;
         for(int j=i;j<n;j++)
             {
               kk*=10;
               kk+=num1[j]-'0';
               if(kk==0&&cn)
                 cn=false;
             }
         for(int j=0;j<i;j++)
             {
               kk*=10;
               kk+=num1[j]-'0';
             }
         if(kk>=A&&kk<=B&&cn&&kk!=ll&&kk>ll)
           if(arr[kk]==0)
           {arr[kk]=1;count++;}
     }
    //cout<<"******************************************\n";
    return count;
}
string converter(int n)
{
    string ss="";
    while(n)
     {
         int k=n%10;
         char ch=k+'0';
         ss=ch+ss;
         n/=10;
     }
    return ss;
}
int main()
{
 //freopen("inp.in","r",stdin);
 //freopen("out.in","w",stdout);
 int tt,c=0,A,B,count;
 int arr[1000];
 cin>>tt;
 while(tt--)
 {
  cin>>A>>B;
  count=0;
  c++;
  for(int i=A;i<=B;i++)
   {
       string ss=converter(i);
       count+=checker(i,A,B,ss);
   }
  cout<<"Case #"<<c<<": "<<count<<"\n";
 }
 return 0;
}
