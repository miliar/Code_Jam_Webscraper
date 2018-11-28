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
	for(int s = 1; s <= T; s++)
	{		
		int C;
		long long N, L, t;
		cin >> L >> t >> N >> C;
		vector<int> a(N);
		vector<int> b(C);
		vector<bool> c(N, false);
		for(int i = 0; i < C; i++)
		{
			cin >> a[i];
			b[i] = a[i];
			
		}
		if(C == 1)
			if(L > 0)
			{
				cout << "Case #" << s << ": " << a[0] << endl;
				continue;
			}
			else
			{
				cout << "Case #" << s << ": " << a[0]*2 << endl;
				continue;
			}
		int j = 0;
		for(int i = C; i < N; i++)
		{		
			a[i] = a[j];			
			j = (j + 1)%C;
		}
		long long ans = 0;
		int i = 0;
		for(; i < N; i++)
		{
			if(ans + a[i]*2 <= t)
			{
				ans += a[i]*2;
				//cout << "1 ans " << ans << endl;
			}
			else
				break;
		}
		if(i == N)
		{
			cout << "Case #" << s << ": " << ans << endl;
			continue;
		}
		if(L > 0)
		{
			int rem = a[i]*2 - (t - ans);
			ans = t;
			if(rem %2 == 1)
			{
				//cout << " here " << endl;
				ans += 1;
				rem -= 1;
			}
			sort(b.begin(), b.end());
			reverse(b.begin(), b.end());
			long long ct = 0;
			int k = -1;
			int j = 0;
			int lastId = 0;
			for( ; ; j = (j + 1)%N)
			{	
				if(j == 0)
					k++;
				if(j <= i)
					continue;					
				if(a[j] == b[k])
				{
					//cout << " j " << j << endl;
					c[j] = true;		
					lastId = j;
					ct++;
					if(ct == L)
						break;	
				}
				//cout << " 1 " << endl;
			}
			//cout << " rem " << rem << endl;
			//cout << " a[lastId] " << a[lastId] << endl;
			if(rem > a[lastId]*2)
			{
				c[lastId] = false;
				ans += rem/2;
				//cout << "2 ans " << ans << endl;
			}
			else
			{
				ans += rem;
				//cout << "3 ans " << ans << endl;
			}
		}
		else
		{
			ans += a[i]*2;
			//cout << "4 ans " << ans << endl;
		}
		for(int m = i + 1; m < N; m++)
		{
			if(c[m] == true)
			{
				ans += a[m];
				//cout << "5 ans " << ans << endl;
			}
			else
			{
				ans += a[m]*2;
				//cout << "6 ans " << ans << endl;
			}
		}
		
		cout << "Case #" << s << ": " << ans << endl;
	}
	//system("pause");
	return 0;
}
