#include <iostream>
#include <string>
#include <set>
using namespace std;

int		n , q;
int		ans;

void	init()
{
	string		line;
	cin >> n;
	getline(cin , line);
	for (int i = 0; i < n; i ++)
		getline(cin , line);
}

void	solve()
{
	string		line;
	cin >> q;
	getline(cin , line);

	set<string>	Set;
	ans = 0;

	while (q --)
	{
		getline(cin , line);
		Set.insert( line );
		if (Set.size() == n)
		{
			ans ++;
			Set.clear();
			Set.insert( line );
		}
	}

	printf("%d\n" , ans);
}

int	main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);

	int	cntCase , t;
	cin >> cntCase;

	for (t = 1; t <= cntCase; t ++)
	{
		printf("Case #%d: " , t);

		init();
		solve();

		
	}

	return 0;
}
