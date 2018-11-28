#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <sstream>
using namespace std;

typedef long long ll;

const int maxn = 256;
int C, D;

struct node
{
	int p, v;
	bool operator<(const node & n)const{
		return p < n.p;
	}
}vendor[maxn];

bool check(ll t){
	ll pos[maxn][2];
	for(int i = 0; i < C; i++){
		
		if(i > 0)
			pos[i][0] = pos[i-1][1] + D;
		else
			pos[i][0] = vendor[0].p - t;

		if(pos[i][0] > vendor[i].p + t )return false;
		if(pos[i][0] < vendor[i].p - t )pos[i][0] = vendor[i].p - t;
		pos[i][1] = pos[i][0] + (ll)(vendor[i].v - 1) * D; 
		if(pos[i][1] > vendor[i].p + t)return false;
	}

	return true;
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("ans.txt","w",stdout);
	
	int T; scanf("%d", &T);
	for(int cas = 1; cas <= T; cas++){
		scanf("%d %d",&C, &D);
		for(int i = 0; i < C; i++){
			scanf("%d %d",&vendor[i].p, &vendor[i].v);
			vendor[i].p *= 2;
		}
		D <<= 1;
		sort(vendor, vendor + C);

		ll l = 0, r = 1LL << 61, mid, res = -1;
		while(l <= r){
			mid = ( r + l ) / 2;
			if( check(mid) ){
				res = mid;
				r = mid - 1;
			}else{
				l = mid + 1;
			}
		}
		printf("Case #%d: ",cas);
		
		if(res & 1){
			printf("%lld.5\n",res/2);
		}else{
			printf("%lld.0\n",res/2);
		}
		
	}
}