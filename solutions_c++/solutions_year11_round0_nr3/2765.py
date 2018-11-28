#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <cmath>
#include <deque>
#include <stack>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <ctime>

using namespace std;

#define maxn 1010
#define maxm (1<<21)
#define datat int
#define ansdatat int

int n, x[maxn], sum[maxn],ss;
int f[2][maxm], ans;

void init_deal(){
	memset(f,0,sizeof(f));
}

void go(int num,int s,int xs,int tot){
	if(num>n){
		if(tot!=0 && tot!=n && (xs == (sum[n]^xs)) &&
			ans < s){
			ans = s;
		}

	}
	else{
		go(num+1, s, xs, tot);
		go(num+1, s+x[num], xs ^ x[num], tot+1);

	}
//	printf("%d %d %d %d ans= %d\n", num,s,xs,tot,ans);
}

int main(){
	
	int tttt;
	scanf("%d", &tttt);
	for(int ttt = 1;ttt<=tttt;ttt++){
		printf("Case #%d: ",ttt);
		scanf("%d", &n);
		sum[0] = 0;
		ss = 0;
		ans = 0;
		for (int i = 1;i<=n ;i++ )
		{
			scanf("%d", &x[i]);
			sum[i] = sum[i-1]^x[i];
			ss += x[i];
		}

		go(1,0,0,0);

//		cout<<sum[n]<<endl;



//		printf("ansi = %d\n", ansi);



		if(ans<=0)
			printf("NO\n");
		else
			printf("%d\n", ans);

	}
	

	return 0;
};

