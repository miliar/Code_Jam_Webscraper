#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>
using namespace std;


char com[200][20],opp[200][20],q[200],s[200];

int tes,c,d,n,top;

int main()
{	
	freopen("b.out","w",stdout);
	scanf("%d",&tes);
	for (int ttt=1;ttt<=tes;ttt++)
	{
		scanf("%d",&c);
		for (int i=1;i<=c;i++)
		{
			scanf("%s",com[i]);
		}
		scanf("%d",&d);
		for (int i=1;i<=d;i++)
		{
			scanf("%s",opp[i]);
		}
		scanf("%d",&n);
		scanf("%s",s);
		top=0;
		for (int i=0;i<n;i++)
		{
		/*	printf("[");
			for (int ii=1;ii<=top;ii++)
			{
				if (ii>1) printf(", ");
				printf("%c",q[ii]);
			}
			printf("]   %c\n",s[i]);
			*/
			top++; q[top]=s[i];
			int o1=0,o2=0;
			if (top>1)
			{
				for (int ii=1;ii<=c;ii++)
				{
					if ((com[ii][0]==q[top] && com[ii][1]==q[top-1]) || (com[ii][0]==q[top-1] && com[ii][1]==q[top])) { o1=1; top--; q[top]=com[ii][2]; break; }
				}
			}
			if (o1) continue;
			for (int ii=1;ii<=d;ii++)
			{
				if (opp[ii][0]==q[top] || opp[ii][1]==q[top])
				{
					for (int tt=1;tt<top;tt++)
						if (q[tt]!=q[top] && (opp[ii][0]==q[tt] || opp[ii][1]==q[tt])) { o2=1; top=0; break; }
				}
				if (o2) break;
			}
		}
		printf("Case #%d: ",ttt);
		printf("[");
		for (int i=1;i<=top;i++)
		{
			if (i>1) printf(", ");
			printf("%c",q[i]);
		}
		printf("]\n");
	}
	return 0;
}
