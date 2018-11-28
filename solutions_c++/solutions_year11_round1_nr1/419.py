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

int T;
int N, PD, PG;
long long LN;


int main() { 
	FILE *fin = fopen("P1-1.txt", "r");  
	FILE *fout = fopen("P1-1ans.txt", "w");
	//FILE *fin = fopen("P1-2.txt", "r");  
	//FILE *fout = fopen("P1-2ans.txt", "w");
	
	fscanf(fin, "%d", &T);
	
	for (int z = 1; z <= T; z++) {
		fscanf(fin, "%lld %d %d", &LN, &PD, &PG);
		LN = min(LN, 100*1LL);
		N = (int)LN;
		//printf("Case #%d: ", z);
		fprintf(fout, "Case #%d: ", z);
		if (PD != 0 && PG == 0) {
			//printf("Broken\n");
			fprintf(fout, "Broken\n");
			continue;
		} else if (PD != 100 && PG == 100) {
			//printf("Broken\n");
			fprintf(fout, "Broken\n");
			continue;
		}
		int yes = 0;
		for (int i = 1; i <= N; i++) {
			if ((i*PD) % 100 == 0) yes = 1;
		}
		if (yes) {
			//printf("Possible\n");
			fprintf(fout, "Possible\n");
		} else {
			//printf("Broken\n");
			fprintf(fout, "Broken\n");
		}
	}
	
	
	
	
	//cin.get();
	
    return 0;
}

