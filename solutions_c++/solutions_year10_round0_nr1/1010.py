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
#include <ctime>

using namespace std;

main()
{
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-output.txt","w",stdout);
	//freopen("A-small-attempt1.in","r",stdin);freopen("A-small-output.txt","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large-output.txt","w",stdout);
	int T ;
	scanf("%d",&T);
	for(int Case=1;Case<=T;Case++)
	{
		int n,k;
		scanf("%d %d",&n,&k);
		bool ok=true;
		for(int i=0;i<n;i++)if(((k>>i)&1)==0)
			ok=false;
		if(ok)
			printf("Case #%d: ON\n",Case);
		else
			printf("Case #%d: OFF\n",Case);
	}
}

