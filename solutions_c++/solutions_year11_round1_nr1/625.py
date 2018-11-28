#include<cstdio>
#include<algorithm>
#include<set>
#include<vector>
#include<queue>
#include<stack>
#include<memory.h>
#include<cstdlib>
#include<map>
#include<cmath>
#include<algorithm>
using namespace std;

long long int t,n,m,a,b;
double pd,pg;
bool pop = false;
int main(){
	scanf("%lld", &t);
	for(int j = 0; j < t; j++){
		scanf("%lld%lf%lf", &n, &pd, &pg);
		pop = false;
		for(int i = 1; i <= n; i++){
			if(floor((pd*i)/100) == ceil((pd*i)/100)){
				pop = true;
				break;
			}
		}
		if(pg==0 && pd == 0)printf("Case #%d: Possible\n", j+1);
		else if(pg == 0)printf("Case #%d: Broken\n", j+1);
		else if(pg == 100 && pd != 100)printf("Case #%d: Broken\n",j+1);
		else if(pop)printf("Case #%d: Possible\n", j+1);
		else printf("Case #%d: Broken\n", j+1);	
	}
	return 0;
}
