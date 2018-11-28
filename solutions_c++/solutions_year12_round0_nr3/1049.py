#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int caso=1; caso<=T; caso++)
	{
		int A, B;
		scanf("%d %d", &A, &B);
		
		int L = 0, n = A, k = 1;
		while(n > 0)
		{
			L++;
			n /= 10;
			k *= 10;
		}
		k /= 10;
		
		vector < pair <int, int> > v;
		for(n=A; n<=B; n++)
		{
			int tmp = n;
			for(int i=0; i<L-1; i++)
			{
				tmp = (tmp % 10) * k + tmp / 10;
				if(tmp > n && tmp <= B) v.push_back(make_pair(n, tmp));
			}
		}
		set < pair <int, int> > S (v.begin(), v.end());
		
		printf("Case #%d: %d\n", caso, (int)S.size());
	}
	
	return 0;
}
