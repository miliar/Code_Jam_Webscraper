//#pragma comment(linker,"/STACK:256000000")

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <cassert>
#include <string>

using namespace std;

#define ldb long double
#define lng long long
#define nextline {int c; while ((int c = getchar()) != 10 && c != EOF);}

#define PI 3.1415926535897932384626433832795
#define EPS 1e-12

#define sqr(x) ((x) * (x))
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)

#define all(a) a.begin(), a.end()
#define two(i) (1 << (i))
#define has(mask, i) ((((mask) & two(i)) == 0) ? false : true)

const int inf = 1000 * 1000 * 1000;
const lng inf64 = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;


#define MAXN 1000

vector <int> word;

int num[11];


void Load()
{
	string s;
	cin >> s;
	word.clear();
	memset(num, 0, sizeof(num));
	int i, x;
	for (i = 0; i < (int) s.size(); i++)
	{
		x = s[i] - 48;
		word.push_back(x);
		num[x]++;		
	}
}

void Solve()
{
	int i, j;
	if (next_permutation(all(word)))
	{
		for (i = 0; i < (int) word.size(); i++)		
			cout << word[i];
	}
	else
	{
		num[0]++;
		for (i = 1; i < 10; i++)	
			if (num[i] > 0)
			{
				cout << i;
				num[i]--;
				break; 
			}
		for (i = 0; i < 10; i++)
			for (j = 0; j < num[i]; j++)
				cout << i;
	}
}
                
int main()
{
	freopen(".in", "rt", stdin);
	freopen(".out", "wt", stdout);
	int t, i;
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		cout << "Case #"  << i << ": ";
		Load();
		Solve();
		cout << "\n";
	}
	return 0;
}
