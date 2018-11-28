#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <math.h>
#include <algorithm>
#define fori(n) for (int i = 0; i < n; i++)
#define forj(n) for (int j = 0; j < n; j++)
#define fork(n) for (int k = 0; k < n; k++)

using namespace std;

int main() {
	ifstream in("next.in");
	FILE* fout = fopen("next.out","w");

	int T;
	in >> T;
	for (int t = 0; t < T; t++) {
		string N;
		in >> N;

		if (!next_permutation(N.begin(),N.end())) {
			sort(N.begin(),N.end());
			
			if (N[0] == '0') {
				int p = 0;
				while(N[p] == '0') p++;
				N[0] = N[p];
				N[p] = '0';
			}

			N.insert(N.begin()+1,'0');
		}

		printf("Case #%d: %s\n",t+1,N.c_str());
		fprintf(fout,"Case #%d: %s\n",t+1,N.c_str());
	}
	return 0;
}
