#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

#define mset(c, val) memset((c), (val), sizeof((c)))
#define all(v) v.begin(), v.end()
#define INF 1000000000
#define EPS 1e-10

#define ADD 5000

typedef vector<int> vi;
typedef long long lint;

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int test, tnum;
	string s;

	void readdata()
	{
		s = "";
		int num;
		fin >> num;
		string inp;
		int t;
		char dir = 'U';
		for (int i = 0; i < num; i++) {
			fin >> inp >> t;
			for (int j = 0; j < t; j++) {
				for (int k = 0; k < inp.length(); k++) {
					if (inp[k] == 'F') {
						s += string(1, dir);
					}
					if (inp[k] == 'R') {
						switch(dir) {
							case 'U': dir = 'R'; break;
							case 'R': dir = 'D'; break;
							case 'D': dir = 'L'; break;
							case 'L': dir = 'U'; break;
						}
					}
					if (inp[k] == 'L') {
						switch(dir) {
							case 'U': dir = 'L'; break;
							case 'R': dir = 'U'; break;
							case 'D': dir = 'R'; break;
							case 'L': dir = 'D'; break;
						}
					}
				}
			}
		}
	}

	int limX[10000][2];

	void initlim()
	{
		for (int i = 0; i < 10000; i++) {
			limX[i][0] = 5000;
			limX[i][1] = -5000;
		}
	}

	void upd(int y, int x) {
		limX[y + ADD][0] = min(limX[y + ADD][0], x);
		limX[y + ADD][1] = max(limX[y + ADD][1], x);
	}

	int simple()
	{
		int res = 0;
		int x = 0, y = 0;
		for (int i = 0; i < s.length(); i++) {
			switch (s[i]) {
				case 'U':
					upd(y, x);
					y++;
					break;
				case 'D':
					y--;
					upd(y, x);
					break;
				case 'L': x--;
					res += y;
					break;
				case 'R': x++;
					res -= y;
					break;
			}
		}
		return abs(res);
	}

	int r1[10000][2];
	int r2[10000][2];

	int find_s2()
	{
		int l = 5000;
		int r = -5000;
		for (int i = 0; i < 10000; i++) {
			if (limX[i][0] == 5000) continue;
			l = min(l, limX[i][0]);
			r1[i][0] = l;
			r = max(r, limX[i][1]);
			r1[i][1] = r;
		}

		l = 5000;
		r = -5000;
		for (int i = 9999; i >= 0; i--) {
			if (limX[i][0] == 5000) continue;
			l = min(l, limX[i][0]);
			r2[i][0] = l;
			r = max(r, limX[i][1]);
			r2[i][1] = r;
		}

		int res = 0;
		for (int i = 0; i < 10000; i++) {
			if (limX[i][0] == 5000) continue;
			l = max(r1[i][0], r2[i][0]);
			r = min(r1[i][1], r2[i][1]);
			res += r - l;
		}
        
		return res;
	}

int main()
{
    fin >> tnum;
	for (test = 0; test < tnum; test++) {
		readdata();
		initlim();
		int s1 = simple();
		int s2 = find_s2();

		fout << "Case #" << (test + 1) << ": " << (s2 - s1) << endl;
	}
	return 0;
}
