#include <stdio.h>
#include <vector>
using namespace std;

int N,S[2020],Y[2020],NON;

void go(int s, int e, int d)
{
	if (s >= e) return;
	if (NON) return;

	int x = s;
	Y[s] = Y[e] - (e - s) * d;
	while (x < e){
		if (S[x] > e){NON = 1; return;}
		Y[S[x]] = Y[x] + (S[x] - x) * d;
		go(x+1,S[x],d+1);
		x = S[x];
	}
}

int main()
{
	int T,Case=0;
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int i;

	scanf ("%d",&T); while (T--){
		scanf ("%d",&N); NON = 0;
		for (i=1;i<N;i++) scanf ("%d",&S[i]);
		Y[N] = 1000000000;
		go(1,N,0);

		printf ("Case #%d: ",++Case);
		if (NON) printf ("Impossible");
		else for (i=1;i<=N;i++) printf ("%d ",Y[i]);
		printf ("\n");
	}
	return 0;
}