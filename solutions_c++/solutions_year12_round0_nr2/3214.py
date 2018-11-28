#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;

int main () {

freopen("As.in", "r", stdin); //for small input
freopen("As.out", "w", stdout);

//freopen("Al.in, "r", stdin); //for large input
//freopen("Al.out, "r", stdout);

int T, N, S, p;
cin >> T;

for (int t = 1; t <= T; ++t) {
	cin >> N >> S >> p;
	int yes = 0;
	for (int i = 0; i < N; ++i){ 
		int score; cin >> score;
		//if (score == 0) continue;
		int r1 = 0;
		int rmax = 0; 
                if (S == 0) {
			r1 = p;
                      //  int asdf = yes;
                        while (r1 <= score) {
                        int k1 = r1 - 1;
                        if (3*r1 == score){
                                 ++yes;
                                 break;
                        }   
                        if (2*r1 + k1 == score) {
                                ++yes;
                                break;
                        }   
                        if (r1 + 2*k1 == score){
                                 ++yes;
                                 break;
                        }   
                        ++r1;
                        }   
                        continue;
                }   
		
			r1 = p;
			while (r1 <= score) {
			int k1 = r1 - 1;
			int k2 = r1 - 2;
			if (3*r1 == score) {
				++yes;
				break;
			}
			if (2*r1 + k1 == score) {
				++yes;
				break;
			}
			if (r1 + 2*k1 == score) {
				++yes;
				break;
			}
			if (r1 + k1+k2 == score) { 
				--S;
				++yes;
				break;
			}
			if (2*r1 + k2 == score) {
				--S;
				++yes;
				break;
			}
			if (r1 + 2*k2 == score) {
				--S;
				++yes;
				break;
			}
			++r1;
			}	
	}	
	
	
	cout << "Case #" << t << ": " << yes << endl;
}
		
return 0;
}
