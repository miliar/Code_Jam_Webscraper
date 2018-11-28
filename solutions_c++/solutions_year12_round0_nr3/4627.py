#include <iostream>
#include <sstream>
#include <map>
#include <string>
#include <cstdlib>
using namespace std;

bool check(int n, int m) {
//	cout << n << endl;
	ostringstream oss1;
	ostringstream oss2;
	oss1 << n;
	oss2 << m;
	string str1 = oss1.str();
	string str2 = oss2.str();
	
//	cout << "str1 : " << str1 << endl;
//	cout << "str2 : " << str2 << endl;
	string tmp = str2;
	for(int i=0;i<str2.size();i++) {
		tmp += tmp[0];
		tmp.erase(tmp.begin());
//		cout << tmp << endl;
		if(str1.compare(tmp) == 0)
			return true;
	}
	
	return false;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	for(int t=1;t<=T;t++) {
		int res = 0;
		int A, B;
		cin >> A >> B;
		for(int n = A; n<=B;n++) {
			for(int m=n+1;m<=B;m++) {
				if(check(n, m)) {
					res ++;
				}
			}
		}
		cout << "Case #" << t << ": " << res << endl;
	}
	
	return 0;
}
