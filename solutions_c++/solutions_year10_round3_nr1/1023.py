#include <cstdio>
#include <set>
using namespace std;
int main()
{
	int t;
	scanf("%d", &t);
	for(int nt = 1; nt <= t; nt++)
	{
		int n;
		scanf("%d", &n);
		set<pair<int,int> > S;
		int suma = 0;
		for(int i = 0; i < n; i++)
		{
			int a, b;
			scanf("%d %d", &a, &b);
			for(set<pair<int,int> >::iterator it = S.begin(); it != S.end(); it++)
				if(((*it).first < a && (*it).second > b) || ((*it).first > a && (*it).second < b))
					suma++;
			S.insert(make_pair(a,b));
		}
		printf("Case #%d: %d\n", nt, suma);
	}
	return 0;
}
