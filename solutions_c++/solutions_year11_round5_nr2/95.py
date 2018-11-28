#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
int N;
int vs[1024];

struct S {
	int start;
	int end;
	int size() const {return end-start+1;}
	bool operator<(const S& s) const {
		return size() > s.size();
	}
};

bool test(int R) {
//	cout<<"testing "<<R<<'\n';
	priority_queue<S> open;
	vector<S> delay;
	for(int i=0; i<N; ++i) {
		int a = vs[i];
		if (!delay.empty() && a>delay[0].end) {
			for(size_t j=0; j<delay.size(); ++j) open.push(delay[j]);
			delay.clear();
		}
		S s;
		s.start = s.end = -5;
		while(!open.empty()) {
			s = open.top();
			open.pop();
			if (s.end < a-1) {
				if (s.size() < R) return 0;
				continue;
			}
			break;
		}

		if (s.end == a-1) {
			s.end = a;
		} else {
			s.start = a;
			s.end = a;
		}
		delay.push_back(s);
	}
	for(size_t j=0; j<delay.size(); ++j) open.push(delay[j]);
	while(!open.empty()) {
		S s = open.top();
//		cout<<"end pop: "<<s.start<<' '<<s.end<<'\n';
		open.pop();
		if (s.size() < R) return 0;
	}
	return 1;
}

int main()
{
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		cin>>N;
		for(int i=0; i<N; ++i) cin>>vs[i];
		sort(vs,vs+N);
		int low = 0;
		int hi = N+1;
		while(hi-low>1) {
			int mid = (low+hi)/2;
			if (test(mid)) {
				low = mid;
			} else {
				hi = mid;
			}
		}
		cout<<"Case #"<<a<<": "<<low<<'\n';
	}
}
