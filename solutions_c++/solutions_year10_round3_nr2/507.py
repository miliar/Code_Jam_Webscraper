#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
int test ;
int t[11][1001][1001];
int f( int z,int x,int y ){
	if( y <= z * x )return 0;
	int &ret = t[ z ][ x ][ y ];
	if( ret != -1 )return ret;
	int mini = 10000;
	for( int i = x + 1; i < y; ++i){
		mini = min( mini, max( f( z, i, y ), f( z, x, i ) ) );
	}
	ret = mini + 1;
	return ret;
}
void doit(){
	//memset( t, -1, sizeof( t ) );
	int L,P,C;
	cin>>L>>P>>C;
	cout<<"Case #"<<test++<<": "<<f( C, L, P )<<endl;
}
void precalc(){
	memset( t, -1, sizeof( t ) );
	for( int c = 2; c < 11; ++c ){
		for( int i = 1; i < 1000; ++i ){
			//cout<<i<<endl;
			for( int j = i + 1; j < 1001; ++j ){
				f( c, i, j );
			}
		}
	}
}
int main(){
	//puts("hola");
	precalc();
	test = 1;
	int T;
	cin>>T;
	for( int i = 1; i <= T; ++i ){
		doit();
	}
}
