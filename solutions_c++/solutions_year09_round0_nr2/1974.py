//Jakub Sygnowski
#include <cstdio>
#include <map>
#define REP(I,N) for(int I=0;I<(N);I++)
using namespace std;
int tab[107][107],n,m,t,spoj;
bool visited[107][107];
int basin[107][107];
int ruchy[107][107];
int rx[]={0,-1,1,0};
int ry[]={-1,0,0,1};
bool inside(int x,int y){
	if (x<0||x>=n||y<0||y>=m)
		return false;
	return true;
}
int best,nrr,zostalo;
int dfs(int sp,int x,int y){
	visited[x][y]=true;

	if (ruchy[x][y]==-1){ 
		basin[x][y]=sp;
		return basin[x][y];
	}
	if (visited[x+rx[ruchy[x][y]]][y+ruchy[x][y]]){
		basin[x][y]=basin[x+rx[ruchy[x][y]]][y+ry[ruchy[x][y]]];
		return basin[x][y];
	}
	basin[x][y]=dfs(sp,x+rx[ruchy[x][y]],y+ry[ruchy[x][y]]);
	return basin[x][y];
}
char znak;
map<int,char> mapa;
int main(){
	scanf("%d",&t);
	REP(nr,t){
		mapa.clear();
		scanf("%d%d",&m,&n);
		REP(yy,m) REP(xx,n){
			scanf("%d",&tab[xx][yy]);
			visited[xx][yy]=false;
		}
		REP(yy,m) REP(xx,n){
			nrr=-1;
			best=tab[xx][yy];
			REP(r,4){
				if (inside(xx+rx[r],yy+ry[r])){
					if (tab[xx+rx[r]][yy+ry[r]]<best){
						best=tab[xx+rx[r]][yy+ry[r]];
						nrr=r;
					}
				}
			}
			ruchy[xx][yy]=nrr;
		}		spoj=0;
		zostalo=n*m;
		while(zostalo){
			REP(yy,m) REP(xx,n){
				if (visited[xx][yy]) continue;
				if (ruchy[xx][yy]==-1){
					visited[xx][yy]=true;
					zostalo--;
					basin[xx][yy]=spoj;
					spoj++;
				}
				else {
					if (visited[xx+rx[ruchy[xx][yy]]][yy+ry[ruchy[xx][yy]]]){
						visited[xx][yy]=true;
						basin[xx][yy]=basin[xx+rx[ruchy[xx][yy]]][yy+ry[ruchy[xx][yy]]];
						zostalo--;
					}
				}
			}
		}
		znak='a';
		REP(yy,m) REP(xx,n) {
			if (mapa.find(basin[xx][yy])==mapa.end()){
				mapa[basin[xx][yy]]=znak;
				znak++;
			}
		}
		printf("Case #%d:\n",nr+1);
		REP(yy,m){ REP(xx,n) printf("%c ",mapa[basin[xx][yy]]); printf("\n"); }
	}

}
