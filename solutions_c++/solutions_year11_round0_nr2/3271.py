//B

#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	//files
	freopen("b.in","r",stdin);
	freopen("out.txt","w",stdout);
	//vars
	int T,t;
	int n,m,len,a,c;
	char c1,c2,c3;
	int comb[30][30];
	bool opp[30][30];
	int lst[1000];
	//testcase loop
	scanf("%d",&T);
		for (t=1; t<=T; t++)
		{
			//init
			memset(comb,-1,sizeof(comb));
			memset(opp,0,sizeof(opp));
			//input
			scanf("%d ",&m);
				while (m--)
				{
					scanf("%c%c%c ",&c1,&c2,&c3);
					comb[c1-'A'][c2-'A']=c3-'A';
					comb[c2-'A'][c1-'A']=c3-'A';
				}
			scanf("%d ",&m);
				for (a=0; a<m; a++)
				{
					scanf("%c%c ",&c1,&c2);
					opp[c1-'A'][c2-'A']=1;
					opp[c2-'A'][c1-'A']=1;
				}
			scanf("%d ",&len);
			//simulate
			n=0;
				for (a=0; a<len; a++)
				{
					scanf("%c",&c1);
					lst[n++]=c1-'A';
						if (n>1)
						{
							c=comb[lst[n-1]][lst[n-2]];
								if (c>=0)
								{
									n--;
									lst[n-1]=c;
								}
								else
								for (c=0; c<n-1; c++)
									if (opp[lst[n-1]][lst[c]])
										n=0;
						}
				}
				if (t<T)
					scanf("\n");
			//output
			printf("Case #%d: [",t);
				for (a=0; a<n; a++)
				{
						if (a)
							printf(", ");
					printf("%c",lst[a]+'A');
				}
			printf("]\n");
		}
	return(0);
}