#include<stdio.h>
#include<string.h>
char s[1000],t[1000],ch[100][100];
int n;

double dfs(int l,int h)
{
	if (l>=h) return 1.00;
	while (s[l]!='(') l++;
	while (s[h]!=')') h--;
	l++;
	h--;
	char *p,*q;
	int i,left,right;
	double prob;
	p=s;
	p=p+l;
	char name[100];
	if (sscanf(p,"%lf %s%n",&prob,&name,&i)==1)
	{
		return prob;
	}
	p=p+i;
	while ((*p)!='(') p=p+1;
	q=p;
	p++;
	left=1;
	right=0;
	while (left>right)
	{
		if ((*p)=='(') left++;
		else
		if ((*p)==')') right++;
		p=p+1;
	}
	for (i=0;i<n;i++) if (!strcmp(ch[i],name)) break;
	if (i<n)
		return prob*dfs(q-s,p-s-1);
	else
		return prob*dfs(p-s,h);
}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.txt","w",stdout);
	
	int T,k,i,L,A;
	char *p;
	scanf("%d",&T);
	for (k=1;k<=T;k++)
	{
		memset(s,0,sizeof s);
		printf("Case #%d:\n",k);
		scanf("%d\n",&L);
		p=s;
		for (i=0;i<L;i++) 
		{
			gets(p);
			p=s+strlen(s);
		}
		*p='\0';
		//printf("%s\n",s);
		scanf("%d",&A);
		while (A--)
		{
			scanf("%s %d",t,&n);
			for (i=0;i<n;i++) scanf("%s",&ch[i]);
			printf("%.7f\n",dfs(0,strlen(s)-1));
		}
	}
}
