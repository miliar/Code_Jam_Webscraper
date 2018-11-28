#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;




int main() {
	FILE *fin = fopen("d.in", "r");
	int N;
	fscanf(fin, "%d", &N);
	FILE *fout = fopen("d.out", "w");
	for(int i = 0; i < N; i++) {
		int K;
		fscanf(fin, "%d", &K);
		char c = getc(fin);
		while(c < 'a' || c > 'z')
			c = getc(fin);
		string S = "";
		while(c >= 'a' && c <= 'z') {
			S += c;
			c = getc(fin);
		}
		
		
		vector<int> v(K);
		for(int j = 0; j < K; j++)
			v[j] = j;
		int m = 100000;
		do {
			string T(S.size(), 'a');
			for(int j = 0; j < S.size() / K; j++)
				for(int k = 0; k < K; k++)
					T[j * K + k] = S[j * K + v[k]];
			int b = 0;
			for(int j = 0; j < T.size(); j++)
				if(T[j] != T[j - 1])
					b++;
			m <?= b;
				
			
			
			
			
		} while(next_permutation(v.begin(), v.end()));
		
		
		
		fprintf(fout, "Case #%d: %d\n", i + 1, m);
			
		
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
