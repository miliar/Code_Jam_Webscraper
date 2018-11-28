#include <iostream>

using namespace std;

char mapping[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i',
	'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main() {
	int n = 0;
	cin >> n;
	cin.get();
	for (int i = 0; i < n; ++i) {
		char buffer[128];
		cin.getline(buffer, 128);
		cout << "Case #" << i + 1 << ": ";
		for (int x = 0; buffer[x]; ++x) {
			if (buffer[x] == ' ') {
				cout << " ";
			} else {
				cout << mapping[buffer[x]-'a'];
			}
		}
		cout << endl;
	}
}