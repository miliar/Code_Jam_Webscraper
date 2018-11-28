#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
using namespace std;

struct stage{int l,p,i;} S[1010];
bool cmp(const stage& a, const stage& b){return a.p == b.p ? a.i < b.i : a.p > b.p;}
int N;

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int i,Test,Case=0;
	scanf ("%d",&Test); while (Test--){
		scanf ("%d",&N);
		for (i=0;i<N;i++) scanf ("%d",&S[i].l);
		for (i=0;i<N;i++) scanf ("%d",&S[i].p);
		for (i=0;i<N;i++) S[i].i = i;
		sort(S,S+N,cmp);
		printf ("Case #%d: ",++Case);
		for (i=0;i<N;i++) printf ("%d ",S[i].i);
		printf ("\n");
	}

	return 0;
}