#include <cstdio>
#include <cstring>

int n,s,q,x,a[105][1005];
char e[105][105],str[105];

int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	int t,res;
	scanf("%d",&n);
	for(t=1; t<=n; t++)
	{
		int i,j;

		scanf("%d",&s);
		gets(str);
		for (i=0; i<s; i++)
		{
			gets(e[i]);
		}
		scanf("%d",&q);
		gets(str);
		for (i=0; i<q; i++)
		{
			gets(str);
			for (j=0; j<s; j++)
			{
				if (!strcmp(str,e[j]))
				{
					a[j][i]=0;
				}
				else
				{
					a[j][i]=1;
				}
			}
		}
		if (q==0)
		{
			res=0;
		}
		else
		{
			int m, im;
			res=-1;
			x=0;
			while(x<q)
			{
				m=0;
				im=-1;
				for (i=0; i<s; i++)
				{
					j=x;
					while(a[i][j]==1)
					{
						j++;
					}
					if (j-x>m)
					{
						m=j-x;
						im=i;
					}
				}
				x+=m;
				res++;
			}
		}
		printf("Case #%d: %d\n",t,res);
	}
	return 0;
}

/*
2
1
qwe
0
ewq

2
5
Yeehaw
NSM
Dont Ask
B9
Googol
10
Yeehaw
Yeehaw
Googol
B9
Googol
NSM
B9
NSM
Dont Ask
Googol
5
Yeehaw
NSM
Dont Ask
B9
Googol
7
Googol
Dont Ask
NSM
NSM
Yeehaw
Yeehaw
Googol

*/