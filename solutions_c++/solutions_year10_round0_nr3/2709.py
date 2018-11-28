#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;


typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

int group[1000];
int max[1000];
int next[1000];

void calculate(int num,int cap){
	int j, tmax = 0;
	For(i, 0, num-1){
	tmax=group[i];
	j=(i+1)%num;
	while((tmax+group[j])<=cap){
		tmax=tmax + group[j];
		j=(j+1)%num;
		}
	max[i]=tmax;
	next[i]=j;
	}
		
}
int main() {
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);
	
	
	int T;
	long r, k, sum = 0;
	int n;
	int index;
	cin>>T;
	For(i, 1, T) {
		cin>>r>>k>>n;
		sum=0;
		for(int j=0; j<n; j++){
			cin>>group[j];
			sum += group[j];
		}
		if(sum <= k)
			cout<<"Case #"<<i<<": "<<sum*r<<endl;
		else{
			calculate(n, k);
			index = 0;
			sum=0;
			for(int round=1; round<=r; round++){
				sum += max[index];
				index = next[index];
			}
			cout<<"Case #"<<i<<": "<<sum<<endl;
		}
	}
	return 0;
}
