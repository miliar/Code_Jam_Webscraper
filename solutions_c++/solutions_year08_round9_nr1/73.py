#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

struct triplet
{
	int a, b, c;
};
int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		int n;
		cin >> n;
		vector<triplet> v(n);
		for(int i = 0; i  < n; i++)
			cin >> v[i].a >> v[i].b >> v[i].c;
		int maxm = 1;
		for(int i =0; i < n; i++)
			for(int j = 0; j < n; j++)
				for(int k = 0; k < n; k++)
				{
					if(v[i].a + v[j].b + v[k].c > 10000)
						continue;
					int cnt = 0;
					for(int u = 0; u < n; u++)
					{
						if(v[i].a >= v[u].a && v[j].b >= v[u].b && v[k].c >= v[u].c)
							cnt++;
					}
					maxm = max(maxm, cnt);
				}
		cout << maxm << endl;

	}
	return 0;
}
