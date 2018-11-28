#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXX=500;

int X,Y;
int masse[MAXX][MAXX];
char ligne[MAXX+5];
long long sommeAvant[3][MAXX+1][MAXX+1];

int mul(int id,int x,int y){
	return id==0 ? x : y;
}

bool centre(int id,int x,int y,int l){
	long long somme=sommeAvant[id][x+l][y+l]+sommeAvant[id][x][y]-sommeAvant[id][x+l][y]-sommeAvant[id][x][y+l]
		-mul(id,x,y)*masse[x][y]-mul(id,x,y+l-1)*masse[x][y+l-1]-mul(id,x+l-1,y)*masse[x+l-1][y]-mul(id,x+l-1,y+l-1)*masse[x+l-1][y+l-1];
	int mil=mul(id,x,y)*2+(l-1);
	long long but=sommeAvant[2][x+l][y+l]+sommeAvant[2][x][y]-sommeAvant[2][x+l][y]-sommeAvant[2][x][y+l]
		-masse[x][y]-masse[x][y+l-1]-masse[x+l-1][y]-masse[x+l-1][y+l-1];
//	printf("%lld %d %lld %lld\n",somme,mil,but,sommeAvant[2][x+l][y+l]);
	return somme*2==mil*but;
}

void resoud(){
	int D;
	scanf("%d%d%d",&Y,&X,&D);
	for (int y=0;y<Y;y++){
		scanf("%s",ligne);
		for (int x=0;x<X;x++)
			masse[x][y]=D+ligne[x]-'0';
	}
	for (int x=0;x<X;x++)
		for (int y=0;y<Y;y++){
			sommeAvant[0][x+1][y+1]=sommeAvant[0][x][y+1]+sommeAvant[0][x+1][y]-sommeAvant[0][x][y]+x*masse[x][y];
			sommeAvant[1][x+1][y+1]=sommeAvant[1][x][y+1]+sommeAvant[1][x+1][y]-sommeAvant[1][x][y]+y*masse[x][y];
			sommeAvant[2][x+1][y+1]=sommeAvant[2][x][y+1]+sommeAvant[2][x+1][y]-sommeAvant[2][x][y]+  masse[x][y];
		}
//	centre(0,0,0,10);
	for (int milieu=X;milieu>=3;milieu--){
		for (int x=0;x<X-milieu+1;x++)
			for (int y=0;y<Y-milieu+1;y++){
//				printf("%d %d %d\n",x,y,milieu);
				if (centre(0,x,y,milieu) && centre(1,x,y,milieu)){
					printf("%d",milieu);
					return ;
				}
			}
	}
	printf("IMPOSSIBLE");
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++){
		printf("Case #%d: ",i+1);
		resoud();
		puts("");
	}
	return 0;
}
