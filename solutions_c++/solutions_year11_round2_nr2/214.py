#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

int T,N,CA; double D;
vector<double> W;

bool chk (double p)
{
	double l = W[0] - p;
	int i;
	for (i=1;i<W.size();i++){
		if (W[i] - l <= D){
			l = l + D;
			if (l - W[i] > p) return false;
		}
		else{
			l = max(l+D,W[i] - p);
		}
	}
	return true;
}

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int i,j,x;

	scanf ("%d",&T); while (T--){
		scanf ("%d %lf",&N,&D); W.clear();
		for (i=0;i<N;i++){
			scanf ("%d %d",&x,&j);
			while (j--) W.push_back(x);
		}sort(W.begin(),W.end());

		double l = 0, r = 1000000000000000ll, m;
		for (i=0;i<100;i++){
			m = (l + r) / 2;
			if (chk(m)) r = m;
			else l = m;
		}

		printf ("Case #%d: %.10lf\n",++CA,m);
	}

	return 0;
}