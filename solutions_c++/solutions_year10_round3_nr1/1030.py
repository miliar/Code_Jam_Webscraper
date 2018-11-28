#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define M 10002
long long  s[M],tmp[M];
long long  ans;

struct node 
{int x,y;}ss[M];

bool cmp(const struct node a,const struct node b)
{return a.x<b.x;}

void Merge(long long  x[],long long  l,long long  mid,long long  r)
{
    long long  i,j,k,v=l;
	   for(i=l,j=mid+1;l<=mid&&j<=r;i++)
		   if(x[j]>x[l]){tmp[i]=x[l++];}
		         else {tmp[i]=x[j++];ans+=mid-l+1;}//ans++;

	   if(l<=mid)
	   {
		   for(;i<=r;i++)
			     tmp[i]=x[l++];
	   }
	   
	    if(j<=r)
			for(;i<=r;i++)
				tmp[i]=x[j++];

		for(k=v;k<=r;k++)
			x[k]=tmp[k];
}

void MergeSort(long long  x[],long long  l,long long  r)
{
   long long  mid=(l+r)/2;
     if(l<r)
	 {
	    MergeSort(x,l,mid);
	    MergeSort(x,mid+1,r);
		Merge(x,l,mid,r);
	 }

}

int main()
{
   long long  n,i,t,cases=0;
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);
   scanf("%lld",&t);
     while(t--)
	 {
		 scanf("%lld",&n);
	     for(i=1;i<=n;i++)
		 {
			 //scanf("%lld",&s[i]);
			 scanf("%lld%lld",&ss[i].x,&ss[i].y);
		 }
		 sort(ss+1,ss+n+1,cmp);
		 for(i=1;i<=n;i++)s[i]=ss[i].y;
		 ans=0;
         MergeSort(s,1,n);
		 printf("Case #%lld: %lld\n",++cases,ans);
	 }

	 //system("pause");
 return 0;
}