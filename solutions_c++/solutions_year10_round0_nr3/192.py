#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

long long lista[1020];
long long vis[1020];
int ind[1020];
long long R, k, N;

int main(){
	int casos;
	
	cin>>casos;

	for (int c = 0; c < casos; c++) {
		cin>>R>>k>>N;
		
		for (int i = 0; i < N; i++) cin>>lista[i];
		
		int i, j, pos = 0;
		long long result=0;
		
		memset(vis, -1, sizeof vis);
		memset(ind, -1, sizeof ind);
		for (i = 0; i < R && vis[pos] == -1; i++) {
			long long cant = 0;
			for (j = 0; j < N && cant+lista[(pos+j)%N] <= k; j++) {
				cant += lista[(pos+j)%N];
			}
			vis[pos] = result;
			result += cant;
			ind[pos] = i;
			pos = (pos+j)%N;
		}
		if (i<R) {
			int cant = i-ind[pos];
			long long sum = result-vis[pos];

			result = sum*((R - ind[pos])/ cant);

			int find = (R - ind[pos]) % cant + ind[pos];
			for (i = 0; i<N; i++) if (ind[i]==find) break;
			result += vis[i];
		}
		
		printf("Case #%d: %Ld\n", c+1, result);
	}
	return 0;
}
