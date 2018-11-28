#include <cstdio>
#include <memory>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int used[100000];
vector<int> bases;

bool lucky(int n, int base)
{
	if (n == 1)
		return 1;
	if (used[n] == 1)
		return 0;
	used[n] = 1;
	int val = 0;
	while (n)
	{
		val += (n%base)*(n%base);
		n /= base;
	}
	return lucky(val,base);

}

int run()
{
	for (int i=2; i; i++)
	{
		int b = true;
		for (int j=0; j<bases.size(); j++)
		{
			memset(used,0,sizeof(used));
			if (lucky(i,bases[j]) == false)
			{
				b = false;
				break;
			}
		}
		if (b)
			return i;
	}
}


int main()
{
	int T;
	char buf[10000];
	scanf("%d", &T);
		cin.getline(buf,10000);
	for (int t=0; t<T; t++)
	{
		cin.getline(buf,10000);
		bases.clear();
		istringstream sin(buf);
		while (sin)
		{
			int a;
			sin >> a;
			if (sin)
				bases.push_back(a);
		}
		int res = run();
		printf("Case #%d: %d\n", t+1, res);
	}
	return 0;
}