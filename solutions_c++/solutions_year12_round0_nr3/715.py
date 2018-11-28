#include <sstream>
#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

int main() {
	int T; scanf("%d", &T);

	for (int t = 0; t < T; t++) {
		int A, B; scanf("%d%d", &A, &B);
		stringstream ssB; ssB << B;
		string Bstr = ssB.str();

		long pairs = 0;
		while (A < B) {
			stringstream ss; ss << A << A;
			string str = ss.str();
			set<int> copies;

			for (int i = 1; i < str.size() / 2; i++) {
				bool success = false;
				for (int j = 0; j < str.size() / 2; j++) {
					if (str[j] < str[i + j]) { success = true; break; }
					else if (str[j] > str[i + j]) { break; }
				}
				if (success) {
					int j = 0;
					for (; j < str.size() / 2; j++) {
						if (str[i + j] > Bstr[j]) break;
						else if (str[i + j] < Bstr[j]) {j = str.size() / 2; break; }
					}
					if (j == str.size() / 2) {
						stringstream ss2; ss2 << str.substr(i, str.size() / 2);
						int next; ss2 >> next;
						if (!copies.count(next)) {
							copies.insert(next);
							pairs++;
						}
					}
				}
			}
			A++;
		}

		printf("Case #%d: %ld\n", t + 1, pairs);
	}
	return 0;
}
