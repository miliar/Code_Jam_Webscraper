#include <iostream>

int check[30][30],check2[30][30];
char c[200],tot;

void doing()
{
	memset(check,0,sizeof(check));
	memset(check2,0,sizeof(check2));
	int n;
	scanf("%d ",&n);
	for (int i=0;i<n;i++)
	{
		char c1,c2,c3;
		scanf("%c%c%c ",&c1,&c2,&c3);
		check[c1-'A'][c2-'A']=c3-'A'+1;
		check[c2-'A'][c1-'A']=c3-'A'+1;
	}
	scanf("%d ",&n);
	for (int i=0;i<n;i++)
	{
		char c1,c2;
		scanf("%c%c ",&c1,&c2);
		check2[c1-'A'][c2-'A']=-1;
		check2[c2-'A'][c1-'A']=-1;
	}
	tot=0;
	scanf("%d ",&n);
	for (int i=0;i<n;i++)
	{
		scanf("%c",&c[tot]);
		while (tot>=1 && check[c[tot]-'A'][c[tot-1]-'A']>0)
		{
			c[tot-1]=char('A'+check[c[tot]-'A'][c[tot-1]-'A']-1);
			tot-=1;
		}
		for (int j=0;j<tot;j++)
			if (check2[c[tot]-'A'][c[j]-'A']==-1) tot=-1;		
		tot++;
	}
	printf("[");
	if (tot!=0)
	{
		printf("%c",c[0]);
		for (int i=1;i<tot;i++) printf(", %c",c[i]);
	}
	printf("]\n");
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int casenum;
	scanf("%d\n",&casenum);
	for (int cc=1;cc<=casenum;cc++)
	{
		printf("Case #%d: ",cc);
		doing();
	}
}
