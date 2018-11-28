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
	set <int> f;
	for(int t=1;t<=T;++t) {
		int a,b,ans=0;
		scanf("%d%d",&a,&b);
		int l=1,step=10;
		while(a>=step) l++,step*=10;
		int mx=step;
		for(int i=a;i<=b;++i) {
			step=10;
			f.clear();
			for(int j=1;j<l;++j,step*=10) {
				int num=(i%step)*(mx/step)+(i/step);
				if (i<num&&num<=b) {
					f.insert(num);
				}
			}
			ans+=f.size();
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
