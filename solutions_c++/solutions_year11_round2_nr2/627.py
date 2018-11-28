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

#define big long long
const double EPS = 1e-9;

vector<big> vec;
int C, D;

bool get(double x){

	double lastPos = vec[0]-x;
	for(int i = 1 ; i < (int)vec.size() ; i++){
		double least = lastPos+D;
		if(least < vec[i])
			lastPos = max(least, vec[i]-x);
		else{
			if(least-(vec[i]+x)-EPS > 0)
				return false;
			lastPos = least;
		}
	}
	return true;
}

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B-small-attempt0.out", "wt", stdout);
	//freopen("B-large.in", "rt", stdin);
	//freopen("B-large.out", "wt", stdout);

	int tt; scanf("%d", &tt);
	for(int t = 0 ; t < tt ; t++){
		//cerr << "Solving testcase " << t+1 << endl;

		vec.clear();
		scanf("%d%d", &C, &D);
		for(int i = 0 ; i < C ; i++){
			int p, v; scanf("%d%d", &p, &v);
			for(int j = 0 ; j < v ; j++)
				vec.push_back(p);
		}

		double low = 0, high = 1000000000000ll;
		while(fabs(low-high) >= 1e-12){
			double mid = (low+high)/2;
			if(get(mid))
				high = mid;
			else
				low = mid;
		}

		printf("Case #%d: %.9lf\n", t+1, low);
	}

	return 0;
}
