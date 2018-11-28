#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int TC = 1, T, NC = 1, N, C, CC, D, DC;

int main ()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	for (cin>>T; TC <= T; TC++)
    {
		int k = 0;
		for (cin>>N, NC = 0; NC < N; NC++)
		{
			int tmp;
			cin>>tmp;
			if (tmp!=NC+1) k++;
		}
		printf ("Case #%d: %d\n", TC, k);
    }
	fclose(stdin);
	fclose(stdout);
    return 0;
}


