#include <iostream>
#include <string>
#include <vector>

using namespace std;

int n;
int v;
int zero[10005];
int one[10005];
int is_and[10005];
int changable[10005];

int sol(int idx, int v)
{
	int li = (idx + 1) * 2 - 1;
	int ri = li+1;
	if (v == 0)
	{
		if (zero[idx] >= 0)
			return zero[idx];
		zero[idx] = 1000000;
		if (is_and[idx])
		{
			int z = min(min(sol(li, 0) + sol(ri, 0), sol(li, 0) + sol(ri, 1)), sol(li,1) +sol(ri,0));
			if (z < zero[idx])
				zero[idx] = z;
		}

		else
		{
			int z = sol(li, 0) + sol(ri, 0);
			if (z < zero[idx])
				zero[idx] = z;
		}
		if (changable[idx])
		{

			if (!is_and[idx])
			{
				int z = 1+min(min(sol(li, 0) + sol(ri, 0), sol(li, 0) + sol(ri, 1)), sol(li,1) +sol(ri,0));
				if (zero[idx] > z)
					zero[idx] = z;
			}
			else
			{
				int z = 1+sol(li, 0) + sol(ri, 0);
				if (z < zero[idx])
					zero[idx] = z;
			}
		}
		return zero[idx];
	}

	if (v == 1)
	{
		if (one[idx] >= 0)
			return one[idx];
		one[idx] = 1000000;
		if (!is_and[idx])
		{
			int z = min(min(sol(li, 1) + sol(ri, 1), sol(li, 0) + sol(ri, 1)), sol(li,1) +sol(ri,0));
			if (z < one[idx])
				one[idx] = z;
		}

		else
		{
			int z = sol(li, 1) + sol(ri, 1);
			if (z < one[idx])
				one[idx] = z;
		}
		if (changable[idx])
		{

			if (is_and[idx])
			{
				int z = 1+min(min(sol(li, 1) + sol(ri, 1), sol(li, 0) + sol(ri, 1)), sol(li,1) +sol(ri,0));
				if (one[idx] > z)
					one[idx] = z;
			}
			else
			{
				int z = 1+sol(li, 1) + sol(ri, 1);
				if (z < one[idx])
					one[idx] = z;
			}
		}
		return one[idx];
	}
}

int main()
{
	int tn;
	cin >> tn;
	int loop = 0;
	while(tn --)
	{
		loop ++;
		cin >> n;
		cin >> v;
		for(int i = 0; i < (n-1)/2; i ++)
		{
			int a, b;
			cin >> a >> b;
			is_and[i] = a == 1;
			changable[i] = b == 1;
			zero[i] = -1;
			one[i] = -1;

		}
		for(int i = 0; i < (n+1)/2; i ++)
		{
			int ni = i + (n-1)/2;
			int t;
			cin >> t;
			if (t == 0)
			{
				zero[ni] = 0;
				one[ni] = 1000000;
			}
			else
			{
				one[ni] = 0;
				zero[ni] = 1000000;
			}
		}
		cout << "Case #" << loop << ": ";
		int xx = sol(0,v);
		if (xx > 50000)
			cout << "IMPOSSIBLE";
		else
			cout << xx;
		cout << endl;
	}
	return 0;
}
