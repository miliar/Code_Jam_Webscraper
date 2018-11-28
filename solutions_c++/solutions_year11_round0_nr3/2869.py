/*
 * C.cpp
 *
 *  Created on: ??þ/??þ/????
 *      Author: B2lawa
 */
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
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <ext/numeric>
#include <memory.h>
#include <valarray>
using namespace std;
int N,nums[1000];
int main()
{
	freopen("C.in","rt",stdin);
	freopen("C.out","wt",stdout);
	int t,s1,s2,mx,sum;
	scanf("%d",&t);
	for(int x=1;x<=t;++x)
	{
		sum=0;
		scanf("%d",&N);
		for(int i=0;i<N;++i)
			scanf("%d",&nums[i]),sum+=nums[i];
		mx=-1;
		bool f;
		for(int i=1;i<(1<<N);++i)
		{

			s1=0,s2=0;
			f=true;
			for(int k=0;k<N;++k)
			{
				if(i&(1<<k))s1^=nums[k];
				else s2+=nums[k],f=false;
			}
			if(!f && s1==s2)mx=max(mx,sum-s2);
		}
		printf("Case #%d: ",x);
		if(mx==-1)printf("NO\n");
		else printf("%d\n",mx);

	}
}
