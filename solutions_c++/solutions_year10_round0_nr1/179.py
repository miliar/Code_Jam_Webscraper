#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <numeric>
#include <functional>
#include <iterator>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <complex>
#include <ctime>
using namespace std;

#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MEM(a,q) memset(a,q,sizeof(a))
#define FOR(i,s,n) for(i=s;i<n;i++)
#define PI acos(-1.0)
#define in(x) scanf("%d",&x)
#define out(x) printf("%d",x)


int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int t,n,k,ca=0;
	in(t);
	while(t--)
	{
		in(n);
		in(k);
		int x=(1<<n);
		cout<<"Case #"<<++ca<<": ";
		if(k%x==x-1)
		{
			puts("ON");
		}
		else puts("OFF");
	}
	return 0;
}