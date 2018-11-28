#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <list>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>

using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

int T, L, A, K, N;
double value[100000];
int lc[100000],rc[100000];
string have[100000], feature[100000];
string S;

int split(string str)
{
	int tot = 1;
	for (int i = 1; i < (int)str.length(); ++i)
	{
		if (str[i] == '(') ++tot;
		if (str[i] == ')') --tot;
		if (tot == 0) return i;
	}
	return -1;
}

int build(string str)
{
	++N;
	int M = N;
	istringstream iss(str);
	char temp;

	iss >> temp >> value[N];
	iss >> temp;
	if (temp == ')')
	{
		lc[N] = rc[N] = -1;
		return N;
	}
	feature[N] = "";

	while (temp >= 'a' && temp <= 'z')
	{
		feature[N] += temp;
		iss >> temp;
	}
	string remain;
	getline(iss, remain);
	remain = '(' + remain;
	int p = split(remain);
	lc[M] = build(remain.substr(0, p + 1));
	rc[M] = build(remain.substr(p + 1, remain.length() - 1 - p));
	return M;
}

bool lookup(string x)
{
	for (int i = 0; i < K; ++i)
		if (x == have[i]) return 1;
	return 0;
}

double cal(int x)
{
	double ret = value[x];
	if (lc[x] == -1) return ret;
	if (lookup(feature[x]))
		return ret * cal(lc[x]);
	else
		return ret * cal(rc[x]);
}

void solve()
{
	fin >> L;
	string junk;
	getline(fin, junk);
	S = "";
	for (int i = 0; i < L; ++i)
	{
		string temp;
		getline(fin, temp);
		S += " " + temp;
	}

	N = 0;
	build(S);
	cout << lc[1] << " " << rc[1] << endl;
	fin >> A;
	for (int i = 0; i < A; ++i)
	{
		string junk;
		fin >> junk >> K;
		cout << K << endl;

		for (int j = 0; j < K; ++j)
			fin >> have[j];
		fout << fixed << setprecision(7) << cal(1) << endl;
	}
}

int main()
{
	fin >> T;
	for (int cas = 1; cas <= T; ++cas)
	{
		fout << "Case #" << cas << ": " << endl;
		solve();
	}
	fin.close();
	fout.close();
	return 0;
}
