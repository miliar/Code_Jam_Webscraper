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

bool primer(long long n) {
	long long arrel = (long long)(sqrt(n));
	bool primer = n > 1;
	for (int b=2; primer && b<=arrel;++b) {
		if (n % b == 0) primer = false;
	}
	return primer;
}

int main() {
	int C;
	cin >> C;
	for (int t=1;t<=C;++t) {
		long long A,B,P;
		cin >> A >> B >> P;
		vector<int> vist(B-A+1,0);
		int k=42;
		for (long long p=P;p<=B;++p) {
			if (primer(p)) {
				set<int> grups;
				for (long long x=A+(p-A%p)%p;x<=B;x+=p) {
					if (vist[x-A]) grups.insert(vist[x-A]);
					vist[x-A]=k;
				}
				for (long long i=0;i<vist.size();++i) {
					if(grups.find(vist[i])!=grups.end()) vist[i]=k;
				}
				k++;
			}
		}
		set<int> grups;
		int ungrouped=0;
		for (int i=0;i<vist.size();++i) {
//			cerr << vist[i] << endl;
			if (vist[i]==0) ungrouped++;
			else grups.insert(vist[i]);
		}
		cout << "Case #" << t << ": " << ungrouped + grups.size() << endl;
	}
}
