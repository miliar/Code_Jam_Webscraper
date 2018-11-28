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

int O[110],OO[110],On,Op,Oi,Oni;
int B[110],BB[110],Bn,Bp,Bi,Bni;

int main()
{
	//freopen("A.in","r",stdin);
	//FRsmall(A,0)
	FRlarge(A)

	int T,C=0,n,i;
	char ch;
	int t,c;
	scanf("%d",&T);
	while(++C<=T)
	{
		scanf("%d",&n);
		On=Bn=0;
		for(i=0;i<n;i++)
		{
			scanf(" %c %d",&ch,&t);
			if(ch=='O'){O[On]=t;OO[On]=i;On++;}
			if(ch=='B'){B[Bn]=t;BB[Bn]=i;Bn++;}
		}
		Op=Bp=1;
		Oi=Bi=0;
		c=0;
		while(Oi<On || Bi<Bn)
		{
			Oni=Oi;Bni=Bi;
			if(Oi<On)
			{
				if(Op<O[Oi])Op++;
				else if(Op>O[Oi])Op--;
				else if(Bi==Bn || BB[Bi]>OO[Oi])Oni++;
			}
			if(Bi<Bn)
			{
				if(Bp<B[Bi])Bp++;
				else if(Bp>B[Bi])Bp--;
				else if(Oi==On || OO[Oi]>BB[Bi])Bni++;
			}
			Oi=Oni;Bi=Bni;
			c++;
		}
		printf("Case #%d: %d\n",C,c);
	}
	return 0;
}
