#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <stack>
#include <string.h>
#include <list>
#include <assert.h>

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define PI 3.14159265358979
#define forn(i, n) for(int i = 0; i < n; ++i)
#define ALL(x) x.begin(), x.end()
#define L(s) (int)((s).size())
#define ms(x) memset(x,0,sizeof(x))
#define ms1(x) memset(x,-1,sizeof(x))
#define del(y,x) erase(y.begin()+x)

typedef long long ll;
using namespace std;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;
const int ST = 100010;
const int ST1 = 1000010;
const ll MOD = 1000000007;

ll ABS(ll a)
{
    if(a<0)
        return a*(-1);
    else
        return a;
}



int main()
{
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	int cur = 1;
	while(T)
	{
		vector<string> mas;
		for(int i = 0;i < 4;i++)
		{
			string a;
			cin >> a;
			mas.pb(a);
		}
		bool win1 = false;
		bool win2 = false;
		for(int i = 0;i < 4;i++)
		{
			int j;
			for(j = 0;j < 4;j++)
			{
				if(mas[i][j]!= 'X' && mas[i][j]!='T')
					break;
			}
			if(j == 4)
				win1 = true;
		}
		for(int j = 0;j < 4;j++)
		{
			int i;
			for(i = 0;i < 4;i++)
			{
				if(mas[i][j]!='X' && mas[i][j]!='T')
					break;
			}
			if(i == 4)
				win1 = true;
		}
		int t = 0;
		for(t = 0;t < 4;t++)
		{
			if(mas[t][t]!='X' && mas[t][t]!='T')
				break;
		}
		if(t == 4)
			win1 = true;


		for(t = 0;t < 4;t++)
		{
			if(mas[t][4-t-1] != 'X' && mas[t][4-t-1]!='T')
				break;
		}
		if(t == 4)
			win1 = true;

		for(int i = 0;i < 4;i++)
		{
			int j;
			for(j = 0;j < 4;j++)
			{
				if(mas[i][j]!= 'O' && mas[i][j]!='T')
					break;
			}
			if(j == 4)
				win2 = true;
		}
		for(int j = 0;j < 4;j++)
		{
			int i;
			for(i = 0;i < 4;i++)
			{
				if(mas[i][j]!='O' && mas[i][j]!='T')
					break;
			}
			if(i == 4)
				win2 = true;
		}
		t = 0;
		for(t = 0;t < 4;t++)
		{
			if(mas[t][t]!='O' && mas[t][t]!='T')
				break;
		}
		if(t == 4)
			win2 = true;

		for(t = 0;t < 4;t++)
		{
			if(mas[t][4-t-1] != 'O' && mas[t][4-t-1]!='T')
				break;
		}
		if(t == 4)
			win2 = true;

		bool fin = true;
		for(int i = 0;i < 4;i++)
			for(int j = 0;j < 4;j++)
				if(mas[i][j] == '.')
					fin = false;
		printf("Case #%d: ",cur);
		if(win1 && win2)
		{
			cout << "Draw" << endl;
		}
		else
		{
			if(win1)
			{
				cout << "X won" << endl;
			}
			else
				if(win2)
				{
					cout << "O won" << endl;
				}
				else
					if(!fin)
					{
						cout << "Game has not completed" << endl;
					}
					else
						cout << "Draw" << endl;
		}

		T--;
		cur++;
	}

    return 0;
}