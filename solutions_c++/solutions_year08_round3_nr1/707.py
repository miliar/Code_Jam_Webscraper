#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <ctime>
#include <queue>
#include <climits>

using namespace std;

#define MP make_pair
#define FF first
#define SS second
#define SZ size()
#define PB push_back
#define all(x) (x).begin(), (x).end()
#define FORZ(i, n) for(typeof(n) i = 0 ; i !=n ; i++)

typedef long long LL;
typedef pair <int, int> II;
typedef vector <int> VI;


int main()
{
    int t;
    cin >> t;
    FORZ(k, t)
    {
	int maxChar, keys, totAlpha;
	cin >> maxChar >> keys >> totAlpha;
	vector <int> given;
	int tmp;
	FORZ(i, totAlpha)
	{
	    scanf("%d", &tmp);
	    given.PB(tmp);
	}
	if(maxChar * keys < totAlpha)
	{
	    printf("Impossible\n");
	    continue;
	}
	sort(all(given), greater<int>() );
	int arr[keys][maxChar];
	memset(arr, -1, sizeof(arr));
	for(int i = 0, row = 0, col = 0 ; i < totAlpha; i++, row = (row + 1)%keys)
	{
	    arr[row][col] = given[i];
	    if(row == keys - 1)
		col++;
	}
	int ans = 0;
	FORZ(i, keys)
	{
	    FORZ(j, maxChar)
	    {
		if(arr[i][j] != -1)
		    ans += arr[i][j] * (j+1);
	    }
	}
	printf("Case #%d: %d\n", k+1, ans);

    }
    return 0;
}
