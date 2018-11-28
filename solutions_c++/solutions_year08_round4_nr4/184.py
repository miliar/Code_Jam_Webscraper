#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;

int k,len;
char c[50010],cc[50010];

int rle(char c[],int len)
{
	int i,tot=0;
	for(i=1;i<=len;i++)
	{
		if(i==1 || c[i]!=c[i-1]) tot++;
	}
	return tot;
}

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);

	int T1,T,i;
	scanf("%d",&T);
	for(T1=1;T1<=T;T1++)
	{
		scanf("%d",&k);
		scanf("%s",&c[1]);
		len=strlen(&c[1]);

		vector<int> p;
		for(i=0;i<=k-1;i++)
		{
			p.push_back(i);
		}

		memcpy(cc,c,sizeof(c));
		int ans=1e9;
		do
		{
	//		memcpy(c,cc,sizeof(cc));
			for(i=1;i<=len;i++)
			{
				int b=(i-1)/k;
				int r=(i-1)%k;

				c[i]=cc[b*k+p[r]+1];
			}
			int tnum=rle(c,len);
			if(tnum<ans) ans=tnum;
		}
		while(next_permutation(p.begin(),p.end()));

		printf("Case #%d: %d\n",T1,ans);
	}
	return 0;
}
