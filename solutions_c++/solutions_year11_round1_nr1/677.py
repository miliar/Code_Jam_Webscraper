#include <iostream>

using namespace std;

int gcd(long long a, long long b) {
	if(b==0) return a;
	else return gcd(b, a % b);
}

int lcm(long long a, long long b) {
	return a / gcd(a, b) * b;
}

int show(int no, int flag) {
	string ans;
	ans = flag ? "Possible" : "Broken";
	cout << "Case #" << no << ": " << ans << endl;
}

int main()
{
	int T;
	cin >> T;
	for(int no=1;no<=T;no++) {
		long long N, Pd, Pg, D, Wd, Ld, G, Wg, Lg;
		int flag = 1;
		cin >> N >> Pd >> Pg;
		
		if(Pg==100 && Pd!=100) {
			show(no, 0);
			continue;
		}
		
		if(Pg==0 && Pd!=0) {
			show(no, 0);
			continue;
		}
		
		
		long long g = gcd(100, Pd);
		D = 100 / g;
		if(D>N) {
			show(no, 0);
			continue;
		}
		show(no, 1);
	}
	return 0;
}
