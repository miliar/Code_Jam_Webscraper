#include <iostream> 
#include <vector> 
#include <cstdio> 
#include <cstring> 
#include <algorithm> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <string> 
#include <sstream> 
#include <ctime> 
#include <cmath> 

using namespace std; 

int T, N, arr[1010], csum, ansxor;

int main() { 
	FILE *fin = fopen("P3.txt", "r");
	FILE *fout = fopen("P3ans.txt", "w");
	fscanf(fin, "%d", &T);
	for (int z = 1; z <= T; z++) {
		csum = ansxor = 0;
		fscanf(fin, "%d", &N);
		for (int i = 1; i <= N; i++) {
			fscanf(fin, "%d", &arr[i]);
			csum += arr[i];
			ansxor ^= arr[i];
		}
		if (ansxor != 0) {
			fprintf(fout, "Case #%d: NO\n", z);
		}
		else {
			sort(arr+1, arr+1+N);
			fprintf(fout, "Case #%d: %d\n", z, csum-arr[1]);
		}
	}
	
	//cin.get();
	
    return 0;
}

