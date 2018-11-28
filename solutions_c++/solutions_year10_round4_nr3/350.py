#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <sstream>
using namespace std;

#define sz(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define ll long long
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define pb push_back
#define pii pair<int,int>
#define inf (1<<25)
#define infL 10000000000000000LL
#define F first
#define S second
#define all(x) x.begin() , x.end()

#define N 205

int tab[N][N][2];
int n;

int tudoMorto(int at) {
	FOR(i,N) FOR(j,N) if(tab[i][j][at]) return 0;
	return 1;
}

int viz(int x, int y, int at){
	if(x < 0 || y < 0) return 0;
	return tab[x][y][at];
}

int calc() {
	int at = 0, cnt = 0;;
	while(!tudoMorto(at)) {
		cnt++;
		FOR(i,N) FOR(j,N) {
			if(tab[i][j][at] == 1){
				if(!viz(i-1,j,at) && !viz(i,j-1,at))
					tab[i][j][1-at] = 0;
				else
					tab[i][j][1-at] = 1;
			}
			else if(tab[i][j][at] == 0){
				if(viz(i-1,j,at) && viz(i,j-1,at))
					tab[i][j][1-at] = 1;
				else
					tab[i][j][1-at] = 0;
			}
		}
		at = 1-at;
	}
	return cnt;
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(t,T) {
		printf("Case #%d: " , t+1);
		cin >> n;
		memset(tab,0,sizeof(tab));
		FOR(i,n) {
			int xini,yini, xfim,yfim;
			cin >> xini >> yini >> xfim >> yfim;	
			for(int i = xini; i  <= xfim; i++)
				for(int j = yini; j<= yfim; j++)
					tab[i][j][0] = 1;
		}
		cout << calc() << endl;
	}

    return 0;
}

