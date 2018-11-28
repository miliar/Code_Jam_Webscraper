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

char *welc = "welcome to code jam";

long long GetCount(char*str, char*sub)
{
	if (sub[0] == NULL) return 1;

	char *str1 = str, *sub1 = sub;
	int i = 0;
	long long count = 0;

	while (str1[0]) {
		if (str1[0] == sub1[0])
			count += GetCount(str1+1, sub1+1) ;
		str1++;
	}
	return count;
}

int main()
{
	int cases;
	char temp[500];
	int count;

	cin >> cases;
	cin.getline(temp, 500);

	REP(c, cases)
	{
		cin.getline(temp, 500);
		count = GetCount(temp, welc) % 10000;
		//cout << "Case #" << c+1 << ": " << GetCount(temp, welc) << endl;
		printf("Case #%d: %4.4d\n", c+1, count);
	}

	return 0;
};