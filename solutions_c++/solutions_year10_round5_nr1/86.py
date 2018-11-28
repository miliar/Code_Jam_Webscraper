#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

bool prime[1000111];

int inv(int a, int p)
{
  int pw = p-2;
  long long ret = 1, mul = a;
  while (pw)
  {
    if (pw&1) ret *= mul;
    mul *= mul;
    
    ret %= p;
    mul %= p;
    
    pw >>= 1;
  }
  
  return ret;
}

int md(ll x, int p)
{
  return (x%p+p)%p;
}

int main()
{
  freopen("A.in", "r", stdin);
  freopen("A.out", "w", stdout);
  
  memset(prime, 1, sizeof prime);
  prime[0] = prime[1] = false;
  for (int i = 2; i*i <= 1000000; i++)
    if (prime[i])
      for (int j = i*i; j <= 1000000; j += i)
        prime[j] = false;
  
	int n_cases; cin >> n_cases;
	for (int tcase = 1; tcase <= n_cases; tcase++)
	{
		int D, K; cin >> D >> K;
		int a[100];
    int mx = 0;
		for (int i = 0; i < K; i++)
		{
			cin >> a[i];
      if (a[i] > mx) mx = a[i];
		}
		
		//duplicate = answer is immediate
		int dup = -1;
		for (int i = 0; i < K-1; i++)
			if (a[i] == a[i+1])
				dup = a[i];
		
		printf("Case #%d: ", tcase);
		
		if (dup != -1)
		{
			printf("%d\n", dup);
		}
		else if (K <= 2)
		{
			puts("I don't know.");
		}
		else
		{
      int lim = pow(10.0, D);
      bool done = false, bad = false;
      int ans = -1;
      for (int i = mx+1; i <= lim; i++)
        if (prime[i])
        {
          //see if the answers are consistent
          int x = -1;
          bool err = false;
          for (int j = 0; j < K-2; j++)
          {
            //a[j]-a[j+1] * X === a[j+1]-a[j+2]
            int nx = md(ll(a[j+1]-a[j+2]) * inv(a[j]-a[j+1], i), i);
            
            if (x != -1 && nx != x)
            {
              err = true;
              break;
            }
            else
              x = nx;
          }
          
          if (err) continue;
          
          int y = md(a[1] - md(ll(a[0])*x, i), i);
          
          //makesure this works
          for (int j = 0;j < K-1; j++)
          {
            if (md(ll(a[j])*x+y, i) != a[j+1])
              throw;
          }
          
          int nxt = md(ll(x)*a[K-1] + y, i);
          if (ans != -1 && ans != nxt)
          {
            bad = true;
            i = lim+1;
          }
          else
          {
            done = true;
            ans = nxt;
          }
        }
        
      if (bad)
        puts("I don't know.");
      else
        printf("%d\n", ans);
		}
	}

	return 0;
}