
#include <cstring>
#include <string>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

int main()
{
//	freopen("A-small-attempt0.in","rt",stdin);
//	freopen("A-small.out","wt",stdout);

	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);

	int t;
	cin >> t;

	for(int tt=0; tt<t; tt++)
	{
		int a[1001];
		int b[1001];

		int n;
		 cin >> n;

		 for(int i=0; i<n; i++)
			 cin >> a[i] >> b[i];

		 int c = 0;
		 for(int i=0; i<n; i++)
			 for(int j=i+1; j<n; j++)
				 if((a[i]>a[j]) != (b[i]>b[j]))
					 c++;

		 printf("Case #%d: %d\n",tt+1,c);


	}
	return 0;
}
