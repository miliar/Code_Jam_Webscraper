#include <iostream>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

namespace InputParser
{
	int readInt() {int N = -1; scanf("%d", &N); return N;}
	string readLine() {
		string result;
		char temp;
		while ((temp = getchar()) != '\n') result.push_back(temp);
		return result;
	}
};

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	string encrypt = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvzq ";
	string decrypt = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupqz ";
	map <char, char> M;
	for (int i = 0; i < encrypt.size(); ++i)
		if (M.find(encrypt[i]) == M.end()) M[encrypt[i]] = decrypt[i];
		else assert(M[encrypt[i]] == decrypt[i]);
	int nTestCases = InputParser::readInt(); getchar();
	for (int testCase = 1; testCase <= nTestCases; ++testCase) {
		string input = InputParser::readLine();
		for (int idx = 0; idx < input.size(); ++idx)
			input[idx] = M[input[idx]];
		printf("Case #%d: %s\n", testCase, input.c_str());
	}
	return 0;
}
