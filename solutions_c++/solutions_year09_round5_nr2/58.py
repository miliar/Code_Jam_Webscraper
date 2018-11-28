#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>

using namespace std;

const int MOD=10009;
int s[20][26];
int S[26];
int ans;
int M;
string pol;
int f[10];

void eval(int M)
{
	int i;
	long long j=1,k=0;
	for(i=0;i<pol.length();i++)
	{
		if (pol[i]=='+')
		{
			k+=j;
			j=1;
		} else j=j*S[pol[i]-'a'];
	}
	ans=(ans+(k+j)%MOD*M)%MOD;
}

void rec(int cur,int end,int total,int M)
{
	if (!total) 
	{
		eval(M);
		return ;
	}
	if (cur==end) return ;
	
	for(int i=0;i<=total;i++)
	{
		if (i) for(int j=0;j<26;j++) S[j]+=s[cur][j];
		rec(cur+1,end,total-i,M/f[i]);
	}
	for(int j=0;j<26;j++) S[j]-=total*s[cur][j];
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t,T;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		int n,k,i,j;
		cin>>pol>>k>>n;
		for(i=0;i<n;i++) 
		{
			string t;
			cin>>t;
			for(j=0;j<26;j++) s[i][j]=0;
			for(j=0;j<t.size();j++) s[i][t[j]-'a']++;
		}

		printf("Case #%d:",t);
		f[0]=1;
		for(i=1;i<10;i++) f[i]=f[i-1]*i;
		M=1;
		for(i=1;i<=k;i++)
		{
			ans=0;
			M*=i;
			rec(0,n,i,M);
			printf(" %d",ans);
		}
		puts("");
		
	}

	return 0;
}