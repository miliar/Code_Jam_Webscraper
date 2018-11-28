//Using open source library The GNU Multiple Precision Arithmetic Library
//http://gmplib.org/ 

#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <numeric>
#include <gmp.h> 
#include <stdio.h>
#include <gmpxx.h>

using namespace std;

typedef complex<double> pto;
typedef mpz_class bigInt;

typedef long long LL;
typedef pair<int,int> PII;
typedef pair<int,PII> PIPII;
typedef pair<PII,PII> PIIPII;
typedef pair<LL,LL> PLL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
typedef vector<int> VI;
typedef vector<VI> VII;
typedef vector<bool> VB;
typedef vector<string> VS;

#define REP(i,n) FOR(i,0,n)
#define FOR(i,s,n) for( LL ___n=LL(n), i=LL(s) ; i<___n ; ++i )
#define REPD(i,n) FORD(i,0,n)
#define FORD(i,s,n) for( LL ___s=LL(s), i=LL(n)-1 ; i>=___s ; --i )
#define FOREACH(i,c) for( typeof((c).begin()) i=(c).begin() ; i!=(c).end() ; ++i )
#define ALL(c) (c).begin(), (c).end()
#define SZ(a) ((int)(a).size())
#define PB push_back
#define gbic get_mpz_t

const int mx[] = {-1,0,1,0, -1, -1, 1, 1};
const int my[] = {0,-1,0,1, -1, 1, -1, 1};
const int inf=0x7fffffff;

int main() {
	
	int T;
	cin >> T;
	FOR(t, 1, T + 1){
		LL N, K;
		cin>>N>>K;
		vector<vector<int> >M(N, vector<int>(N));
		REP(i, N){
			REP(j, N){
				char c;
				cin >> c;
				M[i][j] = c;
			}
		}
		REP(i, N){
			REPD(j, N){
				int color;
				if(M[i][j] != '.'){
					color = M[i][j];
					int k = j + 1;
					while(k < N){
						if(M[i][k] == '.'){
							M[i][k - 1] = '.';
							M[i][k] = color;
							
						}
						k++;
					}
				}
			}
		}
		bool answerB = false;
		bool answerR = false;
		REP(i, N){
			REP(j, N){
				int color;
				if(M[i][j] != '.'){
					color = M[i][j];
					if(color == 'B' && answerB == false){
						REP(m, 8){
							int x, y;
							x = i;
							y = j;
							bool answer = true;
							REP(k, K -1){
								x +=mx[m];
								y +=my[m];
								if(x < 0 || x >= N || y < 0 || y >= N){
									answer = false;
									break;
								}
								else if(M[x][y] != 'B'){
									answer = false;
									break;
								}
							}
							if(answer == true){
								answerB = true;
								break;
							}
						}
					}
					else if(color == 'R' && answerR == false){
						REP(m, 8){
							int x, y;
							x = i;
							y = j;
							bool answer = true;
							REP(k, K -1){
								x +=mx[m];
								y +=my[m];
								if(x < 0 || x >= N || y < 0 || y >= N){
									answer = false;
									break;
								}
								else if(M[x][y] != 'R'){
									answer = false;
									break;
								}
							}
							if(answer == true){
								answerR = true;
								break;
							}
						}
					}
				}
			}
		}
		if(answerB & answerR){
			cout << "Case #" << t << ": " << "Both" << endl;
		}
		else if(answerB){
			cout << "Case #" << t << ": " << "Blue" << endl;
		}
		else if(answerR){
			cout << "Case #" << t << ": " << "Red" << endl;
		}
		else{
			cout << "Case #" << t << ": " << "Neither" << endl;
		}
	}

					
							
							
							
							
							
						
				
	
	
	
    
    return 0;
}
