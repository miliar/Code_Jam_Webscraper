#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#define LL long long
#define maxSize 4

int n;
LL num[maxSize];
LL dif[maxSize];
LL gcd(LL a,LL b)
{
	return ((!b)?(a):gcd(b,a%b));
}
void getAC()
{
	LL res = 0;
	LL fac ;
	sort(num,num+n);
	for(int i=0;i<n-1;i++)
		dif[i] = num[i+1] - num[i];
	sort(dif,dif+n-1);
	if(n==2)
		fac = dif[0];
	else fac = gcd(dif[0],dif[1]);
	LL tmp = num[0]%fac;
	if(tmp!=0)
	{
		res = ((num[0]/fac)+1)*fac - num[0];
	}
	printf("%d\n",res);
}
int main()
{
	freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);	
	int c;
	cin >> c;
	for(int i=1;i<=c;i++)
	{
		cin >> n;	
		for(int j=0;j<n;j++)
			cin >> num[j];
		printf("Case #%d: ",i);
		getAC();
	}
	return 0;
}