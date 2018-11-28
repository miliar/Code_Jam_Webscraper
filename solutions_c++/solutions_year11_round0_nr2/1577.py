#include <cstdio>
#include <vector>
#include <string>

using namespace std;

vector<string> mag(int n) {
	vector<string> result;
	while(n--) {
		char inp[16];
		scanf("%s", inp);
		result.push_back(inp);
	}
	return result;
}

string combine(string inp, vector<string>& com) {
	if (inp.length() < 2) {
		return inp;
	}

	string a = inp.substr(inp.length() - 2, 2);
	for(int i = 0; i < com.size(); ++i) {
		if ((com[i][0] == a[0] && com[i][1] == a[1]) || (com[i][0] == a[1] && com[i][1] == a[0])) {
			return inp.substr(0, inp.length() - 2) + com[i][2];
		}
	}
	return inp;
}

string oppose(string inp, vector<string>& op) {
	for(int i = 0; i < op.size(); ++i) {
		if (inp.find(op[i][0]) != string::npos && inp.find(op[i][1]) != string::npos) {
			return "";
		}
	}

	return inp;
}

void solve() {
	int C, D, N;

	scanf("%d", &C);
	vector<string> com = mag(C);
	scanf("%d", &D);
	vector<string> op = mag(D);

	scanf("%d", &N);
	char ele[128];
	scanf("%s", ele);

	string result = "";
	for(int i = 0; i < N; ++i) {

		result = result + ele[i];

		result = combine(result, com);
		result = oppose(result, op);
	}

	if (result.length() > 0) {
		printf("%c", result[0]);
		for(int i = 1; i < result.length(); ++i) {
			printf(", %c", result[i]);
		}
	}
}

int main() {
	freopen("C:\\Users\\kiheon\\Downloads\\B-large.in", "r", stdin);
	freopen("C:\\workspace\\AOJ [C++]\\src\\output.txt", "w", stdout);
	int z;
	scanf("%d", &z);

	for (int i = 0; i < z; ++i) {
		printf("Case #%d: [", i + 1);
		solve();
		printf("]\n");
	}

	return 0;
}
