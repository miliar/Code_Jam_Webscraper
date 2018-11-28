#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for (int i = 0;i<T;i++)
	{
		int N, K;
		cin>>N;
		cin>>K;

		bool b = (K % (1<<N)) == ((1<<N) - 1);

		printf("Case #%d: %s\n", i+1, b ? "ON" : "OFF");
	}

	return 0;
}
