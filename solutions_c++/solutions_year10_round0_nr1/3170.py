#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <memory.h>
using namespace std;


int main()
{
    freopen("a.in","rt",stdin);
    freopen("a.out","wt",stdout);
	int t,cnt = 1;;
	cin >> t;
    while(t--)
	{
		int n,k;
		cin >> n >> k;
		if((k + 1) % (1 << n) == 0)
			cout << "Case #"<< cnt++ <<": ON\n";
		else
			cout << "Case #"<< cnt++ <<": OFF\n";
	}
	return 0;
}
