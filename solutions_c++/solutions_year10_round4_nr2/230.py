#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;

ifstream fin("b.in");
ofstream fout("b.out");

int dp[1024][12][12];
int m[1024];
int pr[12][1024];

int p;
int n;

int ff(int f, int r, int pl) {
	if(dp[f][r][pl]!=-1) return dp[f][r][pl];
	if(r<=0) {
		dp[f][r][pl] = 0;
		return 0;
	}
	int ret = -2;
	int teams = (1<<r);
	int missed = p-r-pl;
	bool need = false;
	int i;
	for(i=f;i<f+teams;++i) {
		if(missed>=m[i]) {
			need = true;
			break;
		}
	}
	int tmp;
	// we go
	ret = pr[r][f] + ff(f,r-1,pl+1) + ff(f+teams/2,r-1,pl+1);
	if(!need) {
		tmp = ff(f,r-1,pl) + ff(f+teams/2,r-1,pl);
		if(tmp<ret)ret=tmp;
	}
	dp[f][r][pl] = ret;
	return ret;
}

int main() {
	int tests;
	fin>>tests;
	int testNum;
	int i,j;
	for(testNum=1;testNum<=tests;++testNum) {
		memset(dp,-1,sizeof dp);
		fin>>p;
		n = 1<<p;
		for(i=0;i<n;++i) fin>>m[i];
		int step = 2;
		for(i=1;i<=p;++i) {
			j=0;
			while(j<n) {
				fin>>pr[i][j];
				j += step;
			}
			step *= 2;
		}
		int ret;
		ret = ff(0,p,0);
		fout<<"Case #"<<testNum<<": "<<ret<<endl;
	}
	return 0;
}
