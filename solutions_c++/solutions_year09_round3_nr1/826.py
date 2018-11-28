#include <stdio.h>
#include <string.h>

char s[100];
int n;
int a[200];
int m;	//base
int v[200];


int main(int argc, char *argv[])
{
	freopen("A-large.in.txt","r",stdin);
	freopen("a.out","w",stdout);
	
	int T;
	int tt;

	scanf("%d",&T);

	unsigned long long ans;
	int used;

	unsigned long long mi;
	int i,j;

	for (tt=1;tt<=T;tt++)
	{
		scanf("%s",&s);
		memset(a,0,sizeof(a));
		n=strlen(s);
		for (i=0;i<n;i++)
		{
			a[int(s[i])]++;
			/*
			if (s[i]>='0' && s[i]<='9')
			{
				j=s[i]-'0';
			}
			else
			{
				j=s[i]-'a';
			}
			a[j]=1;
			*/
		}

		m=0;
		for (i=0;i<200;i++)
		{
			if (a[i])
			{
				m++;
			}
		}
		if (m==1)
		{
			m=2;
		}

		for (i=0;i<200;i++)
		{
			v[i]=-1;
		}
		
		used=1;
		v[s[0]]=1;

		for (i=1;i<n;i++)
		{
			if (v[s[i]]==-1)
			{
				if (used==1)
				{
					v[s[i]]=0;
//					printf("%c = %d\n",s[i],0);
				}
				else
				{
					v[s[i]]=used;
//					printf("%c = %d\n",s[i],used);
				}
				used++;
			}
		}

		ans=0;
		mi=1;
		
		for (i=n-1;i>=0;i--)
		{
			ans+=v[s[i]]*mi;
			mi*=m;
		}

		printf("Case #%d: %I64d\n",tt,ans);


	}



	return 0;
}
