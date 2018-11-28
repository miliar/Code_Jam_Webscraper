#include<stdio.h>
#define maxl 20
#define maxd 5050
int l,d,n;
char s[maxd][maxl],s1[maxl*30];

bool find(char c,char s[],int & p)
{
	if(s[p]=='(')
	{
		int b=p,e=p+1;
		while(s[e]!=')') ++e;
		p=e+1;
		for(int i=b+1;i<e;++i)
			if(s[i]==c) return 1;
		return 0;
	}
	else return s[p++]==c;
}

bool cmp(char s1[],char s2[])
{
	int p=0;
	for(int i=0;i<l;++i)
		if(!find(s1[i],s2,p))
			return 0;
	return 1;
}

int main()
{
	scanf("%d%d%d",&l,&d,&n);
	for(int i=0;i<d;++i)
		scanf("%s",s[i]);
	for(int i=0;i<n;++i)
	{
		int re=0;
		scanf("%s",s1);
		for(int j=0;j<d;++j)
			if(cmp(s[j],s1))
				++re;
		printf("Case #%d: %d\n",i+1,re);
	}
	return 0;
}

