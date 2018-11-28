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
		int N; fscanf(file_in, "%d", &N);
		int S; fscanf(file_in, "%d", &S);
		int P; fscanf(file_in, "%d", &P);

		vector<int> scores;
		scores.reserve(N);

		F0(n,N){
			int ssum; fscanf(file_in, "%d", &ssum);
			scores.push_back(ssum);
		}

		sort(scores.begin(), scores.end());


		int ans = 0;
		int size = scores.size()-1;

		F0(n,N){
			int q = scores[size-n]/3;
			int r = scores[size-n]%3;
//			printf("%d %d %d\n", scores[size-n], q, P);

			if((q >= P) ||
					((q + 1 >= P) && (((3*q + 1) == scores[size-n]) || (3*q + 2) == scores[size-n]))){
				ans++;
			}
			else{
				if(S>0){
					if((q + 2 >= P && (3*q + 2) == scores[size-n]) || (q + 1 >= P && (3*q) == scores[size-n] && scores[size-n] != 0)){
						ans++;
						S--;
					}
				}
			}
		}



		fprintf(file_out, "Case #%d: %d\n", t+1, ans);
	}


//	fprintf(file_out, "num %d\n", num);



	return 0;
}
