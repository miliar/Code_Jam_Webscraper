#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <string.h>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef unsigned long long ULL;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))

int T, W, H;

#define MAX_W 50
#define MAX_H 50
char TABLE[MAX_W][MAX_H];
bool END;

bool isEnd(char* org)
{
	char table[MAX_W][MAX_H];
	memcpy(&table[0][0], org, sizeof(table));

	int x, y;
	REP(y, H){
		REP(x, W){
			if(table[x][y] == '#')
			{
				return false;
			}
		}
	}
	return true;
}

void solve(char* org)
{
	if(END)
	{
		return;
	}

	if(isEnd(org))
	{
		memcpy(&TABLE[0][0], org, sizeof(TABLE));
		END = true;
		return;
	}

	char table[MAX_W][MAX_H];
	memcpy(&table[0][0], org, sizeof(table));

	int x, y;
	REP(y, H){
		REP(x, W){
			if(table[x][y]=='#' &&
			   table[x+1][y]=='#' && 
			   table[x][y+1]=='#' &&
			   table[x+1][y+1]=='#')
			{
				table[x][y] = '/';
				table[x+1][y] = '\\';
				table[x][y+1] = '\\';
				table[x+1][y+1] = '/';
				solve(&table[0][0]);
				memcpy(&table[0][0], org, sizeof(table));
			}
		}
	}
}

int main()
{
	int t, i, j, k;
	string line;
	ifstream in("input.txt", ios::in);
	FILE* out = fopen("output.txt", "w");

	in >> T;
	REP(t, T){
		fprintf(out, "Case #%d:\n", t+1);

		CL(TABLE, 0);
		in >> H >> W;
		REP(j, H){
			in >> line;
			REP(i, W){
				TABLE[i][j] = line[i];
			}
		}
		
		END = false;
		solve(&TABLE[0][0]);

		if(END)
		{
			REP(j, H){
				REP(i, W){
					fprintf(out, "%c", TABLE[i][j]);
				}
				fprintf(out, "\n");
			}
		}
		else
		{
			fprintf(out, "Impossible\n");
		}
	}
	fclose(out);
}