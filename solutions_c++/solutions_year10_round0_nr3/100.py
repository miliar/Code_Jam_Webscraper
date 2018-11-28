#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <set>
#include <vector>

using namespace std;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	int t,c=1;
	cin >> t;
	while(t--)
	{
		int r, k, n;
		cin >> r >> k >> n;
		
		int i;
		int grps[2000];
		__int64 tot = 0;
		__int64 ans = 0;

		for (i=0; i<n; i++)
		{
			cin >> grps[i];
			tot = tot + (__int64)grps[i];
		}

		cout << "Case #" << c++ << ": ";
		if(tot <= (__int64)k)
		{
			ans = tot * (__int64)r;
			cout << ans << endl;
			continue;
		}

		set<int> circle;
		vector<int> ids;
		vector<__int64> loop;
		__int64 sum = 0;

		int repeatedId = -1;
		i = 0;
		circle.insert(0);
		ids.push_back(0);
		while(true)
		{
			if(sum + (__int64)grps[i] > (__int64)k)
			{
				if(sum == 0 || sum > (__int64)k) break;
				ans += sum;
				int id = i;
				loop.push_back(sum);
				ids.push_back(id);
				//cout << id << endl;
				if(circle.find(id) != circle.end())
				{
					repeatedId = id;
					break;
				}
				else
				{
					circle.insert(id);
				}
				sum = 0;
			}
			sum = sum + (__int64)grps[i++];
			if(i==n) i = 0;
		}

		if(repeatedId == -1)
		{
			cout << ans << endl;
			continue;
		}

		//cout << repeatedId << endl;

		ans = 0;
		int size = ids.size();
		int loopLen;
		int stIndex = -1;
		__int64 loopSum = 0;
		for (i=0; i<size-1; i++)
		{
			if(r == 0) break;
			r --;
			ans += loop[i];
			if(ids[i] == repeatedId)
			{
				stIndex = i;
				loopLen = size - i - 1;
			}
			if(stIndex!=-1) loopSum = loopSum + loop[i];
		}

		int g1 = r/loopLen;
		int g2 = r%loopLen;

		ans = ans + loopSum * g1;
		if(g2!=0)
		{
			int j = 0;
			for (i=stIndex,j=0; j<g2; i++,j++) ans += loop[i];
		}
		
		cout << ans << endl;
	}
	return 0;
}