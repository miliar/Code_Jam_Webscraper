#include <vector>
#include <string>
#include <algorithm>

using namespace std;


int main() {
	int T;
	scanf("%d", &T);
	getchar(); // \n

	for (int C = 1; C <= T; C++) {
		string input, phrase = "welcome to code jam";
		char c;
		vector <int> freq1(510, 0), freq2(510, 0);
		int size = 0;

		while ((c = getchar()) != '\n' && c != EOF) {
			input.push_back(c);
			if (c == 'm') freq1[size] = 1;
			size++;
		}

		int pos = 17;
		while (pos >= 0) {
			int count = 0;
			for (int i = size-1; i >= 0; i--) {
				if (input[i] == phrase[pos])
					freq2[i] = count;
				else {
					count = (count + freq1[i]) % 10000;
					freq1[i] = 0;
				}
			}
			pos--;

			count = 0;
			for (int i = size-1; i >= 0; i--) {
				if (input[i] == phrase[pos])
					freq1[i] = count;
				else {
					count = (count + freq2[i]) % 10000;
					freq2[i] = 0;
				}
			}
			pos--;
		}

		int count = 0;
		for (int i = 0; i < size; i++)
			count = (count + freq1[i]) % 10000;

		printf("Case #%d: %04d\n", C, count);
	}

	return 0;
}
