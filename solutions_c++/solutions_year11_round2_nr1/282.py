#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional> 
#include <numeric>
using namespace std;
#define foreach(i,v) for(__typeof((v).end()) i=(v).begin();i!=(v).end();++i)
#define rforeach(i,v) for(__typeof((v).rend()) i=(v).rbegin();i!=(v).rend();++i)
#define FOR(i,b,e) for(int i=(b);i<(e);++i)
#define FORE(i,b,e) for(int i=(b);i<=(e);++i)
#define debug(x) cerr << #x << " = " << (x) << "\n"
typedef long long LL;

int main(){
	int t;
	cin >> t;
	FORE(z,1,t){
		int n;
		cin >> n;
		string a[n];
		FOR(i,0,n)
			cin >> a[i];
		double wp[n], owp[n], oowp[n];
		int game[n], win[n];
		FOR(i,0,n){
			game[i]=win[i]=0;
			FOR(r,0,n){
				if (a[i][r]!='.') ++game[i];
				if (a[i][r]=='1') ++win[i];
			}
			wp[i] = (double) win[i]/game[i];
		}
		FOR(i,0,n){
			double s=0;
			FOR(r,0,n)
				if (a[i][r]!='.'){
					int g = game[r]-1;
					int w = win[r]+(a[r][i]=='1'?-1:0);
					s += (double) w/g; 
				}
			owp[i] = s/game[i];
		}
		FOR(i,0,n){
			double s=0;
			FOR(r,0,n)
				if (a[i][r]!='.')
					s += owp[r];
			oowp[i] = s/game[i];
		}
			
		printf("Case #%d:\n",z);
		FOR(i,0,n)
			printf("%.12f\n",.25*wp[i]+.5*owp[i]+.25*oowp[i]);
	}
	return 0;
}
