#include<set>
#include<string>
#include<iostream>
using namespace std;
int test;
set<string> yala;
int total;
void f( string s ){
	//cout<<s<<endl;
	if( yala.find( s ) != yala.end() )return;
	total++;
	yala.insert( s );
	int L = s.length(); 
	int pos;
	for( int j = L - 1; j >=0; --j ){
		if( s[ j ] == '/' ){
			pos = j;
			break;
		}
	}
	f(s.substr(0,pos));
}
void doit(){
	int n,m;
	cin>>n>>m;
	total = 0;
	yala.clear();
	yala.insert( "" );
	for( int i = 0; i < n; ++i ){
		string s;
		cin>>s;
		yala.insert( s );
	}
	for( int i = 0; i < m; ++i ){
		string s;
		cin>>s;
		f( s );
	}
	cout<<"Case #"<<test++<<": "<<total<<endl;
}
int main(){
	int T;
	cin>>T;
	test = 1;
	for( int i = 0; i < T; ++i ){
		doit();
	}
}
