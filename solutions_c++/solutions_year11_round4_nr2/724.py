#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<deque>
#include<string>
#include<cctype>
#include<cmath>
#include<sstream>
#include<numeric>
#include<complex>
#include<queue>
using namespace std;

int R, C, D;
string arr[510];
const double EPS = 1e-9;

bool check(int a, int b, int d){

	int aa = a+d-1;
	int bb = b+d-1;
	double mx = (a+aa)/2., my = (b+bb)/2.;

	double sx = 0, sy = 0;
	for(int i = a ; i <= aa ; i++){
		for(int j = b ; j <= bb ; j++){
			if(i == a && j == b)continue;
			if(i == a && j == bb)continue;
			if(i == aa && j == b)continue;
			if(i == aa && j == bb)continue;
			double mass =(D+(arr[i][j]-'0'));
			sx += (i-mx)*mass;
			sy += (j-my)*mass;
		}
	}
	if(fabs(sx) <= EPS && fabs(sy) <= EPS)
		return true;
	return false;
}

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
//	freopen("B-small-attempt0.in", "rt", stdin);
//	freopen("B-small-attempt0.out", "wt", stdout);
	freopen("B-small-attempt1.in", "rt", stdin);
	freopen("B-small-attempt1.out", "wt", stdout);
	//freopen("B-large.in", "rt", stdin);
	//freopen("B-large.out", "wt", stdout);

	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		//cerr << "Solving testcase " << t+1 << endl;

		cin >> R >> C >> D;
		for(int i = 0 ; i < R ; i++)
			cin >> arr[i];

		int M = min(R,C);
		while(M>=3){
			for(int i = 0 ; i < R ; i++){
				if(i+M > R)break;
				for(int j = 0 ; j < C ; j++){
					if(j+M > C)break;
					if(check(i, j, M))
						goto done;
				}
			}
			M--;
		}
done:
		cout << "Case #" << t+1 << ": ";
		if(M >= 3)
			cout << M << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}
