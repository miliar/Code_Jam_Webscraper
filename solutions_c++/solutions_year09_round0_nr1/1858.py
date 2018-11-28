#include <stdio.h>
#include <string.h>
int l,d,n;
char dict[5003][20];
char str[20000];
int chkar[20000][26];
int main(){
	int i,j;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	for(i=0;i<d;i++){
		scanf("%s",dict[i]);
	}
	for(i=0;i<n;i++){
		scanf("%s",str);
		int np = 0;
		int par = 0;
		memset(chkar[np],0,sizeof(chkar[np]));
		for(j=0;str[j];j++){
			if(str[j] == '('){
				par ++;
			}else if(str[j] == ')'){
				par --;
				np++;
				memset(chkar[np],0,sizeof(chkar[np]));
			}
			else if(str[j] != '('){
				chkar[np][str[j]-'a'] ++;
				if(par == 0){
					np ++;
				}
			}
		}
		int ans = 0;
		for(j=0;j<d;j++){
			if(dict[j][np] == 0 && dict[j][np-1] != 0){
				int k;
				for(k=0;k<np;k++){
					if(chkar[k][dict[j][k]-'a'] == 0){
						break;
					}
				}
				if(k >= np){
					ans ++;
				}
			}
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}
