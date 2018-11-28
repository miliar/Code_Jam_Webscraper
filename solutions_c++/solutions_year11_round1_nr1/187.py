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
#include <memory.h>
using namespace std;

#define FRsmall(x,y) freopen(#x"-small-attempt"#y".in","r",stdin);freopen(#x"-small-attempt"#y".out","w",stdout);
#define FRlarge(x) freopen(#x"-large.in","r",stdin);freopen(#x"-large.out","w",stdout);

int gcd(int a,int b)
{
	if(b==0)return a;
	return gcd(b,a%b);
}

int main()
{
	//freopen("A.in","r",stdin);
	//FRsmall(A,0)
	FRlarge(A)

	int T,C=0;
	scanf("%d",&T);
	while(++C<=T)
	{
		printf("Case #%d: ",C);
		int Pd,Pg,D;
		long long N;
		scanf("%I64d %d %d",&N,&Pd,&Pg);
		int d;
		d=gcd(100,Pd);
		Pd/=d;
		D=100/d;
		if(D>N || Pg==100 && D!=Pd || Pg==0 && Pd>0)
		{
			puts("Broken");
		}
		else
		{
			puts("Possible");
		}

	}
	return 0;
}
