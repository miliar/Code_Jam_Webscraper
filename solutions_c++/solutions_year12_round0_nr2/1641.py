#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>
#include <ctime>
#include <memory.h>
#include <string>
#include <sstream>
#include <map>
#include <set>

#define ll long long

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T=0;
	scanf("%d\n",&T);
	for(int t=1;t<=T;++t) {
		int n,s,p,a,ans=0;
		scanf("%d%d%d",&n,&s,&p);
		for(int i=0;i<n;++i) {
			scanf("%d",&a);
			if (a>=3*p-2&&a>=p) ans++;
			else if (s&&a>=3*p-4&&a>=p) ans++,s--;
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
