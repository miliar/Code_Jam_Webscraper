#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
using namespace std;

int main()
	{

		int N,K,T,x=1;
		for(scanf("%d",&T);T>0;T--)
		{
			scanf("%d%d",&N,&K);
		
			if((K%(1<<N))==((1<<N)-1)) printf("Case #%d: ON\n",x++);
			else printf("Case #%d: OFF\n",x++);
		}
	}
