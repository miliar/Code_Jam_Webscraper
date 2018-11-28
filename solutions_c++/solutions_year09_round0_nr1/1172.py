#include <stdio.h>
#include <string.h>

int L,D,N;

char w[16];
long wn[5000][15];
long mi[27];
char s[2];
int t[200];
long p[16];


int main()
{
	freopen("A-large.in.txt","r",stdin);
//	freopen("a2.txt","r",stdin);
	freopen("a.out","w",stdout);

	scanf("%d %d %d",&L,&D,&N);
	long i,j,k,l;
	long cc=0;
	mi[0]=1;
	
	for (i=1;i<27;i++)
	{
		mi[i]=mi[i-1]*2;
//		printf("%ld\n",mi[i]);
	}
	for (i=0;i<D;i++)
	{
		scanf("%s\n",&w);

		for (j=0;j<L;j++)
		{
			wn[i][j]=mi[w[j]-'a'];
//			printf("%c:%d ",w[j],wn[i][j]);
		}
//		printf("\n");
		
//		printf("%s\n",w[i]);
	}

	int tt;
	char ch;
	for (tt=1;tt<=N;tt++)
	{

		i=0;
	
		int answer=0;
		memset(p,0,sizeof(p));
		for (i=0;i<L;i++)
		{
			scanf("%c",&ch);
//			printf("%c",ch);
			if (ch=='(')
			{
				while (scanf("%c",&ch))
				{
//					printf("%c",ch);
					if (ch==')') break;
					p[i]+=mi[ch-'a'];
				}
			}
			else
			{
				p[i]=mi[ch-'a'];
			}

//			printf("%d ",p[i]);
		}
		scanf("\n");
//		printf("\n");

		answer=0;
		for (i=0;i<D;i++)
		{
			for (j=0;j<L;j++)
			{
//				printf("%d:%d=%d  ",wn[i][j],p[j],wn[i][j]&p[j]);
				if ((wn[i][j]&p[j])==0)
				{
					break;
				}
			}
//			printf("\n");
			if (j==L)
			{
				answer++;
			}
		}

		printf("Case #%d: %d\n",tt,answer);
	}

	return 0;
}
