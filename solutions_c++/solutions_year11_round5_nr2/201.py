#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>
#include <stack>

using namespace std;

int main() {
	int T;

	cin >> T;

	for (int t=1;t<=T;t++) {
		int N;
		cin >> N;
		vector<int> hand;
		for (int n=0;n<N;n++) {
			int x;
			cin >> x;
			hand.push_back(x);
		}
		sort(hand.begin(),hand.end());

		queue<int> seqstart;
		int minlen=100000;
		int c=0;
		int prevk=0;
		int flag=0;
		//clog << hand.size();
		for (int n=0;n<N+1;) {
			//clog << n << endl;
			int k=0;
			if (n<N && (flag==0 || hand[n]==c+1)) {
				c=hand[n];
				flag=1;
			}
			else {
				c++;
				flag=0;
			}
			while (n<N && c==hand[n]) {
				n++;
				k++;
			}
			//clog << prevk << " to " << k << endl;
			if (prevk<k) { // start new sequences
				for (int i=0;i<k-prevk;i++) seqstart.push(c);
			}
			else if (prevk>k) {
				for (int i=0;i<prevk-k;i++) {
					int len=c-seqstart.front();
					//clog << "pop " << c << endl;
					seqstart.pop();
					if (minlen>len) minlen=len;
				}
			}

			prevk=k;
			if (flag==0 && n==N) break;
		}
		if (minlen==100000) minlen=0;
		cout << "Case #" << t << ": ";
		cout << minlen;
		//printf("%lf",time);
		
		cout << endl;
	}
	return 0;
}