#include <iostream>
#include <vector>

using namespace std;

typedef unsigned long long int lli;

int main () {
	int t,c;
	cin >> t;
	c=1;
	while (c <= t) {
		lli R,k,N,r,result=0;
		cin >> R >> k >> N;
		vector<lli> rides;
		vector<lli> who_headed;
		vector<bool> used(N,false);

		vector<lli> g(N,0);
		for(int i = 0; i < N; i++) cin >> g[i];
		lli ptr = 0;
		r = 0;
		while (r<R && !used[ptr]) {
			who_headed.push_back(ptr);
			used[ptr]=true;
			lli acc = 0;
			lli started = ptr;
			bool flag = true;
			while(acc+g[ptr] <= k && ((started!=ptr)||flag) ) { acc+=g[ptr];ptr=(ptr+1)%N;flag=false;}
			result += acc;
			rides.push_back(acc);
			r++;
		}
		if(r != R) {
			lli left = 0,cycle = 0, cycle_len;
			for(int i = 0; i < rides.size(); i++) if(ptr == who_headed[i]) {ptr=i;break;}
			for(int i = ptr; i < rides.size(); i++) cycle+=rides[i];
			cycle_len = rides.size()-ptr;
			for(int i = 0; i < (R-(unsigned long long int)rides.size())%(cycle_len); i++) {
				left+=rides[ptr++];
				ptr = ptr%N;
			}
			result = result + ((R-(unsigned long long int)rides.size())/(cycle_len))*cycle+left;
		}
		cout << "Case #"<< c << ": " << result<< endl;
		c++;
	}
	return 0;
}

