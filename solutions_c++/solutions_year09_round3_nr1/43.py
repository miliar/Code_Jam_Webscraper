#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
//#include <cmath>

using namespace std;

const long long MAX=1000000000000000001LL;
char s[100];
char num[256];
long long pow[40][100];

long long process(char*s,int b)
{
	int i,j,l,k;
	long long r=0;
	bool u[50]={0};
	for(i=0;i<256;i++) num[i]=-1;
	for(l=0;s[l];l++);
	num[s[0]]=1;
	u[1]=true;
	if (pow[b][l-1]>=MAX) return MAX;
	r=pow[b][l-1];

	int numbers=1;
	j=0;
	for(i=1;s[i];i++)
	{
		if (num[s[i]]==-1) 
		{
			for(;u[j];j++);
			num[s[i]]=j;
			u[j]=true;
			numbers++;
		}
		k=num[s[i]];
		if (pow[b][l-i-1]>=MAX) return MAX;
		if (k>0 && pow[b][l-i-1]>MAX/k) return MAX;
		if (r>MAX-pow[b][l-i-1]*k) return MAX;
		r+=pow[b][l-i-1]*k;
	}

	if (numbers>b) return MAX;
	return r;

}

void powers()
{
	int i,j;
	for(i=2;i<40;i++)
	{
		pow[i][0]=1;
		for(j=1;j<100;j++)
			if (pow[i][j-1]>MAX/i) pow[i][j]=MAX;
			else pow[i][j]=pow[i][j-1]*i;
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	powers();

	int t,T;
	scanf("%d",&T);
	gets(s);
	for(t=1;t<=T;t++)
	{
		long long ans=MAX;
		gets(s);
		for(int B=2;B<40;B++)
		{
			long long tmp=process(s,B);
			if (tmp<ans) ans=tmp;
		}

		printf("Case #%d: %lld\n",t,ans);
	}

	return 0;
}