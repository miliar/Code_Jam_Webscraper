#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
using namespace std;
typedef unsigned long long LLU;
typedef long long LL;
typedef pair<int,int> pii;
#define MP make_pair
const int INF=99999999;
const double PI=3.1415926535897932384626;
const double EPS=1E-11;
int GCD(int a, int b)
{
	while( 1 )
	{
		a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

		if( b == 0 )
			return a;
	}
}
int main()
{
	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
	int testn;
	scanf("%d",&testn);
	for(int tn=1;tn<=testn;tn++)
	{
		int n,pday,ptot;
		scanf("%d%d%d",&n,&pday,&ptot);
		printf("Case #%d: ",tn);
		if(ptot==100)
		{
			if(pday!=100)
			{
				printf("Broken\n");
				continue;
			}
			else
			{
				printf("Possible\n");
				continue;
			}
		}
		if(ptot==0)
		{
			if(pday!=0)
			{
				printf("Broken\n");
				continue;
			}
			else
			{
				printf("Possible\n");
				continue;
			}
		}
		int t=GCD(pday,100);
		int a=100/t;
		if(a>n)
		{
			printf("Broken\n");
			continue;
		}
		printf("Possible\n");
	}
}
