#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>

using namespace std;


int main(void){
	int T;
	cin >> T;
	for(int q = 0; q < T; q++){
		int P, K, L, l, res= 0;
		cin >> P >> K >> L;
	//	cout << P <<  " " <<  K << " " << L << endl;	
		vector<int> freq;
		//string s;
		//cout << s << endl;
		//istringstream ss(s);
		//cout << 1 << endl;
		for(int w=0; w<L; w++){
			scanf("%d", &l);
			freq.push_back(l);
	//		cout << "got " << l;
		}	
		sort(freq.begin(), freq.end());
		reverse(freq.begin(), freq.end());
		if (L > K * P){
			cout << "Case #" << T << ": " << "Impossible" << endl;
			continue;
		}
		int depth = 0;
		for(int i=0; i<L; i++){
			if (i % K == 0){
				depth++;
			}
	//		cout << "Considering " << freq[i] << " At depth " << depth << endl; 	
			res += freq[i] * depth;
		}
		cout << "Case #" << T << ": " << res << endl;
	}
}
