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

ifstream fin("A_Free Cell.in");
ofstream fout("A_Free Cell.out");

#define cin fin
#define cout fout

int main(){
	int T, test = 0;
	int n, p1, p2;
	for(cin >> T; T--; ){
		cin >> n >> p1 >> p2;
		bool fl = false;
		if(n < 100){
			for(int i = 1; i <= n; i++){
				if((i * p1) % 100 == 0){
					fl = true;
				}
			}
		}
		else fl = true;
		if(p1 != 100 && p2 == 100)
			fl = false;
		if(p1 != 0 && p2 == 0)
			fl = false;
		cout << "Case #" << ++test << ": " << (fl ? "Possible" : "Broken") << endl;
	}
	return 0;
}