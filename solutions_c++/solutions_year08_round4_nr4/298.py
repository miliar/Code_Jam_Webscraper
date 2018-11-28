#include <cstdio>
#define lmax 1005

char s[lmax],s1[lmax];
int k,ans,l;
bool u[6];
int num[6];

void check()
{
	int i,j;
	for(i=0;i<l/k;i++)
		for(j=0;j<k;j++) s1[i*k+j]=s[i*k+num[j]];
	j=1;
	for(i=1;i<l;i++)
		if (s1[i]!=s1[i-1]) ++j;
	if (j<ans) ans=j;
}

void rec(int l)
{
	if (l==k)
	{
		check();
		return;
	}
	for(int i=0;i<k;i++)
		if (!u[i])
		{
			u[i]=true;
			num[l]=i;
			rec(l+1);
			u[i]=false;
		}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,T;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d",&k); gets(s);
		gets(s);
		for(l=0;s[l];l++);
		ans=10000;
		for(int i=0;i<k;i++) u[i]=false;
		rec(0);
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}