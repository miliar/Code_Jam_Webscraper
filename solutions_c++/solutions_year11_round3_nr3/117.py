#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int n, l, h;
int vals[10000];

int find()
{
	for(int f = l; f <= h; ++f)
	{
		bool ok = true;
		
		for(int j = 0; j < n; ++j)
			if(!(vals[j] % f == 0 || f % vals[j] == 0))
			{
				ok = false;
				break;
			}
		if(ok) return f;
	}
	return -1;
}

int main()
{
	int T; scanf("%i", &T);
	for(int t = 1; t <= T; ++t)
	{
		scanf("%i %i %i", &n, &l, &h);		
		for(int i = 0; i < n; ++i)
			scanf("%i", &vals[i]);
		int f = find();
		
		printf("Case #%i: ", t);
		if(f == -1) printf("NO\n");
		else printf("%i\n", f);
	}
	return 0;
}
