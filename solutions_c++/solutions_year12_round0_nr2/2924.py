#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	int T;	cin >> T;
	
	for(int cas = 1; cas <= T; ++ cas)
	{
		int N, P, S, ans = 0, tmp = 0;
		
		cin >> N >> S >> P;
		while(N --)	
		{
			int x;	cin >> x;
			int r = x % 3;
			x /= 3;
			
			if(x == 0 && r < 2)	ans += r >= P;
			
			else if(x >= P)	++ ans;
			
			else if(x == P - 1 && r)	++ ans;
			
			else if(x == P - 1 && !r)	++ tmp;
			
			else if(x == P - 2 && r == 2)	++ tmp;	
		}
		
		cout << "Case #" << cas << ": " << ans + min(tmp, S) << endl;
	}
	
	
	return 0;
}
