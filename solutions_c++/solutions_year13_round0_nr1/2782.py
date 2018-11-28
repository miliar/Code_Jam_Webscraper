#include <algorithm>
#include <numeric>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <stack>

using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORE(i,n) for (int i=0; i<=n; ++i)
#define REP(i,a,b) for (int i=a; i<b; ++i)
#define REPE(i,a,b) for (int i=a; i<=b; ++i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define mp make_pair
#define INF (1e9)

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<VI> VVI;
const double pi = acos(-1.0);
const int inf =(int) 1e9;

const double eps = 1e-4;
const int ss=(int)1e6+3;
const int base=inf;

bool pred (const pair<int,int>& i, const pair<int,int>& j) 
{
    if (i.first==j.first)
        return i.second>j.second;
    else
        return i.first>j.first;
}

int main()
{
#ifdef _DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#else
	//freopen("island2.in","r",stdin);
   //freopen("island2.out","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	cin.get();
	FOR(z,t)
	{
		printf("Case #%d: ",z + 1);
		vector<string> s(4);
		bool point = false;
		FOR(i,4)
		{
			cin>>s[i];
			FOR(j,4) {
				if (s[i][j] == '.')
					point = true;
			}
		}
		//diagonal
		bool ans1 = true;
		bool ans2 = true;
		bool ans3 = true;
		bool ans4 = true;
		FOR(i,4)
		{
			if (s[i][i] != 'X' && s[i][i] != 'T') {
				ans1 = false; 
			}
			if (s[i][3-i] != 'X' && s[i][3-i] != 'T') {
				ans2 = false; 
			}
			if (s[i][i] != 'O' && s[i][i] != 'T') {
				ans3 = false; 
			}
			if (s[i][3-i] != 'O' && s[i][3-i] != 'T') {
				ans4 = false; 
			}
		}
		if (ans1 || ans2) {
			printf("X won\n");
			continue;
		}
		if (ans3 || ans4) {
			printf("O won\n");
			continue;
		}
		//lines
		bool result = false;
		FOR(i,4)
		{
			ans1 = true;
			ans2 = true;
			REP(j,0,4) {
				if (s[i][j] != 'X' && s[i][j] != 'T') {
					ans1 = false; 
				}
				if (s[j][i] != 'X' && s[j][i] != 'T') {
					ans2 = false; 
				}
			}
			if (ans1 || ans2) {
				result = true;
				printf("X won\n");
				break;
			}
			ans1 = true;
			ans2 = true;
			REP(j,0,4) {
				if (s[i][j] != 'O' && s[i][j] != 'T') {
					ans1 = false; 
				}
				if (s[j][i] != 'O' && s[j][i] != 'T') {
					ans2 = false; 
				}
			}
			if (ans1 || ans2) {
				result = true;
				printf("O won\n");
				break;
			}
		}
		if (!result) {
			if (point) {
				printf("Game has not completed\n");
			} else {
				printf("Draw\n");
			}
		}
	}
#ifdef _DEBUG
    fprintf(stderr, "Time: %.2lf sec\n", (clock()*1./CLOCKS_PER_SEC));
#endif
    return 0;
}

