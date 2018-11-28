#include <iostream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.in","w",stdout);
	int i,j,k,l,m,n;
	char c[55][55],s[55][55];
	int t;
	scanf("%d",&t);
	for(int zzz=1;zzz<=t;zzz++){
		printf("Case #%d:\n",zzz);
		scanf("%d%d",&n,&m) ;
		for(i=0;i<n;i++)
			scanf("%s",c[i]);
		memset(s,0,sizeof(0));
		for(i=0;i<n-1;i++)
			for(j=0;j<m-1;j++)
				if(c[i][j]=='#' && c[i][j+1]=='#' && c[i+1][j+1]=='#' && c[i+1][j]=='#'){
					s[i][j]='/';s[i][j+1]='\\';s[i+1][j+1]='/';s[i+1][j]='\\';
					c[i][j]='.';c[i][j+1]='.';c[i+1][j+1]='.';c[i+1][j]='.';
				}
		bool b=0;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++){
				if(c[i][j]=='#')
					b=1;
				if(s[i][j]==0)
					s[i][j]='.';
			}
		if(b)printf("Impossible\n");
		else 
			for(i=0;i<n;i++,puts(""))
				for(j=0;j<m;j++)
					printf("%c",s[i][j]);
	}
	return 0;
}
