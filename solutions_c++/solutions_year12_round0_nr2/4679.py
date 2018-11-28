#include <utility>
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <vector>
using namespace std;

int N, T, S, P;

vector<int> vect;

int main(){
	int t, sum;
	scanf("%d", &N);
	for(int re = 1;re <= N;re++){
		scanf("%d %d %d", &T, &S, &P);
		sum = 0;
		vect.clear();
		for(int i = 0;i < T;i++){
			scanf("%d", &t);
			vect.push_back(t);
		}
		for(unsigned i = 0;i < vect.size();i++){
			t = vect[i];
			if(t >= P * 3){
				sum++;
			}
			else if(P >= 1 && t >= P * 3 - 2){
				sum++;
			}
			else if(P >= 2 && (t == P * 3 - 3 || t == P * 3 - 4) && S > 0){
				sum++;
				S--;
			}
		}
		printf("Case #%d: %d\n", re, sum);
	}
	return 0;
}

