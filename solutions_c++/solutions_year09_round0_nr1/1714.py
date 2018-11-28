#include <stdio.h>
#include <vector>
#include <string>
using namespace std;
#define LM 20
#define DM 5555

FILE *fin = fopen ("input.txt","r");
FILE *fout = fopen ("output.txt","w");

vector<string> V,T,U;
char W[LM],O[LM*26];
int L,D,N,P,C[26];

int main()
{
	int i,j,k;

	fscanf (fin,"%d %d %d",&L,&D,&N);

	for (i=0;i<D;i++){
		fscanf (fin,"%s",&W); V.push_back(W);
	}

	for (i=0;i<N;i++){
		T = V; P = 0; fscanf (fin,"%s",&O);
		
		for (j=0;j<26;j++) C[j] = -1;

		for (j=0;j<L;j++){
			if (O[P] == '('){
				while (1){
					P++;
					if (O[P] == ')'){P++; break;}
					C[O[P]-'a'] = j;
				}
			}
			else C[O[P++]-'a'] = j;

			for (k=0;k<T.size();k++){
				if (C[T[k][j]-'a'] != j) U.push_back(T[k]);
			}
			T = U;
		}

		fprintf (fout,"Case #%d: %d\n",i+1,T.size());
	}

	return 0;
}