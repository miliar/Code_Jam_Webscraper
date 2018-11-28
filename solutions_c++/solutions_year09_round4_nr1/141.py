#include <iostream>
#include <cstring>
using namespace  std;
const int MAXN = 50;
string data[MAXN];
int main(){
	int cases;
	cin >> cases;
	for (int tt = 0; tt < cases; ++tt){
		int n;
		cin >> n;
		getchar();
		for (int i = 0; i < n; ++i){
			cin >> data[i];
		}
		bool used[MAXN];
		memset(used, 0, sizeof(used));
		int ans = 0;
		for (int i = 0; i < n; ++i){
			for (int j = i; j < n; ++j){
				
				bool ok = true;
				int id = -1;
				for (int k = i + 1; k < n; ++k){
					if (data[j][k] == '1'){
						ok = false;
						break;
					}
				}
				if (ok){
			//		cout << i << " " << j << endl;
					used[j] = true;
					ans += j > i ? j - i : i - j;
					if (j < i){
						for (int k = j + 1; k <= i; ++k){
							swap(data[k], data[k - 1]);
						}
					} else {
						for (int k = j; k > i; --k){
							swap(data[k], data[k - 1]);
						}
					}
					break;
				}
			}
		}
		printf("Case #%d: %d\n", tt + 1, ans);
	}
	return 0;
}
