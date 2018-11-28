#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

const int maxn = 100;
struct BC{
	int dep, arr;
};
BC na[maxn+10], nb[maxn+10];
int numa, numb, T;
bool g[maxn+10][maxn+10];
int nx, ny, cx[maxn+10], cy[maxn+10];
bool mk[maxn+10];

bool path( int u){
	for( int v=1; v<=ny; v++ )
		if( g[u][v] && !mk[v] ){
			mk[v]=1;
			if( cy[v]==-1 || path( cy[v] ) ){
				cx[u]=v; cy[v]=u; return 1;
			}
		}
	return 0;
}

int MaxMatch(){
	int res =0;
	memset( cx, -1, sizeof(cx) ); memset( cy, -1, sizeof(cy) );
	for( int i=1; i<=nx; i++ )
		if( cx[i]==-1 ){
			memset( mk, 0, sizeof(mk) );
			res +=path(i);
		}
	return res;
}

void read(){
	int i,j, hour, minite, t;
	char c;
	scanf("%d%d%d", &T, &numa, &numb);
	for( i=1; i<=numa; i++){
		scanf("%d%c%d", &hour, &c, &minite);
		t = hour*60+minite;
		na[i].dep = t;
		scanf("%d%c%d", &hour, &c, &minite);
		t = hour*60+minite;
		na[i].arr = t+T;
	}
	for( i=1; i<=numb; i++){
		scanf("%d%c%d", &hour, &c, &minite);
		t = hour*60+minite;
		nb[i].dep = t;
		scanf("%d%c%d", &hour, &c, &minite);
		t = hour*60+minite;
		nb[i].arr = t+T;
	}
}

void solve(){
	int i, j, res1, res2;
	if( numa==0 ){
		printf("%d %d\n", 0, numb); return ;
	}
	if( numb==0 ){
		printf("%d %d\n", numa, 0); return ;
	}
	memset( g, 0, sizeof(g) );
	// 构图1: 从B到A
	for( i=1; i<=numb; i++)
		for( j=1; j<=numa; j++ )
			if(nb[i].arr <= na[j].dep ) g[i][j]=1;
	
	nx = numb; ny= numa;
	res1 = MaxMatch();
	// 构图2
	memset( g, 0, sizeof(g) );
	for( i=1; i<=numa; i++)
		for( j=1; j<=numb; j++)
			if( na[i].arr <= nb[j].dep ) g[i][j]=1;
	nx = numa; ny=numb;
	res2 = MaxMatch();
	printf("%d %d\n", numa-res1, numb-res2);
}

int main(){
	freopen("Arena-B-large.in", "r", stdin);
	
	freopen("Arena_out.txt", "w", stdout);	
	int tc, i;
	scanf("%d", &tc);
	for( i=1; i<=tc; i++){
		printf("Case #%d: ", i);
		read();
		solve();
	}
	return 0;
}


