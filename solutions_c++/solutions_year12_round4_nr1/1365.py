#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <sstream>
using namespace std;

ifstream fin("in");
ofstream fout("out");

const int MAX_N = 10005;

int N,D;
vector<int> d,l;

int mem[MAX_N][MAX_N];

int min(int a, int b) {
	return ((a<b)?a:b);
}

bool canreach(int from, int to) {
	if(to==N+1)
		return true;
	if(mem[from][to]==-1) {
		int length = min(l[to],d[to]-d[from]);
		int dist = d[to];
		bool b = false;
		for(int j=to+1; j<N+2; j++) {
			if(d[j]>dist+length)
				break;
			b = b | canreach(to,j);
		}
		mem[from][to] = (b?1:0);
	}
	return (mem[from][to]==1);
}

void init() {
	for(int i=0; i<N+2; i++)
		for(int j=0; j<N+2; j++)
			mem[i][j] = -1;
}

int main() {
	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		fin>>N;
		d.resize(N+2); l.resize(N+2);
		d[0] = l[0] = 0;
		for(int i=1; i<=N; i++) {
			fin>>d[i]>>l[i];
		}
		fin>>D;
		d[N+1] = D; l[N+1] = 0;
		init();

		fout << "Case #" << t << ": ";
		fout << ((canreach(0,1))?"YES":"NO") << endl;
	}

	return 0;
}

