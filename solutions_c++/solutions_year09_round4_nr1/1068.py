#include <iostream>
#include <string>
#include <cstring>

int const N = 111;
int n,t;
std::string s[N];
int last[N];
int u[N];

#define LOCAL

int main()
{
    #ifdef LOCAL
    freopen("input.txt","r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    
    std::cin >> t;
    for (int tt = 0; tt < t; tt++)
    {
	std::cin >> n;
	memset(u,0,sizeof(u));
	
	for (int i = 0; i < n; i++)
	{
	    std::cin >> s[i];
	    for (last[i] = n - 1; last[i] >= 0; last[i]--)
	    {
		if (s[i][last[i]] == '1')
		    break;
	    }
	}
	
	int ans = 0, ans2 = 0;
	for (int i = 0; i < n; i++)
	{
	    for (int j = i; j < n; j++)
		if (last[j] <= i)
		{
		    ans += j - i;
		    for (int t = j-1; t >= i; t--)
		    {
			std::swap(s[t], s[t+1]);
			std::swap(last[t], last[t+1]);
		    }
		    break;
		}
	}
	
	std::cout << "Case #" << tt+1 << ": " << ans << "\n";
    }
    return 0;
}

