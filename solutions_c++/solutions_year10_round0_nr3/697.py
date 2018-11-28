#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

#define LL __int64
#define N 1010

int r, k, n, t;
int num[N];
bool f;
LL cost[N];
int v[N];
LL tot = 0;

void init(){
    f = true; 
    scanf("%d%d%d",&k, &r, &n);
    tot = 0;
    for (int i = 0; i < n; ++i){
        scanf("%d",&num[i]);
        tot = tot + num[i];
    } 
    if (tot <= r){
       f = false;
    }
}

void run(){
    if (f == false){
       LL ans = (LL)k * tot;
       //cout << ans << endl;
       printf("%I64d\n",ans);
	   return;
    } 
    memset(v, 0xff, sizeof(v));
    int now = 0;
    int times = 0;
    int id1, id2;
    LL ans = 0;
    for (int i = 0; i < N; ++i) cost[i] = 0;

    while (true){
        int t = num[now];
        if (v[now] != -1){
           id1 = v[now];
           id2 = times;
           break;
        }
        v[now] = times;
        while (t <= r){
            now = (now + 1) % n;
            t += num[now];      
        }      
        t -= num[now];
        ans = ans + t;
        cost[times] = ans;
        times++;
        if (times == k) break;
    }
    
    int left = k - times;
	if (left > 0){
		int len = id2 - id1;
		LL money = cost[id2 - 1];
		if (id1 > 0) money = money - cost[id1 - 1];
    
		ans = ans + (LL)left / len * money;
		left = left - left / len * len;
		if (left > 0){
		   ans = ans + cost[id1 + left - 1];
		   if (id1 > 0) ans = ans - cost[id1 - 1];
		} 
	}
	printf("%I64d\n",ans);
}

int main(){
    int t;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for (int i = 0; i < t; ++i){
        init();
        printf("Case #%d: ",i + 1);
        run();
    }
    return 0;
}
