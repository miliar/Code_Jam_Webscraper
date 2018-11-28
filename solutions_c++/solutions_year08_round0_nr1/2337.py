// program written in C++
// compiled with g++ 3.4.2

#include <iostream>
#include <cstdlib>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <cstring>
using namespace std;

int main()
{
	int n,i,j;
	int s,q;
	set<string> qrs;
	string qq;
	char line[200];
	int minc;
	
	cin >> n;
	
	for (j=1; j<=n; ++j)
	{
		cin >> s;
		gets(line);
		for (i=0;i<s;++i)
		{
			gets(line);
			qq = line;
		}
		cin >> q;
		gets(line);
		minc = 0;
		while (q--)
		{
			gets(line);
			qq = line;
			qrs.insert(qq);
			if (qrs.size() == s)
			{
				++minc;
				qrs.clear();
				qrs.insert(qq);
			}
		}
		cout << "Case #" << j << ": " << minc << endl;
		qrs.clear();		
	}

	return 0;
}
