#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <math.h>
#include <map>
#include <set> 
#include <queue>
#define  rep(i,a,b) for ( int i = a; i<=b; i++ )
const double EPS = 1E-8; 
const double PI  = 3.14159265; 
const int dx[4]={0,1,0,-1};
const int dy[4]={1,0,-1,0};

using namespace std; 

typedef  vector<int> VI; 
typedef  vector<VI>  VV; 
typedef  string      SS; 
typedef  vector<SS> VS; 
typedef  long long   LL;
typedef  map<int,int>MII;
typedef  priority_queue<int> maxpq; 
typedef  priority_queue<int,VI, greater<int>> minpq;

int T; 
int R, C; 
vector<string> A, B; 
bool ok ;

void main(){
	freopen("A-large (3).in","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> T; 
	rep(test_number,1,T){
		cin >> R >> C;
		A.clear(); B.clear(); 
		A.resize(R+1); B.resize(R+1); 
		rep(i,0,R-1){cin >> A[i]; }
		ok = true; 
		rep(i,0,R-2){
			rep(j,0,C-2){
				if (A[i][j]=='#') {
					A[i][j]='/'; 
					if (A[i][j+1]=='#' && A[i+1][j]=='#' && A[i+1][j+1]=='#') {
						A[i][j+1]=92 ;
						A[i+1][j]=92 ;
						A[i+1][j+1]='/'; 
					}
					else {
						ok = false; 
						break; 
					}
				}
			}
			if (!ok) break; 
		}

		rep(i,0,R-1) {
			rep(j,0,C-1){
				if (A[i][j]=='#') ok = false; 
			} 
		}
		printf("Case #%d:\n",test_number); 
		if (!ok) printf("Impossible\n"); 
		else {
			rep(i,0,R-1){
				cout << A[i]<< endl; 
			}
		}
	}
}