#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<string>

using namespace std;

int num[200];
int main(){
	freopen("D://C-small-attempt0.in","r",stdin);
    freopen("D://C-small-attempt0.out","w",stdout);
	int t ; 
	scanf("%d",&t);
	for(int cases = 1 ; cases<=t;++cases){
		int L , R ; 
		int n ; 
		scanf("%d%d%d",&n,&L,&R);
		for(int i = 0 ; i<n ;++i)scanf("%d",&num[i]);
		int res = -1 ;
		for(int i = L ; i<=R;++i){
			bool sta = 0 ; 
			for(int j = 0  ; j<n&&sta==0 ;++j){
				if( num[j] % i == 0 || i % num[j] ==0 )
					;
				else 
					sta = 1 ; 
			}
			if( sta == 0 ){res =i; break;}
		}
		if( res ==-1)
		printf("Case #%d: NO\n",cases);
		else printf("Case #%d: %d\n",cases,res);
	}
	return 0;
}