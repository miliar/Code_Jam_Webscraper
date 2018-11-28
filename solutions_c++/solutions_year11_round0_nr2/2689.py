#include <iostream>
#include <algorithm>
#include <queue>
#include <fstream>
#include <string>
using namespace std;

const int N = 50;
char conbine[N][N];
bool oppose[N][N];

void solve(const string &s, vector<int> &ans)
{
	ans.clear();
	for (int q=0; q < s.length(); ++q) {
		const int now = s[q]-'A';
		ans.push_back(now);

		while (ans.size() >= 2) {
			const int t1 = ans[ans.size()-1];
			const int t2 = ans[ans.size()-2];
			if (conbine[t1][t2] != -1) {
				ans.erase(ans.begin()+ans.size()-2, ans.end());
				ans.push_back(conbine[t1][t2]);
			}
			else break;
		}

		bool isClear = false;
		for (int i=0; i < ans.size(); ++i) {
			for (int j=i+1; j < ans.size(); ++j) {
				if (oppose[ans[i]][ans[j]]) {
					isClear = true;
				}
			}
		}
		if (isClear) {
			ans.clear();
		}
	}
}

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("out.txt");

	int caseNo = 0;
	int cn;
	for (fin>>cn; cn>0; --cn) {

		fill(&conbine[0][0], &conbine[N-1][N], -1);
		fill(&oppose[0][0], &oppose[N-1][N], false);

		int c;
		fin >> c;
		for (int i=0; i < c; ++i) {
			char a, b, t;
			fin >> a >> b >> t;
			conbine[a-'A'][b-'A'] = t-'A';
			conbine[b-'A'][a-'A'] = t-'A';
		}
		int d;
		fin >> d;
		for (int i=0; i < d; ++i) {
			char a, b;
			fin >> a >> b;
			oppose[a-'A'][b-'A'] = true;
			oppose[b-'A'][a-'A'] = true;
		}

		int n;
		fin >> n;
		string s;
		fin >> s;

		vector<int> ans;
		solve(s, ans);
		fout << "Case #" << ++caseNo << ": [";
		for (int i=0; i < ans.size(); ++i) {
			if (i) fout << ", ";
			fout << (char)(ans[i]+'A');
		}
		fout << "]" << endl;
	}

	fin.close();
	fout.close();

	return 0;
}
