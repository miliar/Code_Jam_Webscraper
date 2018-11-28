#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

int seq[10000];

void swap(int &x, int &y)
{
	int t = x; x = y; y = t;
}

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	//freopen("XXX-large.out", "w", stdout);
	int test, cas = 1;
	cin>>test;
	while(test--)
	{
		int N;
		cin>>N;
		int i, ct = 0;
		for(i=1; i<=N; i++) scanf("%d", &seq[i]);

		for(i=1; i<=N; i++) if(i==seq[i])
		{
			ct++;
		}
		cout << "Case #" << cas++ << ": ";
		printf("%.6lf\n", 1.0*(N-ct));
	}
	return 0;
}