#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int n,m,test,cur = 1;
int num[10000];
int main(){
	freopen("D-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	for ( scanf("%d",&test) ; cur <= test ; cur++ ){
		printf("Case #%d: ",cur);
		scanf("%d",&n);
		m = 0;
		for ( int i = 1 ; i <= n ; i++ ) scanf("%d",&num[i]);
		for ( int i = 1 ; i <= n ; i++ )
			if (i!=num[i]) m++;
		printf("%d.000000\n",m);
	}
}
