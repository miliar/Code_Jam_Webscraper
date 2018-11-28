#include<iostream>
#include<cstdio>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<functional>
#include<complex>
#include<iomanip>
#include<numeric>
#include<cassert>
#include<cstring>
#include<cmath>
#include<ctime>
#include<cctype>
#include<utility>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<set>
#include<list>
#include<bitset>
#include<map>

using namespace std;

template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> T gcd( T a , T b ){ return b==0?a:gcd(b,a%b);}

const double pi=acos(-1.0);
const double eps=(1e-9);
const int Dx[8]={-1,0,0,1,-1,1,1,-1};
const int Dy[8]={0,-1,1,0,1,1,-1,-1};
const int op[4] = {3,2,1,0};
const int MAXN = 105;
const int MAXM = 105 ;
const double inf = 1e50;

typedef long long LL ; 
//typedef __int64 LL ;

int Height[MAXN][MAXN];
int H,W;
int NowD[MAXN][MAXN],Flag[MAXN][MAXN];

bool Ok( int x,int y ){ return x >= 0 && x < H && y >= 0 && y < W ;}

char out[MAXN][MAXN];
void floodfill( int x, int y , char id ){
	out[x][y] = id ;
	for( int i = 0 ; i < 4 ; i ++ ){
		int nx = x + Dx[i] ;
		int ny = y + Dy[i] ;
		if( !Ok(nx,ny) || Flag[nx][ny] != Flag[x][y] || out[nx][ny] ) continue ;
		floodfill( nx, ny , id ) ;
	}
}
bool cmp( int a , int b ){
	return Height[a/W][a%W] < Height[b/W][b%W];
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int cases ; scanf("%d",&cases);
	for( int k = 1 ; k <= cases ; k ++ ){
		scanf("%d%d",&H,&W ) ; vector<int> HE;
		for( int i = 0 ; i < H ; i ++ )
			for( int j = 0 ; j < W ; j ++ ){
				scanf( "%d",&Height[i][j] );
				HE.push_back( i*W+j ) ;
			}
		sort( HE.begin() , HE.end() , cmp ) ;
		memset( NowD,-1,sizeof(NowD) ) ; 
		memset( Flag,0,sizeof(Flag) ) ; 

		int id = 1 ;
		for( int i = 0 ; i < HE.size() ; i ++ ){
			int x = HE[i]/W , y = HE[i]%W ;
			if( Flag[x][y] == 0 ) Flag[x][y] = id ++ ;
			for( int i = 0 ; i < 4 ; i ++ ){
				int nx = x + Dx[i] ;
				int ny = y + Dy[i] ;
				if( !Ok(nx,ny) || Height[nx][ny] <= Height[x][y] ) continue ;
				if( NowD[nx][ny] != -1 ){
					int d =  NowD[nx][ny] ;
					int nnx = nx + Dx[op[d]];
					int nny = ny + Dy[op[d]];
					if( Height[x][y] > Height[nnx][nny] ) continue ;
					if( Height[x][y] == Height[nnx][nny] && op[d] < op[i] ) continue ;
				}
				NowD[nx][ny] = i ;
				Flag[nx][ny] = Flag[x][y];
			}
		}
		char c = 'a' ; memset( out , 0 , sizeof(out) ) ;
		for( int i = 0 ; i < H ; i ++ )
			for( int j = 0 ; j < W ; j ++ )
				if( !out[i][j] ) 
					floodfill( i, j ,c++ ) ;
		printf("Case #%d:\n",k);
		for( int i = 0 ; i < H ; i ++ ){
			for( int j = 0 ; j < W ; j ++ ){
				if( j ) putchar(' ');
				putchar(out[i][j]);
			}
			putchar('\n');
		}
	}
}
