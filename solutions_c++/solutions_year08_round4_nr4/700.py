#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<vector>
#include<queue>
#include<iostream>
#include<sstream>
#include<functional>
#include<map>
#include<set>

using namespace std;


int K;
char str[1002];
int fact(int k)
{
	if(k==1)
		return 1;
	return fact(k-1)*k;
}
int getLen(vector<int>& v)
{
	char buf[10002];
	strcpy(buf, str);
	int len=strlen(str);
	int n=len/K;
	for(int i=0; i<n; i++)
		for(int j=0; j<K; j++)
		{
			buf[i*K+j]=str[i*K+v[j]];
		}
	int ret=0;
	for(int i=1; i<len; ++i)
	{
		if(buf[i]!=buf[i-1])
			ret++;
	}
	return ret+1;
}
int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	int numCase;
	scanf("%d", &numCase);
	for(int c=1; c<=numCase; c++)
	{
		scanf("%d",&K);
		scanf("%s",str);
		vector<int> per;
		for(int i=0; i<K; i++)
		{
			per.push_back(i);
		}
		int tim=fact(K);	
		int ret=100000000;
		for(int i=0; i<=tim; i++)
		{
			int len=getLen(per);
			if(len<ret)
				ret=len;
			next_permutation(per.begin(), per.end());
		}

		printf("Case #%d: ", c);
		printf("%d\n" ,ret);
	}
	return 0;
}