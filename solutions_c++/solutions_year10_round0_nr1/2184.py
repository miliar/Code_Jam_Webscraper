#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <map>
#include <queue>
#include <set>
#include <vector>


using namespace std;


int main(int argc, char* argv[]){
	int T;
	FILE *fpt,*fout;
	int one = 1;
	fpt = fopen("A-large.in","r");
	fout = fopen("out","w");
	fscanf(fpt, "%d", &T);
	for(int i=0; i<T; i++){
		int N,K;
		int tester, r;
		fscanf(fpt, "%d %d", &N, &K);
		tester = 1;
		for(int j=1; j<N; j++){
			tester = tester + (one << j);
		}
		printf("%d %x %o\n", tester, tester, tester);
		r = tester & K;
		if(r == tester){
			fprintf(fout, "Case #%d: ON\n", i+1);
		}else{
			fprintf(fout, "Case #%d: OFF\n", i+1);
		}
	}

	return 0;
}

