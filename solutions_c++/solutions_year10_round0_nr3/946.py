/*
 * C.cpp
 *
 *  Created on: 2010-5-8
 *      Author: LK_TMP
 */

#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
const int MAXN=1009;
long long g[MAXN],s[MAXN],k;
int h[MAXN],r,n;

void work()
{
	memset(s,0,sizeof(s));
	for (int i=1;i<=n;i++) h[i]=-1; h[0]=0;
	int head=0,m;
	for (m=1;m<=n+2;m++)
	{
		long long sum=0;	int i,count=0;
		for (i=head;(sum+g[i]<=k && ++count<=n);i=(i+1)%n)	sum+=g[i];
		s[m]=s[m-1]+sum;
		head=i;		if (h[head]>=0) break; else h[head]=m;
	}
	int k=h[head];
	long long len=m-k;
	long long ans=(r-k)/len*(s[m]-s[k])+s[k]+s[(r-k)%len+k]-s[k];
	cout<<ans<<endl;
}

int main()
{
	int t;
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		cin>>r>>k>>n;
		for (int j=0;j<n;j++) cin>>g[j];
		cout<<"Case #"<<i<<": ";
		work();
	}
	fclose(stdin); fclose(stdout);
	return 0;
}
