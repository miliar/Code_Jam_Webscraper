#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <queue>

#define pb push_back
#define pint pair <int, int>
#define mp make_pair
#define fi first
#define se second
#define vi vector<int>
#define vii vector<vi>
#define f(I, N) for(int (I) = 0; (I) < (N); (I) ++)
#define fd(I, N) for(int (I) = (N) - 1; (I) >= 0; (I) --)
#define lint long long
#define dbg 0
#define qwe if(dbg)
#define tch vector<short>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	for(int xx = 1;xx <= t;xx ++)
	{
		int n, k, r, a;
		queue<int> q;
		scanf("%d%d%d", &r, &k, &n);
		while(n --)
		{
			scanf("%d", &a);
			q.push(a);
			qwe cout << a << " ";
		}
		qwe cout << endl;
		queue<int> tmp;
		lint res = 0;
		while(r --)
		{
			int sum = 0;
			while(!q.empty() && sum + q.front() <= k)
			{
				sum += q.front();
				tmp.push(q.front());
				qwe cout << "sum = " << sum << " fr = " << q.front() << endl;
				q.pop();
			}
			res += sum;
			qwe cout << "res = " << res << endl;
			while(!tmp.empty())
			{
				q.push(tmp.front());
				tmp.pop();
			}
		}
		printf("Case #%d: %lld\n", xx, res);
	}
return 0;
}
