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


int main()
{
	//freopen("C.in","r",stdin);
	//FRsmall(C,0)
	FRlarge(C)

	int T,TC=0;
	int n,i,m,s,t,ss;
	scanf("%d",&T);
	while(++TC<=T)
	{
		printf("Case #%d: ",TC);
		scanf("%d",&n);
		m=1000000;s=0;ss=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&t);
			s^=t;ss+=t;
			if(t<m)m=t;
		}
		if(!s)printf("%d\n",ss-m);
		else puts("NO");
	}
	return 0;
}
