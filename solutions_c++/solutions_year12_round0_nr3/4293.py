#include <iostream>
#include <cstdio>
using namespace std;
#define FOR(i,a,b) for(long i=a; i<=b; i++)
#define DOWN(i,a,b) for(long i=a; i>=b; i--)
#define maxn 3000

long ntest;
long a, b, result, temp;
long top, f[maxn];
bool check[maxn][maxn];

long solve(long x)
{
	long temp = f[x];
	if (temp == 0) return 0;
	DOWN(i,x-1,1) temp = temp * 10 + f[i];
	DOWN(i,top,x+1) temp = temp * 10 + f[i];
	return temp;
}

int main()
{	freopen("TEST.IN", "r", stdin);
	freopen("TEST.OUT", "w", stdout);
	scanf("%ld", &ntest);
	FOR(test,1,ntest)
	{
		scanf("%ld%ld", &a, &b);
		result = 0;

		FOR(i,a,b)
			FOR(j,a,b)
				check[i][j] = false;
		FOR(x,a,b)
		{
			top = 0, temp = x;
			while (temp != 0)
			{
				top++;
				f[top] = temp % 10;
				temp /= 10;
			}

			FOR(i,1,top)
			{
				temp = solve(i);
				if ((temp != x) && (min(temp, x) >= a) && (max(temp, x) <=b) && (check[x][temp] == false))
					{
						result++;
						check[x][temp] = true;
						check[temp][x] = true;
					}
			}
		}

        printf("Case #%ld: %ld", test, result);
		if (test != ntest) cout << endl;
	}
	return 0;
}
