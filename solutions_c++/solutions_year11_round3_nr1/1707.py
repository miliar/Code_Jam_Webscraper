#include<cstdio>

int t,x,y;

char tab[57][57];

bool wklej(int px, int py){
	if(px+1>x || py+1>y) return 1;
	if(tab[px+1][py]=='.' || tab[px][py+1]=='.' || tab[px+1][py+1]=='.') return 1;
	else{
		tab[px][py]='/';
		tab[px+1][py]='\\';
		tab[px+1][py+1]='/';
		tab[px][py+1]='\\';
		return 0;
	}
}

void fajt(int kejs){
	for(int i=1; i<=x; i++){
		for(int j=1; j<=y; j++){
			if(tab[i][j]=='#'){
				if(wklej(i,j)){
					printf("Impossible\n");
					return;
				}
			}
		}
	}

	for(int i=1; i<=x; i++){
		for(int j=1; j<=y; j++){
			printf("%c",tab[i][j]);
		}
		printf("\n");
	}
}

int main(){
	scanf("%d",&t);
	for(int ccc=1; ccc<=t; ccc++){
		printf("Case #%d:\n",ccc);
		scanf("%d%d ",&x,&y);
		for(int i=1; i<=x; i++){
			for(int j=1; j<=y; j++){
				tab[i][j]=getchar();
			}
			getchar();
		}
		fajt(ccc);
	}
}

