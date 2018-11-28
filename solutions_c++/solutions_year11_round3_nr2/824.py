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

int findmax(vector<float> v){
	int idx = 0;
	float max = 0;
	F0(i,v.size()){
		if(v[i]>max)
		{
			max = v[i];
			idx = i;
		}
	}
	return idx;
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

	F0(te,T){
		int L, t, N, C;
		fscanf(file_in, "%d %d %d %d", &L, &t, &N, &C);

		int c[C];
		F0(i,C){
			fscanf(file_in, "%d", &c[i]);
		}

		vector<float> dis;
		F0(n, N){
			int idx = n%C;
			dis.push_back(c[idx]);
		}
		int td = 0;
		F0(n, N){
			td += dis[n];
//			printf("%g ", dis[n]);
		}
//		printf("Total dis = %d\n", td);
		float first = t*0.5;
//		printf("First = %g\n", first);

		float prev = 0;
		int first_idx;
		F0(n,N){

			if(first > prev && first < prev+dis[n]){
				float dd = dis[n];
				dis[n] = dd - ( prev+dd-first);
				dis.insert( dis.begin()+n, prev+dd-first);
				first_idx = n;
				break;

			}
			prev += dis[n];
		}


		F0(n, dis.size()){
			td += dis[n];
//			printf("%g ", dis[n]);
		}

		int time =0;

		F0(i,first_idx){
			time += 2*dis[0];
			dis.erase(dis.begin());
		}

		vector<int> max_idx;

//		printf("Time = %d", time);

		F0(n, dis.size()){
			td += dis[n];
//			printf("%g ", dis[n]);
		}


		while(dis.size()!=0 && L != 0){
			int indice = findmax(dis);
			time += dis[indice];
			dis.erase(dis.begin()+indice);
			L--;
		}

		while(dis.size()!=0){
			time += 2*dis[0];
			dis.erase(dis.begin());
		}



//		printf("\n%d %d %d %d\n", L, t, N, C);

		fprintf(file_out, "Case #%d: %d\n", te+1, time);
	}


//	fprintf(file_out, "num %d\n", num);



	return 0;
}
