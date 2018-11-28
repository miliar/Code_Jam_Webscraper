#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
using namespace std;

typedef unsigned long long ULL;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	//freopen("b.in","r",stdin);
	//freopen("B-small-attempt0.out","w",stdout);
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++){
		ULL l,p,c;
		cin >> l >> p >> c;
		ULL count = 0;
		for (ULL i = l*c; i < p; i*=c, count++);
		if (count == 0){
			cout << "Case #" << test << ": " << 0 << endl;
			continue;
		}
		double con = count;
		double res = log(con)/log(2.);
		ULL i;
		for (i = 1; i < count; i*=2);
		if (i == count){
			cout << "Case #" << test << ": " << res+1 << endl;
			continue;
		}
		//double res2 = pow(2.,res);
		/*if (abs(con-res2) < 1e-17){
			cout << "Case #" << test << ": " << res+1 << endl;
			continue;
		}*/
		cout << "Case #" << test << ": " << ceil(res) << endl;
	}
	return 0;
}