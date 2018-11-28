#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

char a[100][10],b[100][10],c[300],d[1000];
int mrk[100];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas=1;cas<=T;cas++)
	{
		printf("Case #%d: ",cas);
		int C,D,E;
		scanf("%d",&C);
		for (int i=0;i<C;i++) scanf("%s",a[i]);
		scanf("%d",&D);
		for (int i=0;i<D;i++) scanf("%s",b[i]);
		int N,top=0;
		scanf("%d",&N);
		scanf("%s",c);
		memset(mrk,0,sizeof(mrk));
		for (int i=0;i<N;i++)
		{
			d[top++]=c[i];
			mrk[c[i]-'A']++;
			while (true)
			{
				bool flag=true;
				if (top<2) break;
				for (int j=0;j<C;j++)
					if ((a[j][0]==d[top-1] && a[j][1]==d[top-2]) || (a[j][1]==d[top-1] && a[j][0]==d[top-2]))
					{
						mrk[a[j][0]-'A']--;
						mrk[a[j][1]-'A']--;
						top-=2;
						mrk[a[j][2]-'A']++;
						d[top]=a[j][2];top++;
						flag=false;break;
					}
				if (flag) break;
			}
			bool f1=true;
			for (int j=0;j<D;j++)
			{
				if (mrk[b[j][0]-'A'] && mrk[b[j][1]-'A'])
				{
					f1=false;break;
				}
			}
			if (!f1) 
			{
				top=0;
				memset(mrk,0,sizeof(mrk));
			}
		}
		if (top<=0) puts("[]");
		else
		{
			printf("[");
			for (int i=0;i<top-1;i++)
				printf("%c, ",d[i]);
			printf("%c",d[top-1]);
			printf("]\n");
		}
	}
}