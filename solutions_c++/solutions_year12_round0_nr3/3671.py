/*
 * main.cpp
 *
 *  Created on: 2011-04-28
 *      Author: ronanrmo
 */
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string.h>
#include <set>
using namespace std;

#define F0(i,n) for(int i=0; i<n; i++)
#define F1(i,n) for(int i=1; i<n; i++)
#define clearfloat(array, size) memset(array, 0, sizeof(float)*size);
#define clearint(array, size) memset(array, 0, sizeof(int)*size);



int hasRecycle(int A, int m){

	char *mc = new char[10000000];
	char *tc = new char[10000000];
	std::set<int> recycles;

	int rec = 0;
	sprintf(mc, "%d", m);


	int len = strlen(mc);

	for(int i=1; i<len; i++){
		for(int j=0; j<len; j++){
			int idx = j + i - ((j+i>=len)?len:0);
			tc[j] = mc[idx];
		}
		tc[len+1] = 0;
		int n = atoi(tc);
		if(n>=A && n < m){
//			printf("%s %s\n", tc, tc);
			rec++;
			recycles.insert(n);
		}
	}
	return recycles.size();
}



int main(int argc, char **argv)
{

	FILE *file_in, *file_out;


	// OPENING FILES ////////////////////////////////////////////////////////////////////

	// checking if first argument is not provided than redirect to stdin
	if(argc == 1){
		file_in = stdin;
	}
	// otherwise open file to write
	else{
		file_in   = fopen(argv[1], "r");
	}

	// checking if second argument is not provided than redirect to stdout
	if(argc < 3){
		file_out = stdout;
	}
	// otherwise open file to write
	else{
		file_out = fopen(argv[2], "w");
	}
	// END OPENING FILES ////////////////////////////////////////////////////////////////

	int T;
	fscanf(file_in, "%d", &T);

	F0(t,T){
		int A,B;
		fscanf(file_in, "%d", &A);
		fscanf(file_in, "%d", &B);

		int ans = 0;
		for(int m = A+1; m<= B; m++){
			ans += hasRecycle(A, m);
		}


		fprintf(file_out, "Case #%d: %d\n", t+1, ans);
	}

	return 0;
}
