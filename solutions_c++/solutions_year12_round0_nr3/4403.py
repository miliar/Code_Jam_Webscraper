#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int lead(int N) {
	if(N<10) return 1;
	return lead(N/10)*10;
}

int main(void) {
	int ts;
	cin >> ts;
	for(int tt=1; tt<=ts; tt++) {
		int A,B;
		cin >> A >> B;
		int cnt=0;
		for(int n=A; n<=B; n++) {
			int n2=n;
			int ld = lead(n2);
			for(;;) {
				n2 = n2/ld + (n2%ld)*10;
				if(n2==n) break;
				if(n2>=A && n2<=B && n2>=ld && n2>n) cnt++;
			}
		}
		cout << "Case #" << tt << ": " << cnt << endl;
	}
}
