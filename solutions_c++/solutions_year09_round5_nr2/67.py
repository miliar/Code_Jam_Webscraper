#include<stdio.h>
#include<string.h>

const int MOD =  10009;

int a[11][26];

char str[1111];
char *ss;
int K, kk;
int n, m;
int b[100][26];
int perm[111];
int ohyes[26];
int ret;

void Go(int Dep)
{
	if(Dep == kk)
	{
		int l1, l2, l3;
		for(l1=0;l1<26;l1++)
		{
			ohyes[l1] = 0;
		}
		for(l1=0;l1<Dep;l1++)
		{
			for(l2=0;l2<26;l2++)
			{
				ohyes[l2] += b[ perm[l1] ][ l2];
			}
		}

		for(l1=0;l1<n;l1++)
		{
			int acc = 1;
			for(l2=0;l2<26;l2++)
			{
				for(l3=0;l3<a[l1][l2];l3++)
				{
					acc *= ohyes[l2];
				}
			}
			ret += acc;
			ret %= MOD;
		}
	}
	else
	{
		int l1;
		for(l1=0;l1<m;l1++)
		{
			perm[Dep] = l1;
			Go(Dep + 1);
		}
	}
}

int main(void)
{

	freopen("B1.in","r",stdin);
	freopen("B1.out","w",stdout);
	int l0, l1, l2;
int T;
	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%s",str);
		n = 0;
		for(ss=strtok(str,"+");ss;ss=strtok(NULL,"+"))
		{
			for(l1=0;l1<26;l1++) a[n][l1] = 0;
			for(l1=0;ss[l1];l1++)
			{
				a[n][ss[l1]-'a']++;
			}
			n++;
		}
		scanf("%d",&K);
		scanf("%d",&m);
		for(l1=0;l1<m;l1++)
		{
			scanf("%s",str);
			for(l2=0;l2<26;l2++) b[l1][l2] = 0;
			for(l2=0;str[l2];l2++)
			{
				b[l1][str[l2] - 'a']++;
			}
		}

		printf("Case #%d:",l0);
		for(kk=1;kk<=K;kk++)
		{
			ret = 0;
			Go(0);
			ret %= MOD;
			printf(" %d",ret);
		}
		printf("\n");
	}
}