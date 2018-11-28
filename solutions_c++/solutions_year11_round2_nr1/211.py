#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

int T,N,CA; char S[111][111];
double C[111],W[111],WP[111],OWP[111],OOWP[111];

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int i,j;

	scanf ("%d",&T); while (T--){
		scanf ("%d",&N);
		for (i=0;i<N;i++) WP[i] = OWP[i] = OOWP[i] = C[i] = W[i] = 0;
		for (i=0;i<N;i++){
			scanf ("%s",S[i]);
			for (j=0;j<N;j++){
				if (S[i][j] != '.') C[i]++;
				if (S[i][j] == '1') W[i]++;
			}
			WP[i] = W[i] / C[i];
		}

		for (i=0;i<N;i++){
			for (j=0;j<N;j++){
				if (S[i][j] == '0') OWP[i] += (W[j] - 1) / (C[j] - 1);
				if (S[i][j] == '1') OWP[i] += W[j] / (C[j] - 1);
			}
			OWP[i] = OWP[i] / C[i];
		}

		for (i=0;i<N;i++){
			for (j=0;j<N;j++){
				if (S[i][j] == '0') OOWP[i] += OWP[j];
				if (S[i][j] == '1') OOWP[i] += OWP[j];
			}
			OOWP[i] = OOWP[i] / C[i];
		}

		printf ("Case #%d:\n",++CA);
		for (i=0;i<N;i++) printf ("%.10lf\n",WP[i]*0.25+OWP[i]*0.5+OOWP[i]*0.25);
	}

	return 0;
}