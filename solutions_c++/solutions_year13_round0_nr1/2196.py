#include <cstdio>
#include <cstring>
#define fr(i,a,b) for(int i=a;i<b;i++)
#define rep(i,b) fr(i,0,b)
using namespace std;

char s[10][10];

int pdt(int *c, char ch){
	if(ch=='O') c[0]++;
	else if(ch=='X') c[1]++;
	else if(ch=='T') c[2]++;
}

int calc(int *c){
	if(c[0]==4 || (c[0]==3 && c[2]==1)) return 0;
	if(c[1]==4 || (c[1]==3 && c[2]==1)) return 1;
	return -1;
}

int cnt[4];
int func(){	
	int venc=-1;
	rep(i,4){
		memset(cnt,0,sizeof(cnt));
		rep(j,4) pdt(cnt,s[i][j]);
		if((venc=calc(cnt))!=-1) return venc;
		
		memset(cnt,0,sizeof(cnt));
		rep(j,4) pdt(cnt,s[j][i]);
		if((venc=calc(cnt))!=-1) return venc;
	}
	
	memset(cnt,0,sizeof(cnt));
	rep(j,4) pdt(cnt,s[j][j]);
	if((venc=calc(cnt))!=-1) return venc;
		
	memset(cnt,0,sizeof(cnt));
	rep(j,4) pdt(cnt,s[j][3-j]);
	if((venc=calc(cnt))!=-1) return venc;
}

int main(){
	int cas;
	scanf("%d",&cas);
	rep(u,cas){
		int qtd=0;
		rep(i,4){
			scanf("%s",s[i]);
			rep(j,4) qtd += s[i][j]=='.'?0:1;
		}
		int venc = func();
		printf("Case #%d: ",u+1);
		if(venc==0) printf("O won");
		else if(venc==1) printf("X won");
		else if(qtd==16) printf("Draw");
		else printf("Game has not completed");
		printf("\n");
	}
	return 0;
}

