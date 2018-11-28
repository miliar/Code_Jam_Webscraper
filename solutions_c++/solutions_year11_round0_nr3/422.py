#include <cstdio>
#include <iostream>
using namespace std;

int TC = 1, T, NC = 1, N;

int main ()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
    for (cin>>T; TC <= T; TC++)
    {
		printf ("Case #%d: ", TC);
		int sum = 0, dsum = 0, lst = 0, num;
		for (cin>>N, NC = 0; NC < N; NC++)
		{	cin>>num;
			sum = sum^num;
			dsum += num;
			lst = ((lst<=num) && (lst) ? lst : num);
		}
		if (sum)
			puts ("NO");
		else
			cout<<dsum-lst<<endl;
    }
	fclose(stdin);
	fclose(stdout);
    return 0;
}
