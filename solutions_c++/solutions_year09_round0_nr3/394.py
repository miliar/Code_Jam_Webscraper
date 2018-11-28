#include <iostream>
#include <algorithm>
#include <fstream>
#include <queue>
#include <string>
using namespace std;

const int L = 19;
const int N = 501;
const char MSG[L+1] = "welcome to code jam";
int memo[L][N];

int solve(const string &msg, const int p, const int msgPos)
{
	if (p==L) return 1;
	if (msgPos==msg.length()) return 0;
	if (memo[p][msgPos] != -1) return memo[p][msgPos];

	int res = 0;
	if (msg[msgPos]==MSG[p]) {
		res += solve(msg, p+1, msgPos+1);
	}
	res += solve(msg, p, msgPos+1);

	return memo[p][msgPos] = res%10000;
}

int main()
{
	fstream fout("out.txt");
	fstream fin("in.txt");

	int T;
	fin>>T;
	string dum;
	getline(fin, dum);
	for (int q=0; q < T; ++q) {
		string msg;
		getline(fin, msg);
		fill(&memo[0][0], &memo[L-1][N], -1);
		printf("Case #%d: %04d\n", q+1, solve(msg, 0, 0));
	}

	fout.close();
	fin.close();

	return 0;
}