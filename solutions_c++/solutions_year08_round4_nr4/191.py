#include <stdio.h>
#include <algorithm>

using namespace std;

#define MAX 10

int perm[MAX];
char str[MAX];

int solve(int k,int n)
{
	char bef='\0';
	int i;
	int ret=0;
	for(i=0;i<n;++i)
	{
		if(str[perm[i%k]+(i/k)*k]!=bef)
		{
			++ret;
			bef=str[perm[i%k]+k*(i/k)];
		}
	}
	return ret;
}

int main()
{
	int resp;
	int cnt,t;
	int tmp;
	int n;
	int i,k;
	scanf("%d",&t);
	for(cnt=1;cnt<=t;++cnt)
	{
		scanf("%d",&k);
		for(i=0;i<k;++i)
			perm[i]=i;
		scanf(" ");
		scanf("%s%n",str,&n);
		resp=n;
		while(next_permutation(perm,perm+k))
		{
			tmp=solve(k,n);
			if(tmp<resp)
			{
				resp=tmp;
			}
		}
		printf("Case #%d: %d\n",cnt,resp);
	}
	return 0;
}


