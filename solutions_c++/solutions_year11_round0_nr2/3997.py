#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <stack>
#include <set>

using namespace std;

char combine[256][256];
bool oppose[256][256];

char & combined(char x, char y) {
	char a = std::min(x, y);
	char b = std::max(x, y);
	return combine[a][b];
}

bool & opposed(char x, char y) {
	char a = std::min(x, y);
	char b = std::max(x, y);
	return oppose[a][b];
}

int main(int argc, char * argv[])
{
	int T;
	cin >> T;


	for (int t = 1; t <= T; t++) {
		memset(combine, 0, 256*256);
		memset(oppose, 0, 256*256);
		int C;
		cin >> C;
		std::string tmp;
		for (int i = 0; i < C; i++) {
			cin >> tmp;
			combined(tmp[0], tmp[1]) = tmp[2];
		}
		int D;
		cin >> D;
		for (int i = 0; i < D; i++) {
			cin >> tmp;
			opposed(tmp[0], tmp[1]) = true;
		}
		int N;
		cin >> N;
		cin >> tmp;

		int seen[256];
		memset(seen, 0, 256*sizeof(int));
		std::stack<char> stack;
		for (size_t i = 0; i < tmp.size(); i++) {
			char curr = tmp[i];
			if (stack.empty()) {
				stack.push(curr);
				seen[curr]++;
				continue;
			}

			char c = combined(stack.top(), curr);
			if (c != 0) {
				seen[stack.top()]--;
				stack.pop();
				stack.push(c);
				continue;
			} 
			bool reset = false;
			for (size_t i = 0; i < 256; i++) {
				if ((seen[i] > 0) && opposed((char)i, curr)) {
					memset(seen, 0, 256*sizeof(int));
					reset = true;
					while (!stack.empty()) stack.pop();
					break;
				}
			}
			if (!reset) {
				stack.push(curr);
				seen[curr]++;
			}
		}
		std::vector<char> reverse;
		while (!stack.empty()) {
			reverse.push_back(stack.top());
			stack.pop();
		}
		std::reverse(reverse.begin(), reverse.end());
		cout << "Case #" << t << ": [";
		if (!reverse.empty()) cout << reverse[0];
		for (size_t i = 1; i < reverse.size(); i++) {
			cout << ", " << reverse[i];
		}
		cout << "]\n";
	}

	return 0;
}

