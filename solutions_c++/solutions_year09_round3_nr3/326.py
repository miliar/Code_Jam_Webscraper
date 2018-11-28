#include <iostream>
#include <cmath>
#include <vector>

#define taskId "C"

using namespace std;

int was[10000];
int need[10000];
int p;

long long ans;

void solve(int n, int q, vector<int> vec, long long sum)
{
	if (n == q)
	{
		ans = min(ans, sum);
	}
	else
	{
		for (int i = 0; i<q; i++)
		{
			if (was[i] == 0)
			{
				int l=0, r = p + 1;
				long long tmp = 0;
				for (int j = 0; j<vec.size(); j++)
					if (vec[j]<need[i] && vec[j]>l)
						l = vec[j];
				for (int j = 0; j<vec.size(); j++)
					if (vec[j]>need[i] && vec[j]<r)
						r = vec[j];
				tmp = r - l - 2;
				was[i] = 1;
				vec.push_back(need[i]);
				solve(n+1, q, vec, sum + tmp);
				vec.pop_back();
				was[i] = 0;
			}
			
		}
	}
}
		
int main (int argc, char * const argv[])
{
	freopen(taskId"-small.in","r",stdin);
	freopen(taskId"-small.out","w",stdout);
	
	int _T;
	cin >> _T;
	
	for (int T = 0; T<_T; T++)
	{
		int q;
		cin >> p >> q;
		
		for (int i = 0; i<q; i++)
			cin >> need[i];
		
		ans = 100000000000LL;
		vector<int> vec;
		vec.push_back(0);
		vec.push_back(p+1);

		solve(0, q, vec, 0);
		cout << "Case #" << T + 1 << ": " << ans << '\n'; 
	}
	
    return 0;
}
