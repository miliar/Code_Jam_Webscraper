#include <iostream>
#include <cstdlib>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define abs(x) ((x) > 0 ? (x) : -1*(x))
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))


int main()
{
	int T;
	
	cin >> T;
	for(int i = 1; i <= T; i++) {
		int alcanzan = 0;
		int ensurp = 0;
		int N, S, p, ti;
//		vector<int> t;
		cin >> N;
		cin >> S;
		cin >> p;
		
		for (int j = 0; j < N; j++) {
			cin >> ti;
//			t.push_back(ti);
			
			int s = ti % 3;
			int valor = floor(ti/3) + (s-- > 0);
			
			if (valor >= p) {
				alcanzan++;
			} else {
				if (ti > 1 && (valor + 1) >= p) {
					ensurp++;
				}
			}
		}
		
		alcanzan += min(ensurp, S);
		
		cout << "Case #" << i << ": " << alcanzan << endl;
	}
	
	return 0;
}
