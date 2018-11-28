#include <iostream>
using namespace std;
typedef long long int lli;
#define ZER(X) memset(X,0,sizeof(X));

typedef long double ld;

int main(){
	int Cases;
	cin >> Cases;
	for(int Case=1; Case <= Cases; ++Case){
		int C, D;
		cin >> C >> D;
		//cerr << C << " " << D << endl;
		ld position=-1000000;
		ld time = 0;
		for (int i = 0; i < C; ++ i){
			int P, V;
			cin >> P >> V;
			//cerr << P << " PV " << V << endl;
			while (V--){
				ld leftmost = max(position + D, P-time);
				ld rigthmost = P+time;
				//cerr << "leftmost " << leftmost << " " << rigthmost << endl;
				if(leftmost < rigthmost)
					position = leftmost;
				else{
					time += (leftmost - rigthmost)/2;
					position = P+time;
				}
			}
		}
		cout << "Case #" << Case << ": " << time <<endl;
	}
	return 0;
}