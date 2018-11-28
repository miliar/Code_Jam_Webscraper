#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <fstream>
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;


int main(){
	ifstream ifs("data.txt");
	int cases;ifs >> cases;
	for(int i=0;i<cases;++i){
		ll N,S,p;
		ifs>>N; ifs >> S; ifs>>p;
		ll result=0;
		for(int j=0;j<N;++j){
			ll score;
			ifs >> score;
			if(3*p-2<=score){
				++result;
			}else if(S!=0&&p>1&&3*p-4<=score){
				++result;--S;
			}

		}
		
		cout<<"Case #"<<i+1<<": "<<result<<endl;
	};
	

};

