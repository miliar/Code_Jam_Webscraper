#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <fstream>
#include <memory.h>

using namespace std;

bool OK(long long N, int pd, int pg)
{
	if(pg == 100)
		if(pd == 100)
			return true;
		else
			return false;
	else if(pg == 0)
		if(pd)
			return false;
		else
			return true;
	else
	{
		for(long long i=N; i>=1; i--)
			if((i * pd)%100 == 0)
				return true;
		return false;
	}
}

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("aSout1.txt", "w", stdout);
//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("aSout.txt", "w", stdout);
	int cas;
	cin >> cas;
	for(int i=1; i<=cas; i++)
	{
		long long N;
		int pd, pg;
		cin >> N  >> pd >> pg;
		cout << "Case #" << i << ": ";
		if(OK(N, pd, pg))
			cout << "Possible" << endl;
		else
			cout << "Broken" << endl;

	}
	return 0;
}
