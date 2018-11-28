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

#define maxn 40
#define maxv 1000010
#define datat int
#define ansdatat int

int n;
int mark[maxn][maxn], f[maxn][maxn], a1,a2,b1,b2, g[maxv];

int ff(int a, int b){
	if(a<=0 || b<=0) 
		return 0;
	if(mark[a][b]>0)
		return f[a][b];
	mark[a][b] = 1;
	f[a][b] = 0;
	int now;
	now = a-b;
	while(now>0){
		if(ff(now,b) == 0){
			f[a][b] = 1;
			return 1;
		}
		now-=b;
	}
	now = b-a;
	while(now>0){
		if(ff(a,now) == 0){
			f[a][b] = 1;
			return 1;
		}
		now-=a;
	}
}

bool get_(int a,int b){
	return !(g[a]<=b && b<g[a]+a);
}

bool check(int a, int b){
	if(a>b)
		return get_(b,a);
	else
		return get_(a,b);
}

void deal(){
	for(int i = 0;i<maxn;i++)
		for(int j = 0;j<maxn;j++){
		ff(i,j);
	}
	for(int i = 1;i<maxn;i++){
		for (int j = 1;j<maxn ;j++ )
		if(f[i][j] == 0)
		{
			g[i] = j;
			break;
		}
	}
	for(int i = maxn;i<maxv;i++){
		if(get_(g[i-1],i)){
			g[i] = g[i-1]+1;
		}
		else{
			g[i] = g[i-1];
		}
	}
/*
	for (int i = 1;i<=100 ;i++ )
	{
		cout<<g[i]<<endl;
	}
*/
	
}

void init_deal(){
	deal();
}

int main(){
	
	int tttt;
	scanf("%d", &tttt);
	init_deal();
	for(int ttt = 1;ttt<=tttt;ttt++){

		scanf("%d%d%d%d", &a1,&a2,&b1,&b2);

		long long ans = 0;
		for(int i = a1;i<=a2;i++){
/*
			for(int j = b1;j<=b2;j++)
			if(g[i]<=j&&j<g[i]+i){
		}
		else{
						ans++;
		}
*/
			long long ll = g[i],rr = g[i]+i-1,
						al = ll, ar = rr;
			if(al < b1)
			   al = b1;
			if(ar > b2)
			   ar = b2;

			long long tmp = b2-b1+1;
			if(al<=ar){
				tmp-= ar-al+1;
			}
			ans+=tmp;
			

		}


		
		
		printf("Case #%d: ",ttt);
		//printf("%d", ans);
		cout<<ans;

		printf("\n");
	}
	

	return 0;
};

