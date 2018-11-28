#include <iostream>
#include <array>
#include <vector>
#include <cassert>
#include <cmath>
#include <string>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <list>
#include <set>
#include <map>

using namespace std;

vector<int64_t> memo;
int64_t partsum(int64_t i0,int64_t i1,const vector<int64_t> & ai) {

	assert(i0 <= i1);
	assert(i1 < memo.size());
	return memo[i1]-memo[i0];
}

int64_t calctime(int64_t init,int64_t t,int64_t length) {
	int64_t ps1 = t-init;
	if (ps1 <= 0) return length+init;
	if (ps1 >= length*2) return length*2+init;
	return init + ps1 + (length-ps1/2);
}

int64_t solve1(int64_t W,int64_t t,int64_t N,const vector<int64_t> & ai) {
	int64_t ans = 0;
	ans+=partsum(0,W,ai)*2;
	
	int64_t length = ai[W%ai.size()];
	ans = calctime(ans,t,length);
	ans+=partsum(W+1,N,ai)*2;
	return ans;	
}

int64_t solve2(int64_t W1,int64_t W2,int64_t t,int64_t N,const vector<int64_t> & ai) {
	int64_t ans = 0;
	ans+=partsum(0,W1,ai)*2;
	
	int64_t length = ai[W1%ai.size()];
	ans = calctime(ans,t,length);
	ans+=partsum(W1+1,W2,ai)*2;
	
	length = ai[W2%ai.size()];
	ans = calctime(ans,t,length);
	ans+=partsum(W2+1,N,ai)*2;
	return ans;	
}

int64_t solve(int64_t L,int64_t t,int64_t N,const vector<int64_t> & ai) {
	memo = vector<int64_t>(N+1);
	memo[0] = 0;
	for (int i=1;i < N+1;++i)
		memo[i] = memo[i-1]+ai[(i-1)%ai.size()];
	switch (L) {
		case 0:
			return partsum(0,N,ai)*2;
		case 1:
		{
			int64_t ans = 10000000;
			for (int64_t i=0;i < N;++i)
				ans = min(ans,solve1(i,t,N,ai));
			return ans;
		}
		case 2:
		{
			int64_t ans = 10000000;
			for (int64_t i=0;i < N;++i)
				for (int64_t j=i+1;j < N;++j)
					ans = min(ans,solve2(i,j,t,N,ai));
			return ans;
		}
	}
	return -1;
}

int main(int argc, char **argv) {
// 	cout << calctime(0,4,10) << endl;
	cout << fixed << setprecision(12);
	int64_t T;
	
// 	ifstream input("input.txt");
	cin >> T;

	for(int64_t i=0;i < T;++i) {
		int64_t L,t,N,C;
		cin>> L >> t >> N >> C;
		vector<int64_t> ai(C);
				
		for (int64_t j=0;j < C;++j) {
			cin>> ai[j];
		}
		
		cout << "Case #" << i+1 << ": " << solve(L,t,N,ai) << endl;
	}
	
    return 0;
}
