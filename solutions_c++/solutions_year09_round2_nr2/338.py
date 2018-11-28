#include<iostream>
using namespace std;
int ex,f[10],n;
char i[100],b[100];
void dfs(int depth,int more)
{
	int a,t;
	if( depth==n ){ if( more==1 ) ex=1; return; }
	if( more==1 )
	{
		for(a=0;a<10;a++)
		{
			if( f[a]>0 )
			{
				f[a]--;
				b[depth]='0'+a;
				dfs(depth+1,1);
				if( ex==1 ) return;
				f[a]++;
			}
		}
		return;
	}
	t=i[depth]-'0';
	for(a=t;a<10;a++)
	{
		if( f[a]>0 )
		{
			f[a]--;
			b[depth]='0'+a;
			dfs(depth+1,(a>t?1:0));
			if( ex==1 ) return;
			f[a]++;
		}
	}
}
int main()
{
	int a;
int T,X;
scanf("%d",&T);
for(X=1;X<=T;X++)
{
	printf("Case #%d: ",X);
	i[0]='0';
	scanf("%s",i+1);
	n=strlen(i);
	for(a=0;a<10;a++) f[a]=0;
	for(a=0;a<n;a++) f[i[a]-'0']++;
	ex=0;
	dfs(0,0);
	b[n]=0;
	for(a=0;a<n;a++) if( b[a]!='0' ) break;
	printf("%s\n",b+a);
}
	return 0;
}
