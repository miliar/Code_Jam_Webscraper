#include<cstdio>
#include<cstring>
#define MAXS 100
#define MAXL 100
#define MAXQ 1000
#define INF 0x3fffffff
using namespace std;
int n,s,q;
char eng[MAXS+1][MAXL+1];
int f[MAXS+1];
char data[MAXL+1];
int main()
{
	int i,l,j,k,tmp,minstep;
	scanf("%d",&n);
	for(l=1;l<=n;++l)
	{
		scanf("%d",&s);
		getchar();
		for(i=1;i<=s;++i)gets(eng[i]);
		scanf("%d",&q);
		getchar();
		for(i=1;i<=q;++i)
		{
			gets(data);
			if(i==1)
				for(j=1;j<=s;++j)
					if(strcmp(data,eng[j])==0)
						f[j]=INF;
					else 
						f[j]=0;
			for(j=1;j<=s;++j)
				if(strcmp(data,eng[j])==0){
					tmp=j;
					break;
				}
			for(j=1;j<=s;++j)
				if(j!=tmp&&f[tmp]+1<f[j])
					f[j]=f[tmp]+1;
			f[tmp]=INF;
			//for(j=1;j<=s;++j)
			//	printf("%d\t",f[j]);			
			//putchar('\n');
		}
		minstep=INF;
		for(j=1;j<=s;++j)
			minstep<?=f[j];
		printf("Case #%d: %d\n",l,minstep);
	}
}
