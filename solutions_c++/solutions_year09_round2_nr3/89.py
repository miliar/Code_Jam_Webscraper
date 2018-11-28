#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <ctime>

#define MAX 20
#define SUM 32768
#define PLUS 10
#define MINUS 11

using namespace std;
FILE *in; FILE *out;

int n, numq;
int a[MAX][MAX];
char vis[MAX][MAX][SUM];
int dir[4][2] = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };

struct State
{
	int row, col, val;
	string exp;
	
	bool operator < (const State& r) const
	{
		if (exp.size() != r.exp.size()) return exp.size() > r.exp.size();
		if (exp != r.exp) return exp > r.exp;

		if (val != r.val) return val < r.val;
		if (row != r.row) return row < r.row;
		return col < r.col;
	}
};
priority_queue <State> q;


string query(int sum)
{
	State cur, next;

	memset(vis, 0, sizeof(vis));
	while (!q.empty()) q.pop();
	
	for (int i=0; i<n; i++)
	{
		for (int c=0; c<n; c++) if (a[i][c] < 10)
		{
			next.row = i; next.col = c;
			next.val = a[i][c] + SUM / 2;
			next.exp = (char)(a[i][c] + '0');
			q.push(next);
		}
	}
	
	while(!q.empty())
	{
		cur = q.top(); q.pop();
		
		if (vis[cur.row][cur.col][cur.val]) continue;
		else
			vis[cur.row][cur.col][cur.val] = 1;
		
		if (cur.val - SUM / 2 == sum) return cur.exp;
		
		for (int i=0; i<4; i++)
		{
			next.row = cur.row + dir[i][0]; if (next.row < 0 || next.row >= n) continue;
			next.col = cur.col + dir[i][1]; if (next.col < 0 || next.col >= n) continue;
			
			next.val = cur.val;
			if (a[cur.row][cur.col] == 10) next.val += a[next.row][next.col];
			if (a[cur.row][cur.col] == 11) next.val -= a[next.row][next.col];
			if (next.val < 0 || next.val >= SUM) continue;
			if (vis[next.row][next.col][next.val]) continue;
			next.exp = cur.exp;
			if (a[next.row][next.col] == 10) next.exp += '+';
			if (a[next.row][next.col] == 11) next.exp += '-';
			if (a[next.row][next.col] < 10) next.exp += (char)(a[next.row][next.col] + '0');
			
			q.push(next);
		}
	}
	return "ERROR";
}

void doWork(int testNum)
{
	char temp[32];
	fscanf(in, "%d %d", &n, &numq);
	
	for (int i=0; i<n; i++)
	{
		fscanf(in, "%s", temp);
		for (int c=0; c<n; c++)
			a[i][c] = isdigit(temp[c]) ? temp[c] - '0' : (temp[c] == '+' ? PLUS : MINUS);
	}
	
	for (int i=0; i<numq; i++)
	{
		int sum;
		fscanf(in, "%d", &sum);
		
		string ans = query(sum);
		fprintf(out, "%s\n", ans.c_str());
	}
	
	return;
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("SquareMath.in", "rt");
	out = fopen("SquareMath.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++)
	{
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d:\n", test);
		doWork(test);
	}
	
	fprintf(stderr, "Total execution time %.3lf seconds.\n", (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	system("pause");
	return 0;
}
