#include <stdio.h>
#include <string.h>
#include <map>
using namespace std;

FILE *fin = fopen ("input.txt","r");
FILE *fout = fopen ("output.txt","w");

map<__int64, int> CHK[11];
int T,L,U,V[11],K;
char N[111];
__int64 p,G[10000];

__int64 di(int p, int v)
{
	__int64 S = 0;
	int t;

	while (1){
		if (v == 0) break;
		
		t = v % p; v /= p;
		S += t * t;
	}

	return S;
}

int main()
{
	int i,j,k,f;

	fscanf (fin,"%d\n",&T);

	for (i=2;i<=10;i++){
		for (j=2;j<=600000;j++){
			p = j;

			if (CHK[i][p] == 0){
				CHK[i][p] = 2; G[0] = p; U = 0;

				while (1){
					U++; G[U] = di(i,G[U-1]);
					if (G[U] == 1){f = 1; break;}
					if (CHK[i][G[U]] != 0){f = CHK[i][G[U]]; break;}
					CHK[i][G[U]] = 2;
				}

				if (f == 2){
					for (k=0;k<U;k++) CHK[i][G[k]] = 2;
				}
				else{
					for (k=0;k<U;k++) CHK[i][G[k]] = 1;
				}
			}
		}
	}

	int CASE = 0,O,x;

	while (T--){
		fgets(N,100,fin); L = strlen(N); O = K = 0;
		for (i=0;;i++){
			sscanf(N+O,"%d",&x); V[K++] = x;
			if (x == 10) O += 3;
			else O += 2;
			if (L <= O) break;
		}

		for (__int64 s=2;;s++){
			bool v = true;
			for (j=0;j<K;j++){
				if (CHK[V[j]][s] == 2){v = false; break;}
			}

			if (v){
				CASE++; fprintf (fout,"Case #%d: %I64d\n",CASE,s); break;
			}
		}
	}

	return 0;
}