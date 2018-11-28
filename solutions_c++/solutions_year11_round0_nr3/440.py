#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>

using namespace std;

int num[2000];
int main(){
    freopen("F://C-large.in","r",stdin);
	freopen("F://C-large.out","w",stdout);
	int t ;
	scanf("%d",&t);
	for(int cases =1 ; cases <= t ;++cases){
		int n ;
		scanf("%d",&n);
		int tmp = 0 ,sum = 0 , minx = 10000000; 
		for(int i = 0 ; i<n ;++i){
			scanf("%d",&num[i]);
			tmp ^= num[i] ; 
			sum += num[i] ; 
			if( minx > num[i] )minx = num[i] ;  
		}
		if( tmp !=0 )printf("Case #%d: NO\n",cases);
		else printf("Case #%d: %d\n",cases, sum - minx );
	}
	return 0 ;
}