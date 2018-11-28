//Maked by diver_ru, maked with love^^
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>

#ifdef ONLINE_JUDGE
//#include <iostream>
FILE *fi = stdin, *fo = stdout;
#else
#include <fstream>

//std::ifstream cin("input.txt");
//std::ofstream cout("output.txt");
FILE *fi = fopen("input.txt", "r"), *fo = fopen("output.txt", "w");
#endif
using namespace std;

const int MAXN = 110;
const int MAXQ = 1010;
const int BIG = 1000000;

int s, q;
int answer;

string names[MAXN];
int state[MAXN];
int tab[MAXN];

string getLine()
{
	char buf[110];
	fgets(buf, 109, fi);
	string result = buf;
	if (result[result.length() - 1] == '\n')
		result.erase(result.length() - 1);
	return (result);
}

void readData()
{
	fscanf(fi, "%d\n", &s);
	for (int i = 1; i <= s; ++i)
		names[i] = getLine();
}

void solve()
{
	fscanf(fi, "%d\n", &q);
	memset(tab, 0, sizeof tab);
	string curName;
	memset(state, 0, sizeof state);
	for (int i = 1; i <= q; ++i){
		curName = getLine();
		for (int j = 1; j <= s; ++j){
			if (curName == names[j]){
				for (int k = 1; k <= s; ++k)
					if (k != j)
						tab[k] = min(tab[k], tab[j] + 1);
				tab[j] = BIG;
				break;
			}
		}
	}
	answer = BIG;
	for (int i = 1; i <= s; ++i)
		answer = min(answer, tab[i]);
}

void writeResult()
{
	fprintf(fo, "%d\n", answer);
}

int main()
{
	int n;
	fscanf(fi, "%d\n", &n);
	for (int i = 1; i <= n; ++i){
		readData();
		solve();
		fprintf(fo, "Case #%d: ", i);
		writeResult();
	}
	return 0;
}