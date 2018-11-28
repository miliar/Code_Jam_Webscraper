// Hexagon.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<LL> VL;
#define FORE(it, c, T) for(T::iterator it = c.begin(); it != c.end(); it++)
#define FORI(i, n) for(int i = 0; i < (n); i++)
#define FORIS(i, s, n) for(int i = (s); i < (n); i++)
#define CLEAR(a, n) memset(a, n, sizeof(a))
#define PB(n) push_back(n)
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(), (c).end()

#define NUM 110

int cts[NUM][NUM][NUM];
VI task;

int T, N;

int dp(int pos1, int pos2, int t_pos);

int main(int argc, char* argv[])
{
#define TASK_NAME(file) "A"file
#define FOLDER(file) "c:\\Projects\\coding\\cj\\2011\\QualificationRound\\"TASK_NAME("")"\\"file
//	ifstream in(FOLDER(TASK_NAME("-test.in")));
//	ofstream out(FOLDER(TASK_NAME("-test.out")));
//	ifstream in(FOLDER(TASK_NAME("-small-attempt0.in")));
//	ofstream out(FOLDER(TASK_NAME("-small-attempt0.out")));
	ifstream in(FOLDER(TASK_NAME("-large.in")));
	ofstream out(FOLDER(TASK_NAME("-large.out")));

	in >> T;
	FORI(ncase, T) {
		in >> N;
		task.clear();
		FORI(i, N) {
			char col;
			int n;
			in >> col >> n;
			if(col == 'O')
				n += 1000;
			else 
				n += 2000;
			task.PB(n);
		}
		CLEAR(cts, -1);
		int res = dp(1, 1, 0);
		out << "Case #" << (ncase+1) << ": " << res << endl;
	}
	return 0;
}

int dp(int pos1, int pos2, int t_pos) {
	int &res = cts[pos1][pos2][t_pos];
	if(res > -1) return res;
	if(t_pos >= N) return res = 0;
	int n = task[t_pos]%1000;
	char c = task[t_pos]>=2000?'B':'O';
	if(c == 'O' && pos1 == n){
		res = dp(pos1, pos2, t_pos+1);
		if(pos2 < 100)
			res = min(res, dp(pos1, pos2+1, t_pos+1));
		if(pos2 > 1)
			res = min(res, dp(pos1, pos2-1, t_pos+1));
		return res = res+1;
	}
	if(c == 'B' && pos2 == n) {
		res = dp(pos1, pos2, t_pos+1);
		if(pos1 < 100)
			res = min(res, dp(pos1+1, pos2, t_pos+1));
		if(pos1 > 1)
			res = min(res, dp(pos1-1, pos2, t_pos+1));
		return res = res+1;
	}
	if(c == 'O') {
		int pos1n = pos1;
		if(pos1 < n) pos1n++;
		else pos1n--;

		res = dp(pos1n, pos2, t_pos);
		if(pos2 < 100)
			res = min(res, dp(pos1n, pos2+1, t_pos));
		if(pos2 > 1)
			res = min(res, dp(pos1n, pos2-1, t_pos));
	} else {
		int pos2n = pos2;
		if(pos2 < n) pos2n++;
		else pos2n--;

		res = dp(pos1, pos2n, t_pos);
		if(pos1 < 100)
			res = min(res, dp(pos1+1, pos2n, t_pos));
		if(pos1 > 1)
			res = min(res, dp(pos1-1, pos2n, t_pos));
	}
	res = res+1;
	return res;
}
