#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <set>

using namespace std;

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);
	int z;
	cin >> z;
	for (int q=0;q<z;q++) {
		long long l,t,n,c;
		cin >> l >> t >> n >> c;
		
		vector<long long> dis(c);
		for (int i=0;i<c;i++) {
			cin >> dis[i];
		}

		long long res = 0;
		long long cur = 0;
		int speed = 2;
		while (cur < n) {
			if (res + dis[cur % c] * 2 > t) {
				vector<int> rem;
				for (int i=cur+1;i<n;i++) {
					rem.push_back(dis[i%c]);
				}
				rem.push_back(dis[cur%c] - (t - res) / 2);
				res = t;
				sort(rem.rbegin(), rem.rend());
				for (int i=0;i<rem.size();i++) {
					if (i < l) {
						res += rem[i];
					}
					else res += rem[i] * 2;
				}
				break;
			}
			else {
				res += dis[cur % c] * 2;
				cur++;
			}
		}
		cout << "Case #" << (q+1) << ": " << res << endl;
	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}