#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <list>
#include <cassert>
#include <conio.h>
using namespace std; 

#define PB push_back 
#define MP make_pair 
#define SZ(v) ((int)(v).size()) 
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n) 
#define FORE(i,a,b) for(int i=(a);i<=(b);++i) 
#define REPE(i,n) FORE(i,0,n) 
#define FORSZ(i,a,v) FOR(i,a,SZ(v)) 
#define REPSZ(i,v) REP(i,SZ(v)) 
typedef long long ll; 

int table[100][100];
double exwp[100][100];
double countr[100], wins[100];
double wp[100], owp[100], oowp[100];

int main() {
	freopen("..\\..\\IO Files\\A-large.in", "r", stdin);
	freopen("..\\..\\IO Files\\A-large.out", "w", stdout);

	//freopen("..\\..\\IO Files\\testA.in", "r", stdin);


	int T, N;
	cin >> T;
	REP(i, T)
	{
		memset(table, 0, sizeof(int)*10000);
		memset(exwp, 0, sizeof(double)*10000);
		memset(countr, 0, sizeof(double)*100);
		memset(wins, 0, sizeof(double)*100);
		memset(wp, 0, sizeof(double)*100);
		memset(owp, 0, sizeof(double)*100);
		memset(oowp, 0, sizeof(double)*100);


		cin >> N;

		FOR(row, 0, N)
		{
			int c = 0, w = 0;
			FOR(col, 0, N)
			{
				char ch;
				cin >> ch;
				if (ch == '1') 
				{
					table[row][col] = 1;
					c++; w++;
				}
				else if (ch == '0') 
				{
					table[row][col] == 0;
					c++;
				}
				else table[row][col] = 2;
			}

			wins[row] = double(w);
			countr[row] = double(c);
			wp[row] = double(w)/c;
		}

		FOR(row, 0, N)
			FOR(col, 0, N)
			{
				if (table[row][col] == 2)
					exwp[row][col] = wp[row];
				else if (table[row][col] == 1)
					exwp[row][col] = (wins[row]-1)/(countr[row]-1);
				else
					exwp[row][col] = wins[row]/(countr[row]-1);
			}

		FOR(row, 0, N)
		{
			int cnt = 0;
			double sum = 0;
			FOR(col, 0, N)
			{
				if (table[row][col] != 2)
				{
					++cnt;
					sum += exwp[col][row];
				}
			}
			owp[row] = sum/cnt;
		}

		FOR(row, 0, N)
		{
			int cnt = 0;
			double sum = 0;
			FOR(col, 0, N)
			{
				if (table[row][col] != 2)
				{
					++cnt;
					sum += owp[col];
				}
			}
			oowp[row] = sum/cnt;
		}

		cout.precision(12);
		cout << "Case #" << i+1 << ": " << endl;
		FOR(row, 0, N)
		{
			double rpi = 0.25*wp[row] + 0.5*owp[row] + 0.25*oowp[row];
			cout << rpi << endl;
		}
	}

	fclose(stdout);
	//getch();
	return 0;
}