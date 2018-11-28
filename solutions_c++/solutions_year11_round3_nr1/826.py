/*
 * main.cpp
 *
 *  Created on: 2011-04-28
 *      Author: ronanrmo
 */
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define F0(i,n) for(int i=0; i<n; i++)
#define F1(i,n) for(int i=1; i<n; i++)
#define clearfloat(array, size) memset(array, 0, sizeof(float)*size);
#define clearint(array, size) memset(array, 0, sizeof(int)*size);

bool findnextBlue(char *in[], int R, int C, int &i, int &j)
{
	for(; i<R; i++){
		for(;j<C; j++){
			if(in[i][j] == '#')
				return true;
		}
	}
	return false;
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
		int R;
		int C;
		fscanf(file_in, "%d %d", &R, &C);

		char **floor = new char*[R];//[R][C+1];
		F0(r,R) floor[r] = new char[C+1];


		F0(r,R){
			fscanf(file_in, "%s", floor[r]);
		}

//		F0(r,R){
//			fprintf(file_out, "%s %d %d\n", floor[r], R, C);
//		}

//		break;

		bool possible = true;

//		F0(r,R){
		for(int r=0; r<R && possible; r++){

			for(int c=0; c<C && possible; c++){
				int rb = r;
				int cb = c;
				if(findnextBlue(floor, R, C, rb, cb)){
					if(rb<R-1 && cb<C-1 && floor[rb+1][cb] == '#'  && floor[rb+1][cb+1] == '#'  && floor[rb][cb+1] == '#'){
						floor[rb][cb] = '/';
						floor[rb+1][cb] = '\\';
						floor[rb+1][cb+1] = '/';
						floor[rb][cb+1] = '\\';
					}else{
						possible = false;
						break;
					}
				}
				else{
					break;
				}
			}
		}

		if(possible){
			fprintf(file_out, "Case #%d:\n", t+1);
				F0(r,R){
					fprintf(file_out, "%s\n", floor[r]);
				}
		}
		else{
			fprintf(file_out, "Case #%d:\n%s\n", t+1, "Impossible");
		}

		F0(r,R)if(floor[r]!=NULL)delete[] floor[r];
		delete[] floor;


	}


//	fprintf(file_out, "num %d\n", num);



	return 0;
}
