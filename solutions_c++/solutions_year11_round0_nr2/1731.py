#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <cstdio>
#include <string>

using namespace std;

int n,t,c,d,anst;
char com[40][4],ops[30][3],str[200],ans[200];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("ans.txt","w",stdout);
	scanf("%d",&t);
	for(int ii=1;ii<=t;ii++)
	{
		scanf("%d",&c);
		for(int i=0;i<c;i++)
			scanf("%s",com[i]);
		scanf("%d",&d);
		for(int i=0;i<d;i++)
			scanf("%s",ops[i]);
		scanf("%d",&n);
		scanf("%s",str);
		anst=0;
		for(int i=0;i<n;i++)
		{
			ans[anst++]=str[i];
			if(anst<2) continue;
			while(1)
			{
				bool over=true;
				for(int j=0;j<c;j++)
					if(anst>=2&&(com[j][0]==ans[anst-1]&&com[j][1]==ans[anst-2])||(com[j][1]==ans[anst-1]&&com[j][0]==ans[anst-2]))
				{
					over=false;
					ans[anst-2]=com[j][2];
					anst--;
				}
				if(over) break;
			}

			for(int j=0;j<d;j++)
				if(anst>=2&&ops[j][0]==ans[anst-1]||ops[j][1]==ans[anst-1])
				{
					bool cleared=false;
					for(int k=anst-2;k>=0;k--)
					{
						if(ops[j][0]==ans[anst-1]&&ops[j][1]==ans[k])
							{anst=0;cleared=true;break;}
						if(ops[j][1]==ans[anst-1]&&ops[j][0]==ans[k])
							{anst=0;cleared=true;break;}
					}
					if(cleared) break;
				}
		}
		printf("Case #%d: [",ii);
		if(anst) printf("%c",ans[0]);
		for(int i=1;i<anst;i++)
			printf(", %c",ans[i]);
		printf("]\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}