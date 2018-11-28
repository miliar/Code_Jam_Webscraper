#include<stdio.h>
#include<stdlib.h>
//#include<algorithm>
//#include<vector>

//using namespace std;

typedef long long ll;

int l,d,n;

char s[5001][20];

main(){
	int i,j,k,ans;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	for(i=1;i<=d;++i)scanf("%s",s[i]);
	for(i=1;i<=n;++i){
		char *buf=new char[500];
		char in[16][0x100]={{}};
		scanf("%s",buf);
		for(j=0;j<l;++j){
			if(*buf=='('){
				do{
					in[j][*buf]=1;
				}while(*buf++!= ')');
			}else{
				in[j][*buf++]=1;
			}
		}
		ans=0;
		for(j=1;j<=d;++j){
			for(k=0;in[k][s[j][k]];++k){
				if(k==l-1){++ans;break;}
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}
}
