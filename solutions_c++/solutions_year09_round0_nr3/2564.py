#include<cstdio>
#include<cstring>

char a[1000],b[]="welcome to code jam";
int f[1000][50];
main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	scanf("%d\n",&n);
	for(int kase=1;kase<=n;kase++){
		gets(a);
		memset(f,0,sizeof(f));
		int i,j;
		for(i=0;a[i];i++)
			for(j=0;b[j];j++){
				if(i)(f[i][j]+=f[i-1][j])%=1000;
				if(a[i]==b[j])
					if(i)
						if(j)(f[i][j]+=f[i-1][j-1])%=1000;
						else (f[i][j]+=1)%=1000;
					else 
						if(j)f[i][j]=0;
						else f[i][j]=1;
			}
		printf("Case #%d: %0*d\n",kase,4,f[i-1][j-1]);
	}
}
