#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<string>

using namespace std;

int num[2000];
int vst[2000];
int main(){
    freopen("F://D-large.in","r",stdin);
    freopen("F://D-large.out","w",stdout);
	int t ;
	scanf("%d",&t);
	for(int cases =1 ; cases <= t ;++cases){
		int n ; 
		scanf("%d",&n);
		double tres = 0 ; 
		for(int i = 1; i<=n ;++i){scanf("%d",&num[i]);if( i != num[i] ) tres += 1 ;}
		printf("Case #%d: %.6f\n",cases,tres);
	}
	return 0 ;
}