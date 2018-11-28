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

const int SIZE = 1000;
int x[SIZE], y[SIZE], r[SIZE];
int M;

double get(int i, int j){
	double d = hypot(x[i]-x[j], y[i]-y[j])+r[i]+r[j];
	return d/2;
}

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	freopen("D-small-attempt1.in", "rt", stdin);
	freopen("D-small-attempt1.out", "wt", stdout);
	//freopen("D-large.in", "rt", stdin);
	//freopen("D-large.out", "wt", stdout);

	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){

		scanf("%d", &M);

		assert(M <= 3);

		for(int i = 0 ; i < M ; i++)
			scanf("%d%d%d", &x[i], &y[i], &r[i]);

		double best = 1e9;

		if(M == 1){
			best = r[0];
		}else if(M == 2){
			best = r[0] >?= r[1];
		}else{

			for(int a = 0 ; a < 3 ; a++)
				for(int b = a+1 ; b < 3 ; b++){
					double r1 = get(a, b);
					double r2 = 0;
					for(int c = 0 ; c < 3 ; c++)
						if(c != a && c != b){
							r2 = r[c];
							break;
						}
					r1 >?= r2;
					best <?= r1;
				}
		}

		printf("Case #%d: %.6lf\n", t+1, best);
		cout << flush;
	}

	return 0;
}
