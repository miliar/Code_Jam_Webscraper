#include<stdio.h>
char s[51][51];
long t,tt,i,j,k,l,n,m;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	for(scanf("%ld",&t),tt=0;tt<t;){
		scanf("%ld%ld",&n,&m);
		gets(s[0]);
		for(i=0;i<n;++i) gets(s[i]);
		printf("Case #%ld:\n",++tt);
		for(i=0;i<n-1;++i){
			for(j=0;j<m-1;++j)
				if(s[i][j]=='#'){
					if(s[i][j+1]=='#'&&s[i+1][j]=='#'&&s[i+1][j+1]=='#')
						s[i][j]=s[i+1][j+1]='/',s[i+1][j]=s[i][j+1]='\\';
					else{
						puts("Impossible");goto end;
						}
					}
			if(s[i][j]=='#'){
				puts("Impossible");goto end;
				}
			}
		for(j=0;j<m;++j) if(s[i][j]=='#') {puts("Impossible");goto end;}
		for(i=0;i<n;++i) puts(s[i]);
		end:;
		}
	scanf("%ld",&t);
	return 0;
}
