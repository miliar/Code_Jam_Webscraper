/*
TASK: snapper
LANG: C++
*/
#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <set>
#include <queue>
#include <cstring>
#include <algorithm>
#define foreach(_v,_c) for( typeof((_c).begin()) _v = (_c).begin() ; _v != (_c).end() ; ++_v )

using namespace std;

int getStatus( int N , int K ){
    return K % ( 1 << N ) == ( 1 << N ) - 1;
}

int main(){
	freopen("snapper.in","r",stdin);
	freopen("snapper.out","w",stdout);
	int T;
	scanf("%d",&T);
	for( int i = 0 ; i < T ; i++ ){
        int N,K;
        scanf("%d%d",&N,&K);
        printf("Case #%d: ", i+1);
        if( getStatus( N , K ) )
            printf("ON\n");
        else
            printf("OFF\n");
	}
	return 0;
}
