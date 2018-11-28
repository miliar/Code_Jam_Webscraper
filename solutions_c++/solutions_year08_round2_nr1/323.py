#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>
#include <utility>
#include <cmath>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;

int main() {
	int N;
	cin >> N;
	for (int t=1;t<=N;++t) {
		long long n,A,B,C,D,x0,y0,M;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		vector<long long> types(9,0);
		long long X=x0,Y=y0;
		types[(X%3)*3+Y%3]++;
		for (int i=1;i<n;++i) {
			X = (A*X+B)%M;
			Y = (C*Y+D)%M;
			types[(X%3)*3+Y%3]++;
		}
		for (int i=0;i<9;++i) cerr << i << ": " << types[i] << endl;
		long long ret=0;
		for (int i=0;i<9;++i) {
			for (int j=i;j<9;++j) {
				int k=((3-(i+j)%3)%3+((3-(i/3+j/3)%3)%3)*3)%9;
				if (k<i||k<j) continue;
				if (j==i) {
					if (k==i) ret+=types[i]*max(types[j]-1,0LL)*max(types[k]-2,0LL)/6;
					else ret+=types[i]*max(types[j]-1,0LL)/2*types[k];
				}
				else {
					if (k==i||k==j) ret+=types[i]*types[j]*max(types[k]-1,0LL)/2;
					else ret+=types[i]*types[j]*types[k];				
				}
				cerr << i << " " << j << " " << k << " " << ret << endl;
			}
		}
		cout << "Case #" << t << ": " << ret << endl;
	}
}
