#include <stdio.h>
#include <string.h>
char com[128][128],op[128][128];

void invoke(char c, char res[], int& n)
{
	int i;
	if (com[c][res[n-1]])
	{
		res[n-1]=com[c][res[n-1]];
		return;
	}
	for (i=0; i<n; i++)
	{
		if (op[res[i]][c]) {
			n=0;
			return;
		}
	}
	res[n++]=c;
	return;
}
	

int main()
{
	int t,n,c,d,i,res_n;
	char s[102],res[102];
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for (int cas = 1; cas<=t; cas++)
	{
		scanf("%d",&c);
		memset(com,0,sizeof(char)*128*128);
		memset(op,0,sizeof(char)*128*128);
		for (i=0; i<c; i++)
		{
			scanf("%s",s);
			com[s[0]][s[1]]=s[2];
			com[s[1]][s[0]]=s[2];
		}
		scanf("%d",&d);
		for (i=0; i<d; i++)
		{
			scanf("%s",s);
			op[s[0]][s[1]]=1;
			op[s[1]][s[0]]=1;
		}
		scanf("%d",&n);
		scanf("%s",s);
		res_n = 0;
		for (i=0; i<n; i++)
		{
			invoke(s[i],res,res_n);
		}
		res[res_n]=0;
		printf("Case #%d: [",cas);
		if (res_n>0) printf("%c",res[0]);
		for (i=1; i<res_n; i++) printf(", %c",res[i]);
		printf("]\n");
	}
	return 0;
}
