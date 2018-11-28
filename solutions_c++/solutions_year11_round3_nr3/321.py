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
#include <ctime>
#include <queue>
#include <complex>
#include <limits>
#include <string.h>
#include <fstream>
using namespace std;
#define rep(x,n) for(int x=0;x<n;x++)
#define mp(x,y) make_pair(x,y)
#define getBit(code, i) (code & (1 << i))
#define setBit(code, i) (code | (1 << i))
#define resetBit(code, i) (code & ~(1 << i))
#define mem(a, b) memset(a, b, sizeof(a))

int all[105];
int N,L,H;
void main2()
{
	cin >> N >> L >> H;
	rep(i,N)
		cin >> all[i];
	for(int i=L;i<=H;i++)
	{
		bool ok = true;
		rep(j,N)
		{
			if( (all[j] % i) != 0 && (i % all[j]) != 0 )
			{
				ok = false;
			}
		}
		if(ok == true)
		{
			cout << i << endl;
			return;
		}
	}
	cout << "NO\n";
}

int main()
{
	freopen("in.txt", "r", stdin);
	//freopen("2small.txt", "w", stdout);
	//freopen("1big.txt", "w", stdout);
	int K;
	cin >> K;
	rep(kase,K)
	{
		printf("Case #%d: ",kase+1);
		main2();
	}
	return 0;
}
