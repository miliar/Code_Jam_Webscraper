
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;

#define sz 50

int matrix[sz][sz];
int last[sz];

int main ()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large-out.txt", "w", stdout);
	int test_cases;
	cin >> test_cases;
	string str;
	for (int numb = 0; numb < test_cases; numb++)
	{
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			cin >> str;
			for (int j = 0; j < n; j++)
				matrix[i][j] = str[j]-'0';
		}
		for (int i = 0; i < n; i++)
			last[i] = -1;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				if (matrix[i][j])
					last[i] = j;
		int ans = 0;
		for (int i = 0; i < n; i++)
		{
			int index;
			for (index = i; index < n; index++)
				if (last[index] <= i)
					break;
			ans += (index - i);
			for (int j = index-1; j >= i; j--)
				last[j+1] = last[j];
		}
		printf("Case #%d: %d\n", numb+1, ans);
	}
	return 0;
}
