#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <ctime>
#include <utility>

using namespace std;

int main()
{	
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int num;
	int n, i, j, t = 1;
	long m, s = 1;
	long a[30];
	a[0] = 0;
	a[1] = 1;
	for(i = 2; i <= 30; i++)
	{
		s = s << 1;
		a[i] = a[i-1]+s;
	}
	cin >> num;
	while(num--)
	{
		scanf("%d %ld", &n, &m);
		m %= (a[n]+1);
		if(m == a[n])
			printf("Case #%d: ON\n", t++);
		else
			printf("Case #%d: OFF\n", t++);
	}
}
