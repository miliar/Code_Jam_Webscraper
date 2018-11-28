#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <string>
#include <vector>
#include <cstring>
#include <cassert>
using namespace std;
inline int sqr(int x){
	return x * x;
}
int convert(int x, int base){
	int ret = 0;
	while (x != 0){
		ret += sqr(x % base);
		x /= base;
	}
	assert(ret < 10000);
	return ret;
}
const int MAXN = 12000000;
bool ans[MAXN][10];
bool s[10000];
int main(){
	int cases;
	for (int i = 2; i < MAXN; ++i){
		//cout << "sdfsdf" << i << endl;
			//cout << i << endl;
			if (i % 10000 == 0) cerr << i << endl;
			
			for (int j = 2; j <= 10; ++j){
				int now = i;
				memset(s, 0, sizeof(s));
				bool ok = true;
				while (true){
					int temp = convert(now, j);
			//		cout << i << " " << t << " " << now << " " << j << endl;
			//		getchar();
					
					now = temp;
					if (now == 1) break;
					if (s[now]){
						ok = false;
						break;
					} else s[now] = true;
				}
				ans[i][j] = ok;
			}
		
	}
	/*for (int i = 0; i < MAXN; ++i){
		printf("{");
		for (int j = 2; j < 10; ++j){
			printf("%d,", ans[i][j]);
		}
		printf("%d}, \n", ans[i][10]);
	}*/
	//getchar();
	cin >> cases;
	string str;
	getchar();
	for (int tt = 1; tt <= cases; ++tt){
		getline(cin, str);
		istringstream in(str);
	//	cout << str << endl;
		int x;
		vector<int> vec;
		while (in >> x){
			vec.push_back(x);
		}
		for (int i = 0; i < MAXN; ++i){
			bool ok = true;
			
			for (int j = 0; j < vec.size(); ++j){
				if (!ans[i][vec[j]]){
					ok = false;
					break;
				}
			}
			if (ok){
				printf("Case #%d: %d\n", tt, i);
				break;
			}
		}
	}
	return 0;
}