#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <map>

using namespace std;

int main(){
	freopen("dataC.in","r",stdin);
	freopen("dataC.txt","w",stdout);
	
	int T,N;
	scanf("%d",&T);
	for (int Test=1;Test<=T;Test++){
		scanf("%d",&N);
		int res = 1<<20,a = 0,tot = 0,x;
		for (int i=1;i<=N;i++){
			scanf("%d",&x);
			tot += x;
			a^=x;
			if (res>x) res=x;
		}
		if (a==0) printf("Case #%d: %d\n",Test,tot-res);
		else printf("Case #%d: NO\n",Test);
	}
	
	return 0;
}
