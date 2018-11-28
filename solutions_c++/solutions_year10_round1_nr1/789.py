#include<string>
#include<iostream>
#include<cstdio>
using namespace std;
string t[ 50 ];
string t2[ 50 ];
string t3[ 50 ];
static int di[ 4 ] = { 0, 1, 1, 1} , dj[ 4 ] = { 1, 0, 1, -1 };
int test;
void doit(){
	int n,k;
	cin>>n>>k;
	for( int i = 0; i < n; ++i ){
		cin>>t[ i ];
	}
	for( int i = 0; i < n; ++i ){
		t2[ i ] = "";
		for( int j = n-1; j >=0; --j ){
			t2[ i ]+=t[ j ][ i ];
		}
	}
	for( int j = 0; j < n; ++j ){
		string s = "";
		for( int i = 0; i < n; ++i ){
			if( t2[ i ][ j ] != '.' )s+=t2[i ][ j];
		}
		for( int i = 0; i < n - s.length(); ++i ){
			t2[ i ][ j ] = '.';
		}
		for( int i = 0; i < s.length(); ++i ){
			t2[ n - s.length() + i ][ j ] = s[ i ];
		}
	}
	/*for( int i = 0; i < n; ++i ){
		cout<<t2[ i ]<<endl;
	}*/
	bool Red = 0, Blue = 0;
	for( int i = 0; i < n; ++i )for( int j = 0; j < n; ++j ){
		for( int dir = 0; dir < 4; ++dir ){
			int i2 = i, j2 = j;
			int cRed = 0, cBlue = 0;
			for( int a = 0; a < k && i2 < n && j2 < n; ++a ){
				if( t2[ i2 ][ j2 ] == 'R' ){
					++cRed;
				}
				if( t2[ i2 ][ j2 ] == 'B' ){
					++cBlue;
				}
				i2 = i2 + di[ dir ];
				j2 = j2 + dj[ dir ];
			}
			if( cRed == k ) Red = 1;
			if( cBlue == k ) Blue = 1;
		}
	}
	cout<<"Case #"<<test<<": ";
	if( Red && Blue ){puts("Both");return;}
	if( Red ){puts("Red");return;}
	if( Blue ){puts( "Blue");return;}
	puts("Neither");
}
int main(){
	int N;
	test = 1;
	cin>>N;
	while( test <= N ){
		doit();
		test++;
	}
}

