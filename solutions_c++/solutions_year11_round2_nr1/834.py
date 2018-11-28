#include <cstdio> 
#include <iostream> 
#include <string> 
#include <vector> 
#include <list>
#include <algorithm> 
#include <functional> 
#include <cmath> 
#include <utility> 
 
#define MP make_pair 
#define PB push_back 
 
using namespace std; 
 
#define REP(i,n) for(i=0;(i)<(int)(n);(i)++) 
typedef long long ll; 
 
#define READ_INT(a) scanf("%d", &a); 
#define READ_LL(a) scanf("%I64d", &a); 
#define READ_STRING(a) cin >> a; 

int main ()
{
	int T, t;
	READ_INT(T);
	REP(t,T){
		int N;
		int i,j,k;
		READ_INT(N);
		vector<string> board(N);
		vector<double> WP(N);
		vector<double> OWP(N);
		vector<double> OOWP(N);
		vector<double> RET(N);
		REP(i, N)READ_STRING(board[i]);
		REP(i ,N){
			int win=0;
			int game = N;
			REP(j, N){
				if(board[i][j] == '.')game--;
				if(board[i][j] == '1')win++;
			}
			WP[i] = ((double)win)/((double)game);
		}
		REP(i, N){
			vector<double> WWP(N);
			REP(j, N){
				if(j==i){
					WWP[j]=0;
					continue;
				}
				int win=0;
				int game = N-1;
				REP(k, N){
					if(k == i)continue;
					if(board[j][k] == '.')game--;
					if(board[j][k] == '1')win++;
				}
				WWP[j] = ((double)win)/((double)game);
			}
			double sum=0;
			int game = 0;
			REP(j, N){
				if(board[i][j] != '.'){
					sum += WWP[j];
					game++;
				}
			}
			OWP[i] = sum/game;
		}
		REP(i, N){
			double sum=0;
			int game = 0;
			REP(j, N){
				if(board[i][j] != '.'){
					sum += OWP[j];
					game++;
				}
			}
			OOWP[i] = sum/game;
		}
		REP(i, N)RET[i] = 0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i];
		printf("Case #%d:\n", t+1);
		REP(i, N)printf("%.8f\n", RET[i]);
	}
}