//Program:

#include<iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>


using namespace std;
typedef vector<long int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;
typedef long double LD;

#define pb push_back
#define REP(i,n) for(i=0;i<(n);i++)
#define FOR(i,a,b) for(i=(a),i<(b);i++)
#define FORD(i,a,b) for(i=(a);i>(b);i--)
#define ALL(c)  (c).begin(),(c).end()
#define OUT(c) cout<<(c)<<endl

#define INF 100000

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

//Global:



//

//Function DEF:




//

int main()
{
  freopen("A.in", "rt", stdin);
freopen("A.txt", "wt", stdout);
int t,n,k,i,j,m,countr,countb,count,d,l,r,tc=0;
char a[52][52],c[52][52];
bool flag1,flag2;

cin>>t;
while(t--)
{tc++;
memset(a,'#',sizeof(a));
memset(c,'#',sizeof(c));
cin>>n>>k;
flag1=false;
flag2=false;
REP(i,n)
{
   REP(j,n)
   {
     cin>>a[i][j];
       }
    }
for(i=0;i<n;i++)
{  m=n-1;
for(j=n-1;j>=0;j--)
   {

       if(a[i][j]!='.')
       {
        c[i][m]=a[i][j];
           m--;
           }

       }
    }

for(i=0;i<n;i++)
{
   for(j=0;j<n;j++)
   {
     if(c[i][j]!='R'&&c[i][j]!='B')
       c[i][j]='.';
       }
    }
char temp;

for(i=n-1;i>=0;i--)
{
    count=0;d=0;l=0;r=0;
    if(flag1&&flag2)
    break;
   for(j=n-1;j>=0;j--)
   {
    if(c[i][j]!='.')
    {temp=c[i][j];
    d=0;
    count=0;
     while(c[i-d][j]==temp&&(i-d)>=0)
     {
       count++;
        d++;
         }
         if(count==k)
            {
            if(temp=='R')
                flag1=true;
                else
                flag2=true;
             }

            count=0;
          d=0;
             while(c[i][j-d]==temp&&(j-d)>=0)
        {
       count++;
       d++;
         }
          if(count==k)
            {if(temp=='R')
            flag1=true;
            else
            flag2=true;
             }
             count=0;
           l=0;
           d=0;
            while(c[i-l][j-d]==temp&&(l<n&&d<n))
        {
        l++;
       count++;
       d++;
         }
          if(count==k)
            {if(temp=='R')
            flag1=true;
            else
            flag2=true;
             }
             count=0;

                d=0;
                r=0;
        while(c[i-r][j+d]==temp&&(r<n&&d<n))
        {
            r++;
       count++;
       d++;
         }
          if(count==k)
            {if(temp=='R')
                flag1=true;
                else
                flag2=true;
             }
             count=0;

        }

       }
    }
/*
for(i=0;i<n;i++)
{
   for(j=0;j<n;j++)
   {
     cout<<c[i][j];
       }cout<<endl;
    }
    */


//cout<<k<<endl;
string ans;
if(flag1&&flag2)
ans="Both";
else if(!flag1&&!flag2)
ans="Neither";
else if(flag1)
ans="Red";
else if(flag2)
ans="Blue";

cout<<"Case #"<<tc<<": "<<ans<<endl;
}
   return 0;
}
