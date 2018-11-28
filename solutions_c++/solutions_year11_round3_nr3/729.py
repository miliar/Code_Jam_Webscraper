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
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		long long N, L, H;
		cin >> N >> L >> H;
		vector<long long> F(N);
		for(int i = 0; i < N; i++)
			cin >> F[i];
		long long ans = 0;
		for(long long s = L; s <= H; s++)
		{
			int i = 0;
			for(; i < N; i++)
			{
				if(F[i] % s != 0 && s % F[i] != 0)
					break;
			}
			if(i == N)
			{
				ans = s;
				break;				
			}
		}
		if(ans != 0)
			cout << "Case #" << t << ": " << ans << endl;
		else
			cout << "Case #" << t << ": NO"<< endl;
	}
	//system("pause");
	return 0;
}
