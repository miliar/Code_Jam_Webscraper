
/*
ID: jwqbtx1
PROG: pprime
LANG: C++
*/
#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string.h>
using namespace std;
#define N 1000005
#define PI acos(-1.0)
#define ll long long
using namespace std; 
int arr[200];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,n,k,i,sum,j,m;
	scanf("%d",&t);
	arr[0]=1;
	for(i=1;i<=30;i++)arr[i]=2*arr[i-1]+1;
	for(j=0;j<t;j++)
	{
		sum=0;
		scanf("%d %d",&n,&k);
		k=k%(arr[n-1]+1);
		if(k==arr[n-1])printf("Case #%d: ON\n",j+1);
		else printf("Case #%d: OFF\n",j+1);
	}
	return 0;
}