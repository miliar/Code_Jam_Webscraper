#include<iostream>
using namespace std;
#define MAX 50

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T; cin>>T;
	for (int t=1; t<=T; t++) {
		int N; cin>>N;

		int counter[MAX];
		for (int i=0; i<MAX; i++) counter[i]=0;

		int MIN=1000000, TOTAL=0;
		while(N--) {
			int curr, c=0; cin>>curr;
			if(MIN>curr) MIN=curr;
			TOTAL+=curr;

			while(1) {
				if(curr==0) break;
				counter[c]=(counter[c]+(curr%2))%2;
				curr/=2;
				c++;
			}
		}

		bool flag=true;
		for (int i=0; i<MAX; i++) {
			if(counter[i]!=0) {flag=false; break;}
		}

		cout << "Case #" << t << ": ";
		if(flag) cout << TOTAL-MIN << endl;
		else cout << "NO" << endl;
	}
	return 0;
}
