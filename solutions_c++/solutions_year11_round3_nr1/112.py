#include<cstdio>
int t,r,c,ok;
char s[55][55];
int main(){
	scanf("%d",&t);
	for (int z=1; z<=t; z++){
		scanf("%d%d",&r,&c);
		for (int i=0; i<r; i++)
		    scanf("%s",s[i]);
		ok=1;
		for (int i=0; i<r; i++)
		    for (int j=0; j<c; j++){
				if (s[i][j]!='#') continue;
				if ((i==r-1)||(j==c-1)){
				   ok=0; continue;
				}
				if (s[i+1][j]=='#'&&s[i][j+1]=='#'&&s[i+1][j+1]=='#'){
				   s[i][j]='/'; s[i+1][j+1]='/';
				   s[i+1][j]='\\'; s[i][j+1]='\\';
				}
				else ok=0;
			}
		if (!ok) printf("Case #%d:\nImpossible\n",z);
		else{
			 printf("Case #%d:\n",z);
			 for (int i=0; i<r; i++) printf("%s\n",s[i]);
		}
	}
	return 0;
}
