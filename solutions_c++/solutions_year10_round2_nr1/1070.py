#include <iostream>
#include <string>
#include <map>

using namespace std;

map<string, int> existPath;
int main() {
	int t, n, m, cutAt;
	int count;
	string buffer;

	cin >> t;

	for(int i=1; i<=t; ++i) {
		existPath.clear();
		cin >> n >> m;

		for(int j=0; j<n; ++j) {
			string tmp = "";
			cin >> buffer;
			while ((cutAt = buffer.find_first_of('/')) != buffer.npos) {
				if ( cutAt > 0 ) {
					tmp = tmp + "/" + buffer.substr(0, cutAt);
					if ( existPath.find(tmp) == existPath.end()  ) {
						existPath.insert(pair<string, int>(tmp, 1));
					}
				}
				buffer = buffer.substr(cutAt+1);
			}
			if ( buffer.length() > 0 ) {
				tmp = tmp + "/" + buffer;
				if ( existPath.find(tmp) == existPath.end() ) {
					existPath.insert(pair<string, int>(tmp, 1));
				}
			}
		}
		count = 0;
		for(int k=0; k<m; ++k) {
			string tmp = "";
			cin >> buffer;
			while ((cutAt = buffer.find_first_of('/')) != buffer.npos) {
				if ( cutAt > 0 ) {
					tmp = tmp + "/" + buffer.substr(0, cutAt);
					if ( existPath.find(tmp) == existPath.end() ) {
						existPath.insert(pair<string, int>(tmp, 1));
						++count;
					}
				}
				buffer = buffer.substr(cutAt+1);
			}
			if ( buffer.length() > 0 ) {
				tmp = tmp + "/" + buffer;
				if ( existPath.find(tmp) == existPath.end() ) {
					existPath.insert(pair<string, int>(tmp, 1));
					++count;
				}
			}
		}
		cout << "Case #" << i << ": " << count << endl;
	}
	return 0;
}
