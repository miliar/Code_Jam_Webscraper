#include <iostream>
#include <string>
#include <deque>

using namespace std;

int rotate(deque<int> &v, int sum) {
	int count = 0, spliced = 0;
	while(true) {
		if(sum-v[0]>=0 && spliced<v.size()) {
			sum -= v[0];
			count += v[0];
			v.push_back(v[0]);
			v.pop_front();
			++spliced;
		} else break;
	}
	return count;
}

int main() {
	long R, k, n, i, money;
	deque<int> q;
	cin>>i;
	for(int c=0,d,e=0;c<i;++c) {
		cin>>R>>k>>n;
		q.clear();
		for(d=0;d<n;++d) {
			cin>>e;
			q.push_back(e);
		}
		money = 0;
		while(--R>=0) 
			money += rotate(q, k);
		cout << "Case #" << (c+1) << ": " << money << endl;
	}
	return 0;
}