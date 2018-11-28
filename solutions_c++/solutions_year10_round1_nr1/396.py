#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>


 
using namespace std;
 
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
 
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
int feld[60][60];
int N,K;
bool checkhor(int vgl){
	FOR(i,0,N){
		int anz = 0;
		FOR(j,0,N){
			if(feld[i][j]==vgl){
				++anz;
				if(anz==K)return true;
			} else {
				anz = 0;
			}
		}
	}
	return false;
}
bool checkver(int vgl){
	FOR(i,0,N){
		int anz = 0;
		FOR(j,0,N){
			if(feld[j][i]==vgl){
				++anz;
				if(anz==K)return true;
			} else {
				anz = 0;
			}
		}
	}
	return false;
}
int dp[60][60];
bool checkdiag(int vgl){
	memset(dp,0,sizeof(dp));
	FOR(j,0,N)dp[0][j]=(feld[0][j]==vgl);
	FOR(i,1,N){
		dp[i][0]=(feld[i][0]==vgl);
		FOR(j,1,N){
			if(feld[i][j]==vgl){
				dp[i][j]=1+dp[i-1][j-1];
				if(dp[i][j]==K)return true;
			} else {
				dp[i][j]=0;
			}
		}
	}
	memset(dp,0,sizeof(dp));
	FOR(j,0,N)dp[0][j]=(feld[0][j]==vgl);
	FOR(i,1,N){
		FOR(j,0,N){
			if(feld[i][j]==vgl){
				dp[i][j]=1+dp[i-1][j+1];
				if(dp[i][j]==K)return true;
			} else {
				dp[i][j]=0;
			}
		}
	}
	return false;
}
int main(){
	int tc;
	cin >> tc;
	FOR(tcc,1,tc+1){
		cin >> N >> K;
		memset(feld,-1,sizeof(feld));
		string s;
		FOR(i,0,N){
			cin >> s;
			int id = 0;
			for(int j = N-1;j>=0;--j){
				if(s[j]=='R'){
					feld[i][id++]=0;
				} else if(s[j]=='B'){
					feld[i][id++]=1;
				}
			}
		}
		bool r = (checkhor(0)||checkver(0)||checkdiag(0));
		bool b = (checkhor(1)||checkver(1)||checkdiag(1));
		if(r&&b)cout << "Case #" << tcc << ": Both\n";
		else if(r)cout << "Case #" << tcc << ": Red\n";
		else if(b)cout << "Case #" << tcc << ": Blue\n";
		else cout << "Case #" << tcc << ": Neither\n";
	}
	return 0;
}
