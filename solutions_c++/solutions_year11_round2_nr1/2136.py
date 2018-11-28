/*
 * main.cpp
 *
 *  Created on: 2011-04-28
 *      Author: ronanrmo
 */
#include <cstdio>
#include <vector>
#include <string.h>
using namespace std;

#define F0(i,n) for(int i=0; i<n; i++)
#define F1(i,n) for(int i=1; i<n; i++)

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

	for(int t=0; t<T; t++){
		int N;
		fscanf(file_in, "%d", &N);
//		int team[N][N];

		char games[N][N+1];
		fprintf(file_out, "Case #%d:\n", t+1);
		for(int n = 0; n < N; n++){
			fscanf(file_in, "%s", games[n]);
		}

		float WP[N];// = 0;
		float OWP[N];// = 0;
		float OOWP[N];// = 0;
		float G[N];//  = 0;
		float W[N];// = 0;
		float gi[N];

		memset(WP, 0, sizeof(float)*N);
		memset(OWP, 0, sizeof(float)*N);
		memset(OOWP, 0, sizeof(float)*N);
		memset(G, 0, sizeof(float)*N);
		memset(W, 0, sizeof(float)*N);
		memset(gi, 0, sizeof(float)*N);

		F0(n,N){

			F0(g,N){
				if(games[n][g] == '1')
					W[n]++;
				if(games[n][g] != '.')
					G[n]++;
			}
			WP[n] = W[n]/G[n];



			F0(g,N){
				if(games[n][g] != '.'){
					float w= 0;
					float ga = 0;
					F0(k,N){
						if(k != n){
							if(games[g][k] == '1'){
								w++;

							}
							if(games[g][k] != '.')
								ga++;

						}
					}
					OWP[n]+= w/ga/G[n];

				}

			}

//			OWP[n] = W[n]/G[n];

		}

		F0(n,N){
			F0(g,N){
				if(games[n][g] != '.'){
					OOWP[n] += OWP[g]/G[n];
				}
			}

			float RPI = 0.25 * WP[n] + 0.50 * OWP[n] + 0.25 * OOWP[n];
			fprintf(file_out, "%g\n", RPI);
		}




	}


//	fprintf(file_out, "num %d\n", num);



	return 0;
}
