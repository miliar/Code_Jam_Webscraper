#include <iostream>
#include <string>
#include <map>
using namespace std;


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, n, m;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas){
		scanf("%d%d", &n, &m);
		int res = 0;
		map<string, bool> a, b;
		string str;
		for(int i = 0; i < n; ++i){
			cin >> str;
			a[str] = true;
		}
		for(int i = 0; i < m; ++i){
			cin >> str;
			b[str] = true;
		}
		for(map<string, bool>::iterator it = b.begin(); it != b.end(); ++it){
			str = it->first;
			for(int len = str.size(), i = 1; i < len; ){
				int p = str.find('/', i);
				if(p == string::npos) p = len;
				string substr = str.substr(0, p);
				//cout << "==" << substr << endl;
				if(!a[substr]){
					++res;
					a[substr] = true;
				}
				i = p + 1;
			}
		}
		printf("Case #%d: %d\n", cas, res);
	}
	return 0;
}