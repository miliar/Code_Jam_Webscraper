#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <set>

using namespace std;

int calc(int x, int A, int B)
{
	int D = 1;
	while(D < x)	D *= 10;
	int P = 10;
	set <int> st;
	while(P < x)
	{
		if(x % P >= P / 10)
		{
			int y = (x % P) * (D / P) + x / P;
			if(y >= A && y <= B && y > x)
			{
				st.insert(y);	
			}
		}
		P *= 10;	
	}	
	return st.size();
}

int solve(int A, int B)
{
	int ret = 0;
	for(int i = A; i <= B; ++ i)
	{
		ret += calc(i, A, B);
	}
	return ret;	
}


int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out_c.out", "w", stdout);
	
	int T;	cin >> T;
	
	for(int cas = 1; cas <= T; ++ cas)
	{
		int A, B;
		cin >> A >> B;
		cout << "Case #" << cas << ": " << solve(A, B) << endl;
	}
	
	
	
	return 0;	
}
