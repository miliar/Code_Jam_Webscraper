#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>

#define REP(i,n) for(typeof(n) _n=n, i=0;i<_n;++i)
#define FOREACH(i,x) for(typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define ALL(x) (x).begin(),(x).end()
#define INFTY 1000000

using namespace std;

long long solveCase(){
	long long n, A, B, C, D, x0, y0, M;
	cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
	vector<vector<long long> > cnt(3,vector<long long>(3,0));
	
	long long x = x0;
	long long y = y0;
	cnt[x % 3][y % 3]++;
	REP(i,n-1){
		x = (A*x+B) % M;
		y = (C*y+D) % M;
		cnt[x % 3][y % 3]++;	
	}
/*
	REP(i,3){
		REP(j,3) cout << cnt[i][j] << " ";
		cout << endl;
	}
*/
	long long total = 0;	

	for(int k1 = 0; k1 < 9; k1++)
	for(int k2 = k1; k2 < 9; k2++)
	for(int k3 = k2; k3 < 9; k3++){
		int i1 = k1/3; int j1 = k1%3;
		int i2 = k2/3; int j2 = k2%3;
		int i3 = k3/3; int j3 = k3%3;
		if ( ( (i1+i2+i3)%3 == 0) && ( (j1+j2+j3)%3 == 0)){
			if ((k1 == k2) && (k2 == k3)){
				long long c = cnt[i1][j1];
				total += c*(c-1)*(c-2)/6;
			} else if ( (k1 == k2) && (k2 != k3)){
				long long c1 = cnt[i1][j1];
				long long c2 = cnt[i3][j3];
				total += c1*(c1-1)*c2/2;
			} else if ( (k1 != k2) && (k2 == k3)){
				long long c1 = cnt[i1][j1];
				long long c2 = cnt[i3][j3];
				total += c1*c2*(c2-1)/2;
			} else  // all different
				total += cnt[i1][j1] * cnt[i2][j2] * cnt[i3][j3];
				//cout << total << endl;
		}		
	}
	return total;
}	

int main(){
	int cases;
	cin >> cases;
	REP(i,cases){
		cout << "Case #" << i+1 << ": " << solveCase() << endl;
	}		
	return 0;
}
