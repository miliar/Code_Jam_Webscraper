#include <string>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <math.h>
#include <utility>
#include <sstream>
#include <queue>
#include <stack>
#include <iomanip>
#include <limits.h>
#ifndef ONLINE_JUDGE
#include <conio.h>
#endif
using namespace std;

#define max(a,b) (a>=b?a:b)
#define min(a,b) (a<=b?a:b)
#define pb push_back
#define mp make_pair
#define all(X) (X).begin(),(X).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

int N,i,j,T,S,P,k,surp[200];
struct node
{  int mx,mxs,total; }a[200];
bool comp(node a,node b)
{
   if(a.total==1 || a.total==29) return 1;
   else if(b.total==1 || b.total==29) return 0;
   if( a.mxs-a.mx!=b.mxs-b.mx ) return a.mxs-a.mx<b.mxs-b.mx;
   return a.mxs<b.mxs;
}  

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    for(k=1;k<=T;k++)
    {
        scanf("%d %d %d",&N,&S,&P);
        for(i=0;i<N;i++)
        {
            scanf("%d",&a[i].total);
            if(a[i].total%3==0)
            {
               a[i].mx=a[i].total/3;
               a[i].mxs=min(a[i].mx+1,10);
               if(a[i].total==0)a[i].mxs=0;
            }
            else if(a[i].total%3==1)
            {
               a[i].mx=1+(a[i].total-1)/3;
               a[i].mxs=a[i].mx;
            }
            else
            {
               a[i].mx=(a[i].total+1)/3;
               a[i].mxs=min(a[i].mx+1,10);
            } 
        }
        memset(surp,0,sizeof surp);
        int cnt=0;
        for(i=0;i<N;i++)
        {
           if(a[i].mx<P && a[i].total>1 && a[i].total<29 && a[i].mxs>=P && cnt<S)
           { surp[i]=1; cnt++; }
        }
        int ans=0;
        for(i=0;i<N;i++)
        {
           if(surp[i]==1)
           { if(a[i].mxs>=P)ans++; }
           else
           { if(a[i].mx>=P)ans++; }
        }
        printf("Case #%d: %d\n",k,ans);
    }           

#ifndef ONLINE_JUDGE
    getch();
#endif
    return 0;
}
