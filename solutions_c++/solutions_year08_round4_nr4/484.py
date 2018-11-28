#include<cstdio>
#include<algorithm>

const int ml=50005,mn=20;
char s[ml],t[ml];
int n,T,a[mn];
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int tn=1;tn<=T;tn++)
	{
		scanf("%d%s",&n,s);
		for(int i=0;i<n;i++)a[i]=i;

		int ans=0x7fffffff;
		do
		{
			int p=0;
			while(s[p*n])
			{
				for(int i=0;i<n;i++)t[p*n+i]=s[p*n+a[i]];
				p++;
			}
			int cur=1;
			for(int i=1;s[i];i++)
				if(t[i]!=t[i-1])cur++;
			ans<?=cur;
		}while(std::next_permutation(a,a+n));
		printf("Case #%d: %d\n",tn,ans);
	}
	return 0;
}
