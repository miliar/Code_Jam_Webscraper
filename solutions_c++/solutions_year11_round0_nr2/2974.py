#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair

int main(){

	FILE* input = fopen("input.txt", "r");
	FILE* output = fopen("output.txt", "w");
	
	int nTestCases = 0;
	fscanf(input,"%d", &nTestCases);

	for(int tt=0; tt<nTestCases; tt++){
		
		int C = 0;
		fscanf(input, "%d ", &C);
		char combinations[300][300];
		memset(combinations,0,sizeof(char)*300*300);
		for(int i=0; i<C; i++){
			char combination[5];
			fscanf(input, "%s", combination);
			combinations[combination[0]][combination[1]] = combination[2];
			combinations[combination[1]][combination[0]] = combination[2];
		}
		

		int D = 0;
		fscanf(input, "%d ", &D);
		char oposed[5];
		bool oposeds[300][300];
		memset(oposeds,0,sizeof(bool)*300*300);
		for(int i=0; i<D; i++){
			fscanf(input, "%s", oposed);
			oposeds[oposed[0]][oposed[1]] = true;
			oposeds[oposed[1]][oposed[0]] = true;
		}


		int N = 0;
		fscanf(input, "%d ", &N);
		char letters[1000];
		fscanf(input, "%s", letters);

		char ret[1000];
		memset(ret,0,sizeof(char)*1000);
		int idx = 1;
		ret[0] = letters[0];
		for(int i=1; i<N; i++){
			ret[idx] = letters[i];
			while(idx > 0 && combinations[ret[idx - 1]][ret[idx]]){
				ret[idx - 1] = combinations[ret[idx - 1]][ret[idx]];
				idx--;
			}
			for(int j=0; j<idx; j++){
				if(oposeds[ret[j]][ret[idx]]){
					idx = -1;
				}
			}
			idx++;
		}

		fprintf(output, "Case #%d: ", tt+1);
		fprintf(output, "[");
		for(int i=0; i<idx; i++){
			if(i)fprintf(output, ", %c", ret[i]);
			else fprintf(output, "%c",ret[i]);
		}
		fprintf(output, "]\n");

	}
}