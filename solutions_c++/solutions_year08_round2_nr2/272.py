#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int main() {
	FILE *fin = fopen("B-small.in", "r");
	int C;
	fscanf(fin, "%d", &C);
	FILE *fout = fopen("B-small.out", "w");
	for(int i = 0; i < C; i++) {
		int A, B, P;
		fscanf(fin, "%d %d %d", &A, &B, &P);
		int l[1100];
		for(int k = A; k <= B; k++)
			l[k] = -1;
		for(int p = P; p <= B; p++) {
			
			bool o = true;
			for(int k = 2; k * k <= p; k++)
				if(p % k == 0)
					o = false;
			if(o) {
				//cout << p  << " " << i << endl;
				int t = -1;
				for(int k = 1; k * p <= B; k++)
					if(k * p >= A) {
						if(t == -1) {
							t = k * p;
							while(l[t] != -1)
								t = l[t];
						}
						else {
							//cout << k * p << endl;
							int u = k * p;
							while(l[u] != -1) {
								//cout << l[u] << endl;
								u = l[u];
							}
							if(u != t)
								l[u] = t;
						}
					}
			}
		}
		
		bool q[1100];
		for(int j = A; j <= B; j++)
			q[j] = false;
		int b = 0;
		for(int j = A; j <= B; j++) {
			int u = j;
			while(l[u] != -1)
				u = l[u];
			if(!q[u]) {
				b++;
				q[u] = true;
			}
		}
		fprintf(fout, "Case #%d: %d\n", i + 1, b);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
