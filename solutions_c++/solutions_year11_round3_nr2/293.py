#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <fstream>
#define MAXM 1000010
#define LL long long 

using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

LL L,n,c,len1,len2;
LL num[MAXM],a[MAXM],b[MAXM],t;
struct In
{
	LL dis;
	LL shi;
}s[MAXM];

bool cmp(LL x,LL y)
{
	return x>y;
}

int main()
{
	int T,cas;
	fin>>T;
	for(cas=1;cas<=T;cas++)
	{
		fin>>L>>t>>n>>c;
		int i,j,k;
		for(i=1;i<=c;i++)
		fin>>num[i];
		s[0].dis=0;
		s[0].shi=0;
		for(i=1;i<=n;i++)
		{
			j=i%c;
			if(j==0) j=c;
			s[i].dis=num[j];
			s[i].dis+=s[i-1].dis;
			s[i].shi=s[i].dis*2;
		}
		len1=0;
		len2=0;
		LL res=0;
		for(i=0;i<=n;i++)
		if(s[i].shi>=t) break;
		for(j=1;j<i;j++)
		{
			k=j%c;
			if(k==0) k=c;
			a[len1++]=num[k];
		}
		if(i<=n)
		{
			if(s[i].shi>t)
			{
				a[len1++]=(t-s[i-1].shi)/2;
				b[len2++]=(s[i].shi-t)/2;
			}
			else if(s[i].shi==t && i>0)
			{
				k=i%c;
				if(k==0) k=c;
				a[len1++]=num[k];
			}
		}
		for(j=i+1;j<=n;j++)
		{
			k=j%c;
			if(k==0) k=c;
			b[len2++]=num[k];
		}
		sort(b,b+len2,cmp);
		for(i=0;i<len1;i++)
			res+=a[i]*2;
		for(j=0;j<len2 && j<L;j++)
			res+=b[j];
		for(;j<len2;j++)
			res+=2*b[j];
		fout<<"Case #"<<cas<<": "<<res<<endl;
	}
	return 0;
}
