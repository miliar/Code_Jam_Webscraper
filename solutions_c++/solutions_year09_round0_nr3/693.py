#include <iostream>
#include <algorithm>
#include <fstream>
#include <queue>
#include <string>

using namespace std;

string all = "welcome to code jam";
string s;
int Memo[600][20];
int Ret = 0, ls;

bool Pos(char A, char B, int f) {
	if (all[f] == A && all[f+1] == B)
		return true;
	return false;
}

int DFS(int id, int la) {
	if (la == 18)
		return 1;
	if (Memo[id][la] != -1)
		return Memo[id][la];
	Memo[id][la] = 0;
	for (int j=id+1;j<ls;j++) {
		if (Pos(s[id], s[j], la)) {
			Memo[id][la] = (Memo[id][la]+DFS(j, la+1))%10000;
		}
	}
	return Memo[id][la];
}

string tos(int n) {
	string Rt;
	while (n) {
		Rt += n%10+'0';
		n /= 10;
	}
	reverse(Rt.begin(), Rt.end());
	while (Rt.size() < 4)
		Rt.insert(Rt.begin(), '0');
	return Rt;
}

int main() {
	ifstream fin("C-large.in");
	ofstream fout("wtcj1.out");
	fin.sync_with_stdio(false);
	fout.sync_with_stdio(false);
	int n;
	fin >> n;
	for (int i=0;i<=n;i++) {
		for (int j=0;j<600;j++) {
			for (int k=0;k<20;k++) {
				Memo[j][k] = -1;
			}
		}
		getline(fin, s);
		ls = s.size();
		if (!i)
			continue;
		Ret = 0;
		for (int j=0;j<ls;j++) {
			if (s[j] == 'w') {
				Ret = (Ret+DFS(j, 0))%10000;
			}
		}
		fout << "Case #" << i << ": " << tos(Ret) << endl;
	}
	return 0;
}