#include <cstdio>
#include <iostream>
#include <cstring>
#include <stack>
#include <algorithm>
#include <queue>
using namespace std;
int tc = 1;
int T,N,M;
priority_queue<int> pq;
int x[1200000];
long long dis[1000002];

int L,C;

long long t;
int main() {
	freopen("C.txt","w",stdout);
	freopen("Cin.txt","r",stdin);
	
scanf("%d",&T);
while (T--){
	while (!pq.empty()) pq.pop();
	scanf("%d%lld%d%d",&L,&t,&N,&C);
	for (int i=0;i<C;i++)
	scanf("%d",&x[i]);
	long long res = 0;
	for (int i=0;i<N;i++){
		int jar = 2*x[i%C];
		if (jar <= t) t-=jar;
		else {
		//	printf("%lld\n",jar-t);
			pq.push(jar - t); t = 0; 
			}
			
		res+=jar*2;
		}
	
	
	while (!pq.empty() && L) {
		L--;
		res-=(pq.top());
		pq.pop();
		}
	
	
	printf("Case #%d: ",tc++);
	if (res!=-1) {
		printf("%lld\n",res/2);
		}
	else printf("NO\n");
	}
}
