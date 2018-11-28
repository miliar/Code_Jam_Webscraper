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

int T;
char N[100];

void solve()
{

	fin >> N;
	bool flag = 1;
	for (int i = 0; i < (int)strlen(N) - 1; ++i)
		if (N[i] < N[i + 1]) flag = 0;
	if (flag)
	{
		sort(N, N + strlen(N));
		int i = 0;
		while (i < (int)strlen(N) && N[i] == '0') ++i;
		if (i == (int)strlen(N))
			fout << N[0] << "0" << N + 1 << endl;
		else
		{
			fout << N[i] << "0";
			for (int j = 0; j < i; ++j) fout << N[j];
			for (int j = i + 1; j < (int)strlen(N); ++j) fout << N[j];
			fout << endl;
		}
	}
	else
	{
		next_permutation(N, N + strlen(N));
		fout << N << endl;
	}

}

int main()
{
	fin >> T;
	for (int cas = 1; cas <= T; ++cas)
	{
		fout << "Case #" << cas << ": ";
		solve();
	}
	fin.close();
	fout.close();
	return 0;
}
