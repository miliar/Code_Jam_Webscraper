#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1 << 29;
typedef long long ll;

/*class 
{
private:
	
public:
	
};*/

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=last_bit(n); return res; }

///////////////////////////////////////////////////////////////////////////////////////////////////////////////

const int dr[] = {-1, 0, 1, 0};
const int dc[] = {0, 1, 0, -1};

ifstream fin("vstup.txt");
//FILE * fout = fopen("vystup.txt", "w");
ofstream fout("vystup.txt");

string board[20];

struct State
{
	State(): number(0) { }

	int number;
	string expr;

	bool operator<(const State & s) const { return number < s.number; }
};

set<int> used[20][20];
set<State> dp[2][20][20];
string expr[251];

bool cmps(const string & str1, const string & str2) //ci je 1 < 2
{
	if (str1.size() < str2.size()) return true;
	if (str1.size() > str2.size()) return false;

	int index = 0;
	while (index < str1.size() && str1[index] == str2[index]) ++index;
	if (index == str1.size()) return false;
	return str1[index] < str2[index];
}

void solve(int T)
{
	int W, Q;
	fin >> W >> Q;

	FOR(i, 0, W) fin >> board[i];

	//vynuluje polia
	FOR(i, 0, W)
		FOR(j, 0, W)
		{
			used[i][j].clear();
			FOR(k, 0, 2) dp[k][i][j].clear();
		}
	FOR(i, 0, 250) expr[i].clear();

	//inicializacia
	FOR(i, 0, W)
		FOR(j, 0, W)
		{
			if (isdigit(board[i][j]))
			{
				State temp;
				temp.number = board[i][j]-'0';
				temp.expr = board[i][j];
				expr[board[i][j]-'0'] = temp.expr;
				dp[1][i][j].insert(temp);
			}
		}

	//spusti dynamiku
	int act = 1; //0 -> cita '+'/'-' a zapisuje do cisel
	FOR(step, 0, 100)
	{
		if (act == 0)
		{
			FOR(i, 0, W)
				FOR(j, 0, W)
					if (board[i][j] == '+' || board[i][j] == '-') 
					{
						//pre kazdy stav, ktory ma ulozeny
						for (set<State>::iterator iter = dp[act][i][j].begin(); iter != dp[act][i][j].end(); ++iter)
						{
							used[i][j].insert(iter->number);
							//do kazdeho smeru
							FOR(d, 0, 4)
							{
								int ii = i+dr[d], jj = j+dc[d];
								if (ii < 0 || ii >= W || jj < 0 || jj >= W) continue;

								int n = iter->number;
								n += (board[i][j]=='+'?1:-1) * (board[ii][jj]-'0');
								if (used[ii][jj].find(n) != used[ii][jj].end()) //cislo tu uz pouzite bolo
									continue;

								State temp;
								temp.number = n;
								set<State>::iterator iter2 = dp[1-act][ii][jj].find(temp);
								temp.expr = iter->expr + board[ii][jj];

								if (iter2 == dp[1-act][ii][jj].end()) //este tam dp stav nie je			
								{
									dp[1-act][ii][jj].insert(temp);
									if (temp.number >= 1 && temp.number <= 250 && (expr[temp.number] == "" || cmps(temp.expr, expr[temp.number])))
										expr[temp.number] = temp.expr;
								}
								else if (cmps(temp.expr, iter2->expr)) //inak porovna vyrazy
								{
									iter2->expr = temp.expr;
									if (temp.number >= 1 && temp.number <= 250 && (expr[temp.number] == "" || cmps(temp.expr, expr[temp.number])))
										expr[temp.number] = temp.expr;
								}
							}
						}
						dp[act][i][j].clear();
					}
		}
		else
		{
			FOR(i, 0, W)
				FOR(j, 0, W)
					if (isdigit(board[i][j]))
					{
						//pre kazdy stav, ktory ma ulozeny
						for (set<State>::iterator iter = dp[act][i][j].begin(); iter != dp[act][i][j].end(); ++iter)
						{
							used[i][j].insert(iter->number);
							//do kazdeho smeru
							FOR(d, 0, 4)
							{
								int ii = i+dr[d], jj = j+dc[d];
								if (ii < 0 || ii >= W || jj < 0 || jj >= W) continue;

								int n = iter->number;
								if (used[ii][jj].find(n) != used[ii][jj].end()) //cislo tu uz pouzite bolo
									continue;

								State temp;
								temp.number = n;
								set<State>::iterator iter2 = dp[1-act][ii][jj].find(temp);
								temp.expr = iter->expr + board[ii][jj];

								if (iter2 == dp[1-act][ii][jj].end()) //este tam dp stav nie je		
									dp[1-act][ii][jj].insert(temp);
								else if (cmps(temp.expr, iter2->expr)) //inak porovna vyrazy
									iter2->expr = temp.expr;
							}
						}
						dp[act][i][j].clear();
					}
		}

		act = 1-act;
	}

	fout << "Case #" << T << ":" << endl;
	FOR(step, 0, Q)
	{
		int N;
		fin >> N;

		if (expr[N] == "") cout << "CHYBA" << endl;
		fout << expr[N] << endl;
	}
}

int main()
{
	int N;

	fin >> N;
	FOR(step, 0, N)
		solve(step+1);

	return 0;
}
