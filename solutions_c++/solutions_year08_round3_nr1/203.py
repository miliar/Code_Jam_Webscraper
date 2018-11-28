#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;

long long fre[1001];
int main()
{

	ifstream cin("in.txt");
	ofstream cout("out.txt");
	//freopen("out.txt","w",stdout);
	int ncase,m;
	cin >> ncase;
	m = 0;
	while (ncase--)
	{
		int P,K,L,i;
		cin >> P >> K >> L;
		for (i = 0 ; i < L ; i++)
			cin >> fre[i];
		if ( K * P < L)
		{
			cout << "Case #" << m << ": Impossible"  << endl;
			continue;
		}
		sort(fre,fre+L);
		long long res = 0;
		long long mat = 1;
		int flag = 0;
		for (i = L - 1 ; i >= 0 ; i--)
		{
			res += fre[i] * mat;
			flag++;
			if (flag == K)
			{
				flag = 0;
				mat++;
			}
		}
		m++;
		cout << "Case #" << m << ": " << res << endl;
		//printf("Case #%d: ",m);
	}
}
