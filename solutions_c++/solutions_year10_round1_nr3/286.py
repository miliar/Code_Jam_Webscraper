#include<algorithm>
#include<stdlib.h>
#include<stdio.h>
#include<cmath>
#include<cstring>
#include<string.h>
#include<time.h>
#include<vector>
#include<queue>
#include<list>
#include<stack>
#include<set>
#include<map>
#include<iostream>
using namespace std;

const int INF = (1<<25);

int Gcd( int a, int b ){
	if( a < b ) swap( a, b );
	while( b!=0 ){ swap( a, b ); b %= a; }
	return a;
}

bool win( int a, int b ){
	if( a<b ) swap( a, b );
	if( a==b ) return false;
	if( a%b==0 ) return true;

	int k = a/b;
	bool ok = win( b, a-k*b );
	if( k==1 ) return !ok;
	else return true;
	/*if( a-a/b*b == 1 ){
		if( a/b==1 ) return false;
		else return true;
	}

	for(int i=1; i<=a/b; i++){
		if( !win(a-i*b,b) ) return true;
	}
	return false;*/
}

int main(){
	freopen("C:\\Users\\zgm\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\zgm\\Desktop\\out.txt","w",stdout);
	int T, a1, a2, b1, b2;
	scanf("%d",&T);
	for(int tt=1; tt<=T; tt++){
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		int num = 0;
		for(int i=a1; i<=a2; i++){
			for(int j=b1; j<=b2; j++){
				if( win(i/Gcd(i,j),j/Gcd(i,j)) ) num++;
			}
		}
		printf("Case #%d: %d\n",tt,num);
	}
	return 0;
}
