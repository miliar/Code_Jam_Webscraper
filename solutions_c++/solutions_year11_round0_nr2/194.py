#include<sys/types.h>
#include<dirent.h>

#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<cstdlib>
#include<sstream>
#include<cmath>
#include<fstream>
#include<map>
#include<set>

#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define ABS(x) ((x) > 0 ? (x) : -(x))

#define SWAP(x, y) {(x) += (y); (y) = (x) - (y); (x) -= (y);}

#define EPS 1e-6
#define PI 3.14159265358979323846

using namespace std;

int oppose[26][26];

int combine[26][26];

char line[8];

int x[1000];

int ccount[26];

char term[1000];

int main()
{
	
	int ncase;

	map<string, int> table;

	string tmpterm = "A";
	for(int i = 0; i < 26; i++){

		tmpterm[0] = i + 'A';
		table[tmpterm] = i;
	}

	scanf("%d", &ncase);

	for(int case_idx = 1; case_idx <= ncase; case_idx++){

		memset(oppose, 0, sizeof(oppose));
		for(int i = 0; i < 26; i++){
			for(int j = 0; j < 26; j++){
				combine[i][j] = -1;
			}
		}

		int C;
		scanf("%d", &C);
		for(int i = 0; i < C; i++){
			int a, b, c;
			scanf("%s", term);

			string tmpterm = "A";

			tmpterm[0] = term[0];
			a = table[tmpterm];
			tmpterm[0] = term[1];
			b = table[tmpterm];
			tmpterm[0] = term[2];
			c = table[tmpterm];

			combine[a][b] = c;
			combine[b][a] = c;
		}
		int D;
		scanf("%d", &D);
		for(int i = 0; i < D; i++){

			int a, b;
			scanf("%s", term);

			string tmpterm = "A";

			tmpterm[0] = term[0];
			a = table[tmpterm];
			tmpterm[0] = term[1];
			b = table[tmpterm];


			oppose[a][b] = 1;
			oppose[b][a] = 1;
		}


		int len = 0;

		int N;

		scanf("%d", &N);

		memset(ccount, 0, sizeof(ccount));

		scanf("%s", term);

		for(int i = 0; i < N; i++){
			int idx = term[i] - 'A';
			
			if(len && combine[idx][x[len - 1]] >= 0){

				ccount[x[len - 1]]--;
				x[len - 1] = combine[idx][x[len - 1]];
				ccount[x[len - 1]]++;

				continue;
			}
			for(int j = 0; j < 26; j++){
				if(ccount[j] && oppose[idx][j]){
					len = 0;
					memset(ccount, 0, sizeof(ccount));
					goto end;
				}
			}

			x[len] = idx;
			len++;
			ccount[idx]++;
end:
			;

		}

		printf("Case #%d: [", case_idx);
		for(int i = 0; i < len; i++){

			if(i)	printf(", ");
			printf("%c", x[i] + 'A');
		}
		printf("]\n");



	}
	return 0;
}

// vi: ts=2 sw=2
