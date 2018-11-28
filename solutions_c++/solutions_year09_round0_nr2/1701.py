#include<cstdio>
#define REP(i,n) for(int i=0;i<n;i++)
#define NIL (-1)
#define OO (1<<30)
const bool dbg = 0;

const int MAXN = 110;
int map[MAXN][MAXN];
int dra[MAXN][MAXN];
int h,w;
int d;
int dirH[] = {-1,0,0,1};
int dirW[]= {0,-1,1,0};

void read(){
	d = 0;
	scanf("%d%d",&h,&w);
	REP(i,h)
		REP(j,w)
			scanf("%d",&map[i+1][j+1]);
	REP(i,h+2)
		map[i][0] = map[i][w+1] = OO;
	REP(i,w+2)
		map[0][i] = map[h+1][i] = OO;
	REP(i,h+2)
		REP(j,w+2)
			dra[i][j] = NIL;
}

int dfs(int hh,int ww){
	if(dbg)printf("dfs(%d,%d)[%d|%c]\n",hh,ww,map[hh][ww],'a'+dra[hh][ww]);
	if(dra[hh][ww] != NIL)return dra[hh][ww];
	int best = NIL;
	REP(i,4){
		int nH = hh+dirH[i], nW = ww+dirW[i];
		if(map[nH][nW] < map[hh][ww] && (best == NIL || map[nH][nW] < map[hh + dirH[best]][ww + dirW[best]]))
			best = i;
	}
	if(dbg)printf("dfs(%d,%d):best:%d\n",hh,ww,best);
	if(best == NIL) dra[hh][ww] = d++;
	else dra[hh][ww] = dfs(hh+dirH[best],ww+dirW[best]);
	if(dbg)printf("dfs(%d,%d):[%c]\n",hh,ww,dra[hh][ww]+'a');
	return dra[hh][ww];
}
void compute(int cas){
	REP(i,h)
		REP(j,w)
			if(dra[i+1][j+1] == NIL)
				dfs(i+1,j+1);
	printf("Case #%d:\n",cas+1);
	REP(i,h){
		REP(j,w)
			printf("%c ",dra[i+1][j+1]+'a');
		printf("\n");
	}
}


int main(){
	int t;
	scanf("%d",&t);
	REP(i,t){
		read();
		compute(i);
	}
	return 0;
}

