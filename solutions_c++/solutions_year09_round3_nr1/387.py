#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; e<= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n, t) t *v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c, t) for(VAR(i, (c).begin() , t); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second

int digit[128];
char temp[64];

long long Calc(char* temp)
{
	REP(i, 128) digit[i] = -1;
	int n = 1;
	REP(i, strlen(temp))
	{
		if (digit[temp[i]] < 0)
			if (n==2)
			{
				digit[temp[i]] = 0;
				n=-n;
			}
			else
			{
				if (n<0) n=-n;
				digit[temp[i]]=n++;
			};
	}

	if (n<0) n=-n;
	long long ret = digit[temp[0]];

	REP(i, strlen(temp)-1)
	{
		ret = ret*n + digit[temp[i+1]];
	}
	return ret;
}



int main()
{
	int cases;
	cin >> cases;

	REP(cas, cases)
	{
		cin >> temp;


		cout << "Case #" << cas+1 << ": " << Calc(temp) << endl;
	}


	return 0;
};