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

ifstream fin("C_Expensive Dinner.in");
ofstream fout("C_Expensive Dinner.out");

#define cin fin
#define cout fout
#define int64 long long
#define Max 1000000

bool npr[1000010];
vector <int64> p;

void find_prime(){
	for(int i = 2; i < Max; i++){
		if(!npr[i]){
			p.push_back(i);
			for(int j = 2 * i; j < Max; j += i)
				npr[j] = true;
		}
	}
}

int main(){
	find_prime();
	int64 T, test = 0, n;
	for(cin >> T; T--; ){
		cerr << T << endl;
		cin >> n;
		if(n == 1){
			cout << "Case #" << ++test << ": " << 0 << endl;
			continue;
		}
		int64 res = 1;
		for(int i = 0; i < p.size() && p[i] <= n; i++){
			int64 x = p[i];
			while(x * p[i] <= n){
				x *= p[i];
				res++;
			}
		}
		cout << "Case #" << ++test << ": " << res << endl;
	}
	return 0;
}