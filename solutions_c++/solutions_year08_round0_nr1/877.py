#include <iostream>
#include <map>
#include <vector>
#include <string>
using namespace std;

int main(void)
{
	char buf[1024];

	int i, j;
	int N, S, Q;
	cin >> N;
	for (i=1; i<=N; ++i) {
		cin >> S;
		cin.getline(buf, sizeof(buf));

		vector<string> engines;
		map<string, bool> engineIsUsed;
		for (j=0; j<S; ++j) {
			cin.getline(buf, sizeof(buf));
			engines.push_back(buf);
			engineIsUsed[buf] = false;
		}

		cin >> Q;
		cin.getline(buf, sizeof(buf));
		int ans = 0;
		int usedEngineNum = 0;
		for (j=0; j<Q; ++j) {
			cin.getline(buf, sizeof(buf));

			//cout << buf << endl;

			if (engineIsUsed[buf]) {
				continue;
			}

			usedEngineNum++;

			if (usedEngineNum == S) {
				//cout << "---" << endl;
				ans ++;
				usedEngineNum = 1;
				for (int k=0; k<S; ++k) {
					engineIsUsed[engines[k]] = false;
				}
			}

			engineIsUsed[buf] = true;
		}


		cout << "Case #" << i << ": " << ans << endl;
	}

	return 0;
}

