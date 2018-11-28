#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <ctime>
#include <cmath>
#include <stdio.h>
#include <set>
#include <map>
#include <stack>
#include <fstream>
#include <list>

#define SZ(a) (int(a.size()))
#define MEM(a, val) memset(a, val, sizeof(a))
#define MP(a, b) make_pair(a, b)
#define PB(a) push_back(a)

using namespace std;

typedef unsigned long long ULL;
typedef long long LL;
typedef long double dbl;
typedef pair<int, int> pii;
typedef vector<int> vint;

#define char unsigned char

string s;
//set< pair<char, char>  > M;
map<char, char> F;

int mat[256][256];
vector<char> TO;
int start, finish;
int ANS;

vector<char> cl;
vector<int> p;
int cycle_st, cycle_end;

bool dfs (int v) {
	cl[v] = 1;
	for (int i = 0; i < SZ(TO); ++i) {
		int to = TO[i];
		if (mat[v][to] == -1) {
			if (cl[to] == 0) {
				p[to] = v;
				if (dfs (to))  return true;
			}
			else if (cl[to] == 1) {
				cycle_end = v;
				cycle_st = to;
				return true;
			}
		}
	}
	cl[v] = 2;
	return false;
}

int in[256];
int out[256];

bool was[256];
void del_circles() {
	int n = 256;
	bool flag = true;
	while (flag) {
		flag = false;
		for (int i=0; i<SZ(TO); ++i){
			p.clear();
			p.assign (256, -1);
			cl.clear();
			cl.assign (256, 0);
			cycle_st = -1;
			if (dfs (TO[i])) {
				flag = true;
				//delete
				vector<int> cycle;
				cycle.push_back (cycle_st);
				for (int v=cycle_end; v!=cycle_st; v=p[v])
					cycle.push_back (v);
				cycle.push_back (cycle_st);
				ANS += SZ(cycle) - 1;
				reverse (cycle.begin(), cycle.end());
				int add = 1;
				for (int i=0; i<int(cycle.size()) - 1; ++i) {
					//printf ("%d ", cycle[i]+1);
					mat[cycle[i]][cycle[i + 1]] = 0;
					out[cycle[i]]--;
					in[cycle[i + 1]]--;
				}
				/*for (int i=0; i<int(cycle.size()) - 1; ++i) {
					if (in[cycle[i]] > 0 || was[i] == true)
						add = 0;
					was[i] = true;
				}
				ANS += add;*/
				//end delete
	
				break;
			}
		}
	}

}


int dfs_my(int v) {
	for (int i = 0; i < SZ(TO); ++i) {
		int to = TO[i];
		if (mat[v][to] == -1) {
			mat[v][to] = 0;
			out[v]--;
			in[to]--;
			return dfs_my(to) + 1;
		}
	}
	return 0;
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	start = 0;
	finish = 255;
	TO.PB(start);
	TO.PB(finish);
	for (char ch = 'a'; ch <= 'z'; ++ch)
		TO.PB(ch);
	TO.PB('0');
	F['o'] = '0';
	F['i'] = '1';
	TO.PB('1');
	F['e'] = '3';
	TO.PB('3');
	F['a'] = '4';
	TO.PB('4');
	F['s'] = '5';
	TO.PB('5');
	F['t'] = '7';
	TO.PB('7');
	F['b'] = '8';
	TO.PB('8');
	F['g'] = '9';
	TO.PB('9');
	int T;
	cin >> T;
	
	for (int I = 1; I <= T; ++I) {
		int kk;
		cin >> kk;
		ANS = 0;
		cin >> s;
		MEM(mat, 0);
		for (int i = 0; i < SZ(s) - 1; ++i) {
			//M.insert(MP(s[i], s[i + 1]));
			mat[s[i]][s[i + 1]] = -1;
			if (F.find(s[i]) != F.end()) {
				//M.insert(MP(F[s[i]], s[i + 1]));
				mat[F[s[i]]][s[i + 1]] = -1;
			}
			if (F.find(s[i + 1]) != F.end())  {
				//M.insert(MP(s[i], F[s[i + 1]]));
				mat[s[i]][F[s[i + 1]]] = -1;
			}
			if (F.find(s[i]) != F.end() && F.find(s[i + 1]) != F.end())  {
				//M.insert(MP(F[s[i]], F[s[i + 1]]));
				mat[F[s[i]]][F[s[i + 1]]] = -1;
			}
		}
		
		MEM(in, 0);
		MEM(out, 0);
		MEM(was, false);
		for (int i = 0; i < 256; ++i) {
			for (int j = 0; j < 256; ++j) {
				if (mat[i][j] == -1) {
					in[j]++;
					out[i]++;
				}
			}
		}

		del_circles();

		
		
		bool flag = true;
		int add = 1;
		while(flag) {
			flag = false;
			for (int i = 0; i < SZ(TO); ++i) {
				int v = TO[i];
				if (in[v] == 0 && out[v] > 0) {
					ANS += dfs_my(v) + 1;
					flag = true;
					add = 0;
					break;
				}
			}
		}
		ANS += add;
		printf("Case #%d: %d\n", I, ANS);
	}
	return 0;
}
