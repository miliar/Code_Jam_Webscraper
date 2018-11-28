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

bool p[2000001];

inline int pow(int log){
	int res = 1;
	for(int i = 0; i < log; i++){
		res*=10;
	}
	return res;
}

inline int rot(int a,int log){
	return a/10 + pow(log)*(a%10);
}

int main(){
	/*while(1){
		int a;
		cin>>a;
		int k = log10(a);
		for(int i = 0; i < 10; i++){
			a = rot(a,k);
			cout<<a<<endl;
		}
	}*/
	int T;
	scanf("%d",&T);
	for(int X = 1; X <= T; X++){
		memset(p,0,sizeof(p));
		int A,B;
		long long ans = 0;
		scanf("%d%d",&A,&B);
		for(int i = max(A,10); i <= B; i++){
			if(!p[i]){
				long long res = 0;
				p[i] = true;
				int k = log10(i);
				int num = rot(i,k);
				while(i!=num){
					if(A<=num && num<=B && k == (int)log10(num)){
						p[num] = true;
						res++;
						//cout<<num<<endl;
					}
					num = rot(num,k);
					//cout<<num<<endl;
				}
				//cout<<res<<endl;
				ans += res*(res+1)/2;
			}
		}
		printf("Case #%d: %lld\n",X,ans);
	}
	return 0;
}
