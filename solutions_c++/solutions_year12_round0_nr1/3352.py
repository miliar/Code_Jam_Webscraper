#include<cstdio>
#include<cstring>
char s[105];
char conversion[31],conversion2[31];
int t,n; char ch,cc;
int main()
{
	freopen("tongues.in","r",stdin);
	freopen("tongues.out","w",stdout);
	scanf("%d\n",&t);
	strcat(conversion,"ynficwlbkuomxsevzpdrjgthaq");
	strcat(conversion2,"yhesocvxduiglbkrztnwjpfmaq");
	int i;
	for(int test=1;test<=t;++test)
	{
		gets(s+1);
		for(n=1;s[n];++n); n--;
		for(i=1;i<=n;++i)
			if((s[i]>='a')&&(s[i]<='z'))
				s[i]=conversion2[s[i]-97];
		printf("Case #%d: ",test);
		for(i=1;i<=n;++i)
			printf("%c",s[i]);
		printf("\n");
	}
	return 0;
}
