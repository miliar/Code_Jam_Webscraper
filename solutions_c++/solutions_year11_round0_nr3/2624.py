/*
 * main.cpp
 *
 *  Created on: 2011-04-28
 *      Author: ronanrmo
 */
#include <cstdio>
#include<vector>
#include<algorithm>
using namespace std;


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


//	fprintf(file_out, "num %d\n", T);

	for(int i=0; i<T; i++){
//		max = -1;
		int N;
		fscanf(file_in, "%d", &N);
		vector<int> vals;
		for(int j=0; j<N; j++){
			int val;
			fscanf(file_in, "%d", &val);
			vals.push_back(val);

			//			fprintf(file_out, "%d ", val);
		}
		// check
		bool possible;
		int sum=0;
		for(int j=0; j<vals.size(); j++){
			sum ^= vals[j];
		}

		if(sum != 0)
			possible = false;
		else possible = true;

		if(possible){
			sort(vals.begin(), vals.end());
			for(int s=1; s<N; s++){
				int sumP =0;
				int sumS =0;
				int sumT = 0;
				for(int j=0; j<s; j++){
//					printf("%d ", vals[j]);
					sumP ^= vals[j];
				}
				for(int j=s; j<vals.size(); j++){
//					printf("%d ", vals[j]);
					sumS ^= vals[j];
					sumT += vals[j];
				}
				if(sumP == sumS){
					fprintf(file_out, "Case #%d: %d\n",i+1, sumT);
					break;
				}else{
					fprintf(file_out, "Case #%d: NO\n",i+1);
				}
			}

		}else{
			fprintf(file_out, "Case #%d: NO\n",i+1);
		}

	}


	//	printf("%d %d %d\n", 5^4, 7^9, 50^10);

	return 0;
}





