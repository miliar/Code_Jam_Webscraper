#include <iostream>1
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>

using namespace std;

long long v[1002], mem[1002], before[1002];

int main(){
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	
	int T;
	cin>>T;
	for (int t = 0; t < T; ++t){
		unsigned long long r, k, n, g, res = 0;
		cin>>r>>k>>n;
		for (int i = 0; i < n; ++i){
			cin>>g;
			v[i] = g;
		}

		memset(mem, -1, sizeof(mem));
		unsigned long long pos = 0, step = 0;
		for(;step < r;++step){
			if (mem[pos] != -1){
				int lcycle = step - mem[pos];
				unsigned long long rcycle = res - before[pos];
				res = before[pos];
				long long left = r - mem[pos];
				if (left > 0){
					res += rcycle*(left / lcycle);
					left %= lcycle;
					for (step = 0; step < left; ++step){
						unsigned long long sum = v[pos], spos = pos;
						++pos; pos %= n;
						while (sum + v[pos] <= k && pos != spos){
							sum += v[pos];
							++pos;pos %= n;
						}
						res += sum;
					}
				}
				break;
			}else{
				mem[pos] = step;
				before[pos] = res;
				unsigned long long sum = v[pos], spos = pos;
				++pos;pos %= n;
				while (sum + v[pos] <= k && pos != spos){
					sum += v[pos];
					++pos;pos %= n;
				}
				res += sum;
			}
		}
		cout<<"Case #"<<t+1<<": "<<res<<endl;
	}

	return 0;
}