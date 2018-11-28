#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <set>
#include <sstream>

using namespace std;

int main (void) {
	ofstream OUT;
	OUT.open ("OU.txt");
	ifstream FILE("IN.txt");
	int Num;
	FILE>>Num;
	for (int z=1; z<=Num; z++) {
		int M,V;
		FILE>>M>>V;
		vector <int> g((M-1)/2);
		vector <int> c((M-1)/2);
		for (int i=0; i<(M-1)/2; i++) FILE>>g[i]>>c[i];
		vector <vector <int> > cost(M, vector <int> (2, 40000));
		for (int i=(M-1)/2; i<M; i++) {
			int a;
			FILE>>a;
			cost[i][a]=0;
			}
		for (int i=0; i<g.size(); i++) cout<<g[i]<<" "<<c[i]<<"\n";
//		for (int i=0; i<M; i++) cout<<i<<" "<<cost[i][0]<<" "<<cost[i][1]<<"\n";
		
		for (int i=(M-1)/2-1; i>=0; i--) {
			int dx=(i+1)*2-1;
			int sx=dx+1;
			if (g[i]==0) {
				cost[i][0]=min(cost[i][0],cost[dx][0]+cost[sx][0]);
				cost[i][1]=min(cost[i][1],cost[dx][1]+cost[sx][0]);
				cost[i][1]=min(cost[i][1],cost[dx][0]+cost[sx][1]);
				cost[i][1]=min(cost[i][1],cost[dx][1]+cost[sx][1]);
				}
			if (g[i]==0) if (c[i]==1) {
				cost[i][0]=min(cost[i][0],cost[dx][0]+cost[sx][0]+1);
				cost[i][0]=min(cost[i][0],cost[dx][1]+cost[sx][0]+1);
				cost[i][0]=min(cost[i][0],cost[dx][0]+cost[sx][1]+1);
				cost[i][1]=min(cost[i][1],cost[dx][1]+cost[sx][1]+1);				
				}
			if (g[i]==1) {
				cost[i][0]=min(cost[i][0],cost[dx][0]+cost[sx][0]);
				cost[i][0]=min(cost[i][0],cost[dx][1]+cost[sx][0]);
				cost[i][0]=min(cost[i][0],cost[dx][0]+cost[sx][1]);
				cost[i][1]=min(cost[i][1],cost[dx][1]+cost[sx][1]);
				}
			if (g[i]==1) if (c[i]==1) {
				cost[i][0]=min(cost[i][0],cost[dx][0]+cost[sx][0]+1);
				cost[i][1]=min(cost[i][1],cost[dx][1]+cost[sx][0]+1);
				cost[i][1]=min(cost[i][1],cost[dx][0]+cost[sx][1]+1);
				cost[i][1]=min(cost[i][1],cost[dx][1]+cost[sx][1]+1);
				}
			}
		for (int i=0; i<M; i++) cout<<i<<" "<<cost[i][0]<<" "<<cost[i][1]<<"\n";

		if (cost[0][V]>=40000) OUT<<"Case #"<<z<<": "<<"IMPOSSIBLE"<<"\n";
		else OUT<<"Case #"<<z<<": "<<cost[0][V]<<"\n";
		}
	FILE.close();
	OUT.close();
	system("PAUSE");
	return 0;
	}
