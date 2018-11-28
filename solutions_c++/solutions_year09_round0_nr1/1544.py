#include <stdio.h>
#include <string.h>
char a[5000][20];
char c[500];
bool b[15][26];
int main(){
	int l,d,n;
	scanf("%d%d%d",&l,&d,&n);
	for(int i=0;i<d;i++){
		scanf("%s",&a[i]);
	}
	for(int i=1;i<=n;i++){
		scanf("%s",c);
		memset(b,0,sizeof(b));
		int p=0;
		for(int j=0;j<l;j++){
			if(c[p] == '('){
				p++;
				while(c[p] != ')'){
					b[j][c[p]-'a']=1;
					p++;
				}
				p++;
			}else{
				b[j][c[p]-'a']=1;
				p++;
			}
		}
		int cnt=0;
		for(int k=0;k<d;k++){
			bool ok=1;
			for(int j=0;j<l;j++){
				if(!b[j][a[k][j]-'a']){
					ok=0;
					break;
				}
			}
			if(ok)
				cnt++;
		}
		printf("Case #%d: %d\n",i,cnt);
	}
}