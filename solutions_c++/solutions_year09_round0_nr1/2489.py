#include <cstdio>
#include <cstring>
char a[6000][20];
bool ok[20]['z'+2];
int i,l,d,n,I,j,t,k;
char st[20];
main()
{
	scanf("%d%d%d\n",&l,&d,&n);
	for (i=0;i<d;++i)
		gets(a[i]);
	for (I=0;I<n;++I)
	{
		gets(st);
		memset(ok,0,sizeof ok);
		t=0;
		k=0;
		if (st[0]=='(') k=1;
		for (i=0;i<strlen(st);++i)
		{
			if (st[i]=='(')
				++t;
			else if (st[i]==')') --t;
			if (t==0) ++k;
			ok[k-1][st[i]]=1;
		}
		int ans=0;
		for (i=0;i<d;++i)
		{
			bool f=1;
			for (j=0;j<strlen(a[i]);++j)
			    if (!ok[j][a[i][j]])
			    {
					f=0;
					break;
				}
			if (f) ++ans;
		}
		printf("Case #%d: %d\n",I+1,ans);
	}
	return 0;
}
