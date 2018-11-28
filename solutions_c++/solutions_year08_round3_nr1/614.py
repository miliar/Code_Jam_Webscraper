#include <algorithm>
#include <iostream>
using namespace std;
int main()
{
	long long int N, i, o, res, P, K, L;
	long long int tab[10000], wtab[10000];
	cin >> N;
	for (o=1; o<=N; ++o)
	{
		//scanf("%d%d%d", &P, &K, &L);
		cin >> P >> K >> L;
		for (i=0; i<10000; ++i) tab[i]=11000000;
		for (i=0; i<L; ++i)
		{
			int tmp;
			scanf("%d", &tmp);
			tab[i]=tmp;
		}
		sort(tab, tab+(sizeof(tab) / sizeof(tab[0])));
		res=0;
		for (i=0; i<L; ++i)
			wtab[L-1-i]=tab[i];
		for (i=0; i<L; ++i)
			res+=(i/K+1)*wtab[i];
		cout << "Case #" << o << ": " << res << endl;
	}
	return 0;
}

