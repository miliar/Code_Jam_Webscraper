#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <sstream>
#include <map>

using namespace std;

template<class A, class B> A convert(B x) {stringstream s; s << x; A r; s >> r; return r;} 
int mem[1000001];
int main() {
	memset(mem, 0, sizeof mem);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		memset(mem, 0, sizeof mem);
		int a, b;
		cin >> a >> b;
		int res = 0;
		for (int i = a; i <= b; ++i) {
			string s = convert<string>(i);		
			int cnt = 0;	
			for (int j = 0; j < (int)s.size()-1; ++j) {
				s = s[s.length()-1] + s.substr(0, s.length()-1);
				int si = convert<int>(s);
				if (s[0] != '0' && si > i && si <= b && si >= a) {
					if (mem[si] != i) {
						mem[si] = i;
						cnt++;
					}
				}
			}

			res += cnt;
		}
		
		cout << "Case #" << t+1 << ": ";
		cout << res;
		cout << endl;
	}
	return 0;
}