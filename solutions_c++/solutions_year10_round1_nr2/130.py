#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>


using namespace std;

int D,I,M,N;

int investigate(int a, int b) {
	int diff = abs(a-b);
	if (diff<=M) return 0;
	// inserts needed...
	if (M!=0) {
		int inserts = (diff-1)/M;
		int o2 = inserts*I;
		int o3 = max(0,inserts-1)*I+max(0,diff-inserts*M);
		return min(max(0,diff-M),min(max(o2,0),max(0,o3)));
	}
	else return max(0,diff);
}

int main() {
	int T;
	cin >> T;
	
	for (int i=1;i<=T;i++) {
		if (i!=1) cout << endl;
		
		cin >> D >> I >> M >> N;
		vector<int> a;
		for (int j=0;j<N;j++) {
			int k;
			cin >> k;
			a.push_back(k);
		}
		
		cout << "Case #" << i << ": ";
		if (N==1) {cout << 0; continue;}
		int o1 = (N-1)*D; // delete all but 1
		if (N==2) {
			/*int diff = abs(a[0]-a[1]);
			if (diff<=M) {cout << 0; continue;}
			// inserts needed...
			int inserts = (diff-1)/M;
			int o2 = inserts*I;
			int o3 = (inserts-1)*I+(diff-(inserts+1)*M);
			cout << min(min(o1,o2),o3);*/
			cout << min(o1,investigate(a[0],a[1]));
			continue;
		}
		else {
			int a1 = investigate(a[0],a[1]);
			int a2 = investigate(a[1],a[2]);
			int a3 = investigate(a[0],a[2]);
			int o2 = a1+D, o3=a2+D,o4=a3+D,o5=a1+a2;
			if (a[1]!=a[0]) for (int z=a[1];(z-a[0])*(a[1]-a[0])>=0;z-=(a[1]-a[0])/abs(a[1]-a[0])) {
				//cout << "T" << (z-a[0])*(a[1]-a[0]) << z << endl;
				int test = investigate(a[0],z)+investigate(a[2],z)+abs(z-a[1]);
				if (o5>test) o5=test;
				//cout << test << " for " << z << endl;
				//cout << investigate(a[0],z) << investigate(a[2],z) << endl;
			}
			//cout << o1 << "," << o2 << "," << o3 << "," << o4 << "," << o5 << endl;
			cout << min(o1,min(o2,min(o3,min(o4,o5))));
			
		}
	}
	cout << endl;
	return 0;	
}
