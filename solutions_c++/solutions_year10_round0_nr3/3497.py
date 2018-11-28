#include <iostream>
#include<vector>
#include <cstdio>
#include<queue>

using namespace std;



int main() {
	freopen("C.in.txt", "r", stdin);
	freopen("C.out.txt", "w", stdout);
	int t,ca=1;
	scanf("%d",&t);
	while(t--){
		int r,k,n,tmp,num;
		queue<int> q;
		scanf("%d%d%d",&r,&k,&n);
		for(int i=0; i<n; i++){
			scanf("%d",&tmp);
			q.push(tmp);
		}
		long long ans=0,g;
		for(int i=0; i<r; i++){
			g=k,num=0;
			while(num++<n){
				int t=q.front();
				if(g>=t){
					g-=t;ans+=t;
					q.pop();
					q.push(t);
				}
				else break;
			}
		}
		printf("Case #%d: %d\n",ca++,ans);
	}
    return 0;
}

