#include<iostream>
#include<vector>
#include<deque>
#include<map>
using namespace std;
long long doit(){
	int R,k,n;
	cin>>R>>k>>n;
	map< deque< int >, int > m;
	deque< int > v( n );
	for( int i = 0; i < n; ++i ){
		cin>>v[ i ];
		m[ v ] = 0;
	}
	int ciclo;
	int offset;
	vector< long long > tot( n + 1, 0 );
	for( int i = 1; i <= n; ++i ){
		int index = 0;
		while( index < n && tot[ i - 1 ] + v.front() <= k ){
			tot[ i - 1 ]+=( long long )v.front();
			index++;
			v.push_back( v.front() );
			v.pop_front();
		}
		/*for( int j = 0; j < n; ++j ){
			cout<<v[ j ]<<" ";
		}
		cout<<endl;*/
		if( m.find( v ) != m.end() ){
			offset = m[ v ];
			ciclo = i - offset;
			break;
		}
		m[ v ] = i;
	}
	/*cout<<offset<<endl;
	for( int i = 0; i < offset; ++i ){
		cout<<tot[ i ]<<" ";
	}
	cout<<endl;
	cout<<ciclo<<endl;
	for( int i = offset; i < offset + ciclo; ++i){
		cout<<tot[ i ]<<" ";
	}
	cout<<endl;*/
	long long ret = 0;
	for( int i = 0; i < offset; ++i ){
		ret += tot[ i ];
	}
	R-=offset;
	long long TOT = 0;
	for( int i = 0; i < ciclo; ++ i ){
		TOT += tot[ i + offset ];
	}
	ret += TOT*( long long )( R / ciclo );
	for( int i = 0; i < R % ciclo; ++i ){
		ret += tot[ i + offset ];
	}
	return ret;
}
int main(){
	int T;
	cin>>T;
	for( int i = 1; i <= T; ++i ){
		cout<<"Case #"<<i<<": "<<doit()<<endl;
	}
}
