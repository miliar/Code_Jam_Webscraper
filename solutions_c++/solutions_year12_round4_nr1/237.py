#include <stdio.h>
#include <algorithm>
using namespace std;

int N,D,d[10001],l[10001],X[10001];

int main()
{
	int T,Case=0;
	freopen ("A-large.in","r",stdin);
	freopen ("output.txt","w",stdout);
	int i,j,p;

	scanf ("%d",&T); while (T--){
		scanf ("%d",&N);
		for (i=1;i<=N;i++) scanf ("%d %d",&d[i],&l[i]), X[i] = 0;
		scanf ("%d",&D);
		X[1] = d[1];
		for (i=1;i<=N;i++){
			for (j=i+1;j<=N;j++){
				if (d[i] + X[i] < d[j]) break;
				if (l[j] >= d[j] - d[i]) X[j] = max(X[j],d[j]-d[i]);
				else X[j] = l[j];
			}
		}
		printf ("Case #%d: ",++Case);
		p = 0;
		for (i=1;i<=N;i++) if (D <= d[i] + X[i]) p = true;
		puts(p?"YES":"NO");
	}
}