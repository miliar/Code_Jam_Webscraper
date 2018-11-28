#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
	int N,i,cnt;
	long long ans,x;
	map <char,int> m;
	string str;
	
	cin >> N;
	for (int testcase=1;testcase<=N;testcase++) {
		m.clear();
		
		cin >> str;
		if (str.length() == 1) {
			cout << "Case #" << testcase << ": " << 1 << endl;
			continue;
		}
		
		for (i=0,cnt=0;i<str.length();i++) if (m.find(str[i]) == m.end()) {
			m[str[i]] = cnt ? (cnt-1) ? cnt : 0 : 1;
			cnt++;
		}
		
		cnt = max(cnt,2);
		
		for (i=str.length()-1,x=1,ans=0;i>=0;i--) {
			ans += m[str[i]] * x;
			x *= cnt;
		}
		cout << "Case #" << testcase << ": " << ans << endl;
	}
}
