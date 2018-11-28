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

int T, N, arr[1010];
double mycount;

int main() { 
	FILE *fin = fopen("P4.txt", "r");  
	FILE *fout = fopen("P4ans.txt", "w");
	fscanf(fin, "%d", &T);
	for (int z = 1; z <= T; z++) {
		fscanf(fin, "%d", &N);
		mycount = 0.0;
		for (int i = 1; i <= N; i++) {
			fscanf(fin, "%d", &arr[i]);
			if (arr[i] != i) mycount += 1.0;
		}
		fprintf(fout, "Case #%d: %.6f\n", z, mycount);
	}
	
	//cin.get();
	
    return 0;
}

