#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <functional>
#include <map>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
using namespace std;

int T,N,S,p,t[100];

int main(){
	scanf("%d",&T);
	for(int X = 1; X <= T; X++){
		scanf("%d%d%d",&N,&S,&p);
		for(int i = 0; i < N; i++){
			scanf("%d",t+i);
		}
		int A = 3*p-2;
		int B = 3*p-4;
		
		int ans = 0,surprising = 0;
		for(int i = 0; i < N; i++){
			if(t[i]>=A) ans++;
			else if(t[i]>=B&&t[i]>=2) surprising++;
		}
		ans += min(surprising,S);
		
		printf("Case #%d: %d\n",X,ans);
	}
	return 0;
}
