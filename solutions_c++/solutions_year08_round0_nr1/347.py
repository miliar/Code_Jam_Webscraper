#include <cstdio>
#include <fstream>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

int cases;

string engine[105];
string query[1005];
int e,q;
map<string,int> ind;
int dp[1005][105];

int up[1005],down[1005];

const int INF=9000000;

int solve() {
	if (q==0) {return 0;}
	fill(dp[0],dp[1004]+105,INF);
	int taboo=ind[query[0]];
	for(int i=0;i<e;i++) {
		if (i!=taboo) {
			dp[0][i]=0;
		}
	}
	
	for(int i=1;i<q;i++) {
		up[0]=INF;
		for(int j=1;j<e;j++) {
			up[j]=min(up[j-1],dp[i-1][j-1]);
		}
		down[e-1]=INF;
		for(int j=e-2;j>=0;j--) {
			down[j]=min(down[j+1],dp[i-1][j+1]);
		}
	
	
		int explode=ind[query[i]];
		for(int j=0;j<e;j++) {
			if (j!=explode) {
				dp[i][j]<?=dp[i-1][j];
				dp[i][j]<?=(min(up[j],down[j])+1);
			}
		}
	}
	int ret=INF;
	for(int i=0;i<e;i++) {
		ret<?=dp[q-1][i];
	}
	
	return ret;
}

string scratch;

int main() {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	
	fin>> cases;
	for(int i=0;i<cases;i++) {
		ind.clear();
		fin >> e;
		getline(fin,scratch);
		for(int j=0;j<e;j++) {
			getline(fin,engine[j]);
			ind[engine[j]]=j;
		}
		fin >> q;
		getline(fin,scratch);
		for(int j=0;j<q;j++) {
			getline(fin,query[j]);
		}
		fout << "Case #" << i+1 << ": " << solve() << endl;
	}
	return 0;
}
