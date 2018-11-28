#include <iostream>
#include<algorithm>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include <cstdio>
#include<map>
#include<stack>
#include<set>
#include<queue>
#include<cctype>
#include<assert.h>
#include<numeric>
#include<ctime>
#include<iterator>
//#include<sstream>
using namespace std;



int main() {
	freopen("C.in.txt", "r", stdin);
	freopen("C.out.txt", "w", stdout);
	int t,ca=1;cin>>t;
	while(t--){
		int r,k,n;
		queue<int> q;
		scanf("%d%d%d",&r,&k,&n);
		for(int i=0; i<n; i++){
			int t;scanf("%d",&t);
			q.push(t);
		}
		long long ans=0,g,cnt;
		for(int i=0; i<r; i++){
			g=k;cnt=0;
			while(cnt++<n){
				int t=q.front();
				if(g>=t){
					g-=t;ans+=t;
					q.pop();q.push(t);
				}
				else break;
			}
		}
		printf("Case #%d: %I64d\n",ca++,ans);
	}
    return 0;
}

