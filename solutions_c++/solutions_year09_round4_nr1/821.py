//Jakub Sygnowski
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <sstream>
using namespace std;

#define REP(I,N) for(int I=0;I<(N);++I)
#define FOR(I,A,B) for(int I=(A);I<=(B);++I)
#define FORD(I,A,B) for(int I=(A);I>=(B);--I)
#define VAR(A,B) __typeof(B) A=B
#define FORE(I,X) for(VAR(I,(X).begin());I!=(X).end();++I)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define INF 1000000007
#define sq(A) ((A)*(A))
#define SZ(X) ((int)(X).size())
typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

int mat[50][50];
int t,n,res;
bool wporz(int row,int od){
	FOR(i,od,n-1){
		if (mat[i][row]) return false;
	}
	return true;
}
char zn;
int main(){
	scanf("%d",&t);
	REP(nr,t){
		scanf("%d",&n);
		REP(y,n){
			REP(x,n){
				scanf(" %c",&zn);
				mat[x][y]=zn-'0';
			}
		}
		res=0;
		REP(wier,n-1){
		//	printf("res=%d\n",res);
		//	REP(y,n) { REP(x,n) printf("%d ",mat[x][y]); printf("\n"); }
		//	printf("\n");
			if (wporz(wier,wier+1))
				continue;
			else {
				FOR(i,wier+1,n-1){
					if (wporz(i,wier+1)){
						FORD(zm,i,wier+1){
						//	printf("a");
							REP(xx,n) swap(mat[xx][zm],mat[xx][zm-1]);
							res++;
						}
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n",nr+1,res);
	}
}
