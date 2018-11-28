#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int main(){
	int m,n,s,cnt,sum,p,t,T,i;
	scanf("%d", &m );
	for(int T = 1; T <= m; T++){
		cnt=0,sum=0;
		scanf("%d%d%d", &n, &s, &p);
		for(i = 0; i < n; ++ i){
			scanf("%d", &t);
			if(p>t) continue;
			if(3*p - 4 == t || 3*p - 3 == t){
				if(cnt < s){
					++cnt;
					++sum;
				}
			}
			else if( t >= 3*p - 2 ) 
				++sum;
		}
		printf("Case #%d: %d\n",T, sum);
	}
}
