#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <set>
#include <math.h>
#include <map>
#include <list>
#include <queue>
#include <algorithm>
#include <fstream>
#include <cstdio>

using namespace std;

typedef vector <int> VI;
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPV(i, a, b) for (int i = (a); i <= (b); ++i)
#define PB push_back
#define ALL(x) x.begin(),x.end()

char strin[10000];
int siz;
long long rez;
string S;
char op[40];

void calc();
void genop(int j);
bool ugly(int s);

void genop(int j)
{
	if (j < siz)
	{
		op[j] = '+';
		genop(j+1);
		op[j] = '-';
		genop(j+1);
		op[j] = '*';
		genop(j+1);
	}
	else
	{
		calc();
	}
}

bool ugly(long long s)
{
	if ((s % 2 == 0) || (s % 3 == 0) || (s % 5 == 0) || (s % 7 == 0)) return true;
	else return false;
}

void calc()
{
	long long s = 0, temp = S[0]-'0';
	bool plus = true;
		
	for (int i = 0; i < S.size()-1; i++)
	{
		if (op[i] == '+') {
			if (plus) s += temp;
			else s -= temp;
			plus = true;
			temp = S[i+1]-'0';
		}
		else if (op[i] == '-') {
			if (plus) s += temp;
			else s -= temp;
			plus = false;
			temp = S[i+1]-'0';
		}
		else if (op[i] == '*') {
			temp *= 10;
			temp += S[i+1] - '0';
		}
	}
	if (plus) s += temp;
	else s -= temp;
	if (ugly(s)) rez++;
}

int main()
{
	int T, j;
	freopen("B_small.txt", "rt", stdin);
	ofstream out("B_small.out");
	gets(strin);
	sscanf(strin, "%d", &T);
	for (j = 1; j <= T; j++) {
		gets(strin);
		S = (string) strin;
		siz = S.size()-1;
		rez = 0;
		genop(0);
		out << "Case #" << j << ": " << rez << endl;
	}
	return 0;
}
