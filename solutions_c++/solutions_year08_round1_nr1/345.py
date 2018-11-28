#include<iostream>
#include<algorithm>	
#include<map>
#include<vector>
#include<cmath>
#include<queue>
#include<string>

#define INF ((1 << 30) - 1)

using namespace std;

long long minsum(vector<int> &a, vector<int> &b) {
	sort(a.begin(), a.end());
	sort(b.begin(), b.end());
	
	long long sum, minsum = INF;
	
	do {	
		do {
			sum = 0;
			for(int i = 0; i < a.size(); i++) {
				sum += a[i] * b[i];
			}
		} while(next_permutation(b.begin(), b.end()));
		if(minsum > sum)
			minsum = sum;
	} while(next_permutation(a.begin(), a.end()));
	
	return minsum;
}

int main() {
	int T, N, x;
	long long sum;
	
	cin >> T;
	
	for(int ti = 0; ti < T; ti++) {
		deque<int> na, nb, pa, pb;
		vector<int> a, b;
		
		cin >> N;
		for(int ni = 0; ni < N; ni++) {
			cin >> x;
			a.push_back(x);
			if(x <= 0) {
				na.push_back(x);
			} else {
				pa.push_back(x);
			}
		}
		for(int ni = 0; ni < N; ni++) {
			cin >> x;
			b.push_back(x);
			if(x <= 0) {
				nb.push_back(x);
			} else {
				pb.push_back(x);
			}
		}
		
		sum = 0;
		
		sort(na.begin(), na.end());
		sort(pa.begin(), pa.end());
		sort(nb.begin(), nb.end());
		sort(pb.begin(), pb.end());
		
		while(!na.empty() && !pb.empty()) {
			sum += na[0] * pb[pb.size()-1];
			na.pop_front();
			pb.pop_back();
		}
		
		while(!nb.empty() && !pa.empty()) {
			sum += nb[0] * pa[pa.size()-1];
			nb.pop_front();
			pa.pop_back();
		}
		
		while(!na.empty() && !nb.empty()) {
			if(na[0] * nb[nb.size()-1] < na[0] * nb[nb.size()-1]) {
				sum += na[0] * nb[nb.size()-1];
				na.pop_front();
				nb.pop_back();
			} else {
				sum += na[nb.size()-1] * nb[0];
				na.pop_back();
				nb.pop_front();
			}
		}
		
		while(!pa.empty() && !pb.empty()) {
			if(pa[0] * pb[pb.size()-1] < pa[0] * pb[pb.size()-1]) {
				sum += pa[0] * pb[pb.size()-1];
				pa.pop_front();
				pb.pop_back();
			} else {
				sum += pa[pb.size()-1] * pb[0];
				pa.pop_back();
				pb.pop_front();
			}
		}
		
		cout << "Case #" << (ti+1) << ": " << sum << endl;
		//cout << "Case #" << (ti+1) << ": " << minsum(a, b) << endl;
	}
	
	return 0;
}
