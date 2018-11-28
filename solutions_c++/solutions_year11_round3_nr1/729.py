#include <cstdio>
#include <vector>
#include <cmath>
#include <string>
#define FOR(x,y,z) for(int (x)=(y);(x)<(z);(x)++)
#define FORQ(x,y,z) for(int (x)=(y);(x)<=(z);(x)++)
#define FORDQ(x,y,z) for(int (x)=(y);(x)>=(z);(x)--)
#define R 60
using namespace std;
char tab[R][R];
int n,m;
void change(int x,int y){
	if(x+1>n||y+1>m)return;
	if(tab[x][y]=='#'&&tab[x+1][y]=='#'&&tab[x][y+1]=='#'&&tab[x+1][y+1]=='#'){
		tab[x][y]='/';
		tab[x][y+1]=92;
		tab[x+1][y]=92;
		tab[x+1][y+1]='/';
	}
}
int main(){
	int Z;
	scanf("%d",&Z);
	FORQ(packs,1,Z){	
		scanf("%d%d",&n,&m);
		FOR(i,0,n)
			scanf("%s",tab[i]);
		FOR(i,0,n){
			FOR(j,0,m){
				if(tab[i][j]=='#')change(i,j);
			}
		}
		bool fail=false;
		FOR(i,0,n)
			FOR(j,0,m)
				if(tab[i][j]=='#')fail=true;
		printf("Case #%d:\n",packs);
		if(fail)printf("Impossible\n");
		else 
		FOR(i,0,n)
				printf("%s\n",tab[i]);
	}
}