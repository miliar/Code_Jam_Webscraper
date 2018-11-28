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

double p[99999 + 20];

struct node{
	int pos;
	int num;
	bool operator < (const node & m)const{
		return num < m.num;
	}
}a[1002],b[1002];
int x[1002],y[1002];
bool used[1002];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,n;

	scanf("%d",&T);
	for(int cas = 1; cas <= T; cas ++){
		scanf("%d",&n);
		memset(used,false,sizeof(used));
		for(int i = 0; i < n; i ++){
			scanf("%d %d",&x[i],&y[i]);
			b[i].pos = i;
			b[i].num = y[i];
		}
		sort(b,b+ n);
		int now = 0,ans = 0;
		bool flag = true;
		for(int i = 0; i < n; i ++){
			//star 不够做等级1的刷star
			while(now < b[i].num){
				int pos = -1;
				for(int j = 0; j < n;j ++){
					if(!used[j] && now >= x[j] &&(pos < 0 || y[j] > y[pos])) pos = j;
				}
				if(pos == -1){
					flag = false;
					break;
				}
				//If the player has never completed the level before and completes it with a 1-star rating, that player earns 1 star.
				now ++;
				used[pos] = true;
				ans ++;
			}
			if(now < b[i].num) {
				flag = false;
				break;
			}
			//If the player has never completed the level before and completes it with a 2-star rating, that player earns 2 stars.
			if(!used[b[i].pos]) now += 2;
			//If the player has only completed the level before with a 1-star rating and completes it this time with a 2-star rating, the player earns 1 more star.
			else now ++;
			used[b[i].pos] = true;
			ans ++;
			
		}
		 printf("Case #%d: ",cas);
		if(flag) printf("%d\n",ans);
		else puts("Too Bad");
		
		

	}
	return 0;
}