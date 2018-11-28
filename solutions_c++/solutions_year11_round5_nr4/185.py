#include <assert.h> 
#include <ctype.h> 
#include <float.h> 
#include <math.h> 
#include <stdio.h> 
#include <string> 
#include <stdlib.h> 
#include <time.h> 
#include <algorithm> 
#include <numeric> 
#include <functional> 
#include <utility> 
#include <vector> 
#include <list> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <sstream> 
#include <iostream> 
#include <memory.h>

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;


char s[410];;
int N;
ll ans;

bool check(ll a, int maxDig)
{
	ll o = a;

	int i;
	for (i = 0; i < maxDig; i++)
	{
		if (!a)
			break;

		if (i == N)
			return false;

		if (s[i] != '?')
		{
			if ((a & 1) != s[i] - '0')
				return false;
		}
		a /= 2;
	}

	if (maxDig == N)
	{
		if (a == 0 && i == N)
		{
			ans = o;
		}
		else
		{
			return false;
		}
	}
		

	return true;

}

void search(ll cur, int pos)
{
	if (pos > N)
		return;


	if (!check(cur * cur, pos))
		return;

	if(ans != -1)
		return;

	if (pos < 32)
	{
		search(cur + (1LL << pos), pos + 1);
	}

	if (ans != -1)
		return;

	search(cur , pos + 1);

}

void solveTest()
{
	scanf("%s", s);
	N = strlen(s);
	reverse(s, s + N);

	ans = -1;
	

	search(0, 0);

	string res;
	while (ans)
	{
		res += ans & 1 ? '1' : '0';
		ans /= 2;
	}

	assert (res.size() == N);
	{
		for (int i = 0; i < N; i++)
		{
			if (s[i] != '?')
			{
				if (s[i] != res[i])
					printf("FAILED");
			}
		}
	}

	reverse(all(res));


	printf("%s\n", res.c_str());
}


int main(int argc, char* argv[])
{
	freopen("test.in", "r", stdin);

	int T;
	scanf("%d", &T);

	for (int nTest = 1; nTest <= T; nTest++)
	{		
		printf("Case #%d: ", nTest);

		solveTest();

		fflush(stdout);
	} 

	return 0;
}


