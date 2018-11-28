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

using namespace std;

int main(){
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int Te=1,cas; scanf("%d",&cas);
	while( cas-- ){
		int N; scanf("%d",&N);
		int a[1005];
		for(int i=1;i<=N;i++) scanf("%d",a+i);
		double ans=0.0;
		bool vst[1005]={false};
		for(int i=1;i<=N;i++){
			if( a[i]==i || vst[i] ) continue;
			int loop=1;
			int t=i;
			vst[i]=true;
			while( a[t]!=i ){
				loop++;
				t=a[t];
				vst[t]=true;
			}
			ans+=loop;
		}
		printf("Case #%d: %.10lf\n",Te++,ans);
	}
}