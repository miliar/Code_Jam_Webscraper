#include <iostream>
#include <algorithm>

using namespace std;

int M, V;
int inter[10001];
int change[10001];
int leaf[10001];

int calculate() {
	int best[10001][2];
	for(int i=M; i>=(M+1)/2; i--) {
		best[i][0] = best[i][1] = M+1;
		best[i][leaf[i]] = 0;
	}
	for(int i=(M-1)/2; i>=1; i--) {
		best[i][0] = best[i][1] = M+1;
		if(inter[i] == 1) //AND
		{
			best[i][0] = min(best[i*2][0], best[i*2+1][0]);
			best[i][1] = best[i*2][1] + best[i*2+1][1];
		}
		else //OR
		{
			best[i][1] = min(best[i*2][1], best[i*2+1][1]);
			best[i][0] = best[i*2][0] + best[i*2+1][0];
		}

		if(change[i] == 1)
			if(inter[i] == 1) //AND
			{
				best[i][0] = min(best[i][0], best[i*2][0] + best[i*2+1][0] + 1);
				best[i][1] = min(best[i][1], min(best[i*2][1], best[i*2+1][1]) + 1);
			}
			else //OR
			{
				best[i][0] = min(best[i][0], min(best[i*2][0], best[i*2+1][0]) + 1);
				best[i][1] = min(best[i][1], best[i*2][1] + best[i*2+1][1] + 1);
			}
	}
	return best[1][V];
}

int main(int argc, char* argv[]) {
	int n;
	cin >>n;
	for(int i=0; i<n; i++) {
		cin >>M >>V;
		for(int j=1; j<=(M-1)/2; j++)
			cin >>inter[j] >>change[j];
		for(int j=(M+1)/2; j<=M; j++)
			cin >>leaf[j];
		int r = calculate();
		cout <<"Case #" <<i+1 <<": ";
		if(r > M)
			cout <<"IMPOSSIBLE";
		else
			cout <<r;
		cout <<endl;
	}
}

/*
d:\Documents\Visual Studio 2008\Projects\GoogleCodeJam\Debug\
*/