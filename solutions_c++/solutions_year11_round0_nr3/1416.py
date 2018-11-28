#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T,n,i,j,k,x,s;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>n;
		k=100000000;
		x=s=0;
		for(i=0;i<n;i++)
		{
			cin>>j;
			s+=j;
			x^=j;
			k=min(j,k);
		}
		printf("Case #%d: ",t);
		if (x) puts("NO"); else printf("%d\n",s-k);
	}

	return 0;
}