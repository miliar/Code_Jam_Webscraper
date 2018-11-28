#include <iostream>
#include <utility>

using namespace std;

long long sum;
int values[1000];

long long  _max=-1;

long long calc(int depth, int N, int a, int b, long long  c, long long  d) {
	if(sum-d <= _max) return -1;
	if(depth==N) {
		if(a!=b) return -1;
		if(c==sum || c==0) return -1;
		_max = c;
		return c;
	}
	return max(calc(depth+1, N, a^values[depth], b, c+values[depth], d), calc(depth+1, N, a, b^values[depth], c, d+values[depth]));
}

int main() {
	int T;
	cin >> T;
	
	for(int t=1; t<=T; t++) {
		int N;
		cin >> N;
		for(int i=0; i<1000; i++) values[i]=0;
		sum=0;
		_max=-1;
		int check=0;
		for(int i=0; i<N; i++) {
			cin >> values[i];
			sum+=values[i];
			check = check^values[i];
		}
		if(check==0) {
			long long result = calc(0, N, 0, 0, 0, 0);
			if(result==-1) {
				cout << "Case #" << t << ": NO" << endl;
			} else {
				cout << "Case #" << t << ": " << result << endl;
			}
		} else {
			cout << "Case #" << t << ": NO" << endl;
		}
	}
	
	return 0;
}
