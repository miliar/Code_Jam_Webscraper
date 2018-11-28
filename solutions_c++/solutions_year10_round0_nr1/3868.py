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

#define PB push_back
#define mset(x,a) memset(x,(a),sizeof(x))
#define SIZE(X) ((int)X.size())



int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t,k,n;
	int z=1;
	scanf("%d",&t);
	while (t--)
	{
     scanf("%d",&n);
	 scanf("%d",&k);

	 long long times;
	 times=((int)pow(2,(double)n))-1;
	 if(k==times) printf("Case #%d: ON\n",z);
	 else if((k+1)%(times+1)==0)printf("Case #%d: ON\n",z);
	 else printf("Case #%d: OFF\n",z);
	 z++;
	}
	return 0;
}