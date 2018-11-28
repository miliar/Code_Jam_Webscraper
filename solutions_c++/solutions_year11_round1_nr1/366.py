#include <stdio.h>
#include <iostream>

using namespace std;

inline int gcd(int a,int b) {
	int t;
	while(b) {
		t=b;
		b=a%b;
		a=t;
	}
	return a;
}

inline int lcm(int a,int b) {
	return a*b/gcd(a,b);
}

inline bool solve(long long n,int a,int b) {
	int ga,ra,da;
	if(b==0||b==100) return a==b;
	ga=gcd(a,100);
	ra=100/ga;
	da=a/ga;
	return ra<=n;
}

int main(void) {
	int t,a,b,casenum=1;
	long long n;
	cin >> t;
	while(t--) {
		cin >> n >> a >> b;
		cout << "Case #" << casenum++ << ": ";
		cout << (solve(n,a,b)?"Possible":"Broken") << endl;
	}
}
