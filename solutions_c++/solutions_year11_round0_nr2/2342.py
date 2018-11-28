#include <stdio.h>

#define ab(x) (((x)>=0)?(x):(-(x)))

int main()
{
	int n,ca=0,i,m,j,a,b;
	char s[1000];
	char q[1000];
	char com[1000][4];
	char opo[1000][4];
	scanf("%d",&n);
	while (scanf("%d",&n)==1)
	{
		for (i=0;i<n;++i) scanf("%s",com[i]);
		scanf("%d",&m);
		for (i=0;i<m;++i) scanf("%s",opo[i]);
		scanf("%d",&i);
		scanf("%s",s);
		q[0]=0;
		j=0;
		for (i=0;s[i];++i)
		{
			q[j++]=s[i];
			if (j>=2) for (a=0;a<n;++a) if ((com[a][0]==q[j-1] && com[a][1]==q[j-2]) || (com[a][1]==q[j-1] && com[a][0]==q[j-2]))
			{
				--j;
				q[j-1]=com[a][2];
				break;
			}
			if (j>=2 && a==n) for (a=0;a<m;++a) for (b=0;b<j-1;++b) if ((opo[a][0]==q[j-1] && opo[a][1]==q[b]) || (opo[a][1]==q[j-1] && opo[a][0]==q[b]))
			{
				j=0;
				break;
			}
		}
		printf("Case #%d: [",++ca);
		for (i=0;i<j;++i)
		{
			if (i>0) printf(", ");
			printf("%c",q[i]);
		}
		printf("]\n");
	}
	return 0;
}
