								/* in the name of Allah */
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <cstdio>
#include <cmath>
#include <map>

using namespace std;

ifstream fin("B_Revenge of the Hot Dogs.in");
ofstream fout("B_Revenge of the Hot Dogs.out");

#define cin fin
#define cout fout
#define int64 long long

int c, n;
int64 d, num[1000010];

bool can(int64 t){
	int64 bef = num[0] - t;
	for(int i = 1; i < n; i++){
		int64 nt = max(bef + d, num[i] - t);
		int64 dif = abs(nt - num[i]);
		if(dif > t)
			return false;
		bef = nt;
	}
	return true;
}

int main(){
	int T, test = 0;
	for(cin >> T; T--; ){
		n = 0;
		cin >> c >> d;
		d *= 2;
		int p, x;
		for(int i = 0; i < c; i++){
			cin >> p >> x;
			for(int j = n; j < n + x; j++)
				num[j] = 2 * p;
			n += x;
		}
		int64 l = 0, r = 2000000000000LL;
		while(l < r){
			int64 t = (l + r) / 2;
			if(can(t))
				r = t;
			else l = t + 1;
		}
		//cout << l << endl;
		cout << "Case #" << ++test << ": " << l / 2 << (l % 2 ? ".5" : ".0") << endl;
		cerr << T << endl;
	}
	return 0;
}