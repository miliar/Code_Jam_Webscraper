#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<utility>
#include<set>
#include<sstream>
#define fr(a,b,c) for (a=b;a<=c;a++)
#define frr(a,b,c) for (a=b;a>=c;a--)
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define oo 1000111222
using namespace std;

int a[1111],d[1111];
double re;

int main()
{
   int test,it,n,i;
   cin >> test;
   fr(it,1,test)
   {
      cin >> n;
      memset(d,0,sizeof(d));
      fr(i,1,n) scanf("%d",&a[i]);
      re=0;
      fr(i,1,n)
        if (!d[i])
        {
           int x=i,s=1;
           d[i]=1; 
           while (1)
           {
              x=a[x]; 
              if (x==i) break;
              d[x]=1; s++;
           }
           if (s>1) re+=s;
        }
      printf("Case #%d: %.6lf\n",it,re);
   }
   return 0;
}
