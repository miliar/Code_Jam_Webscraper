#include<iostream>
#include<cstdio>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<functional>
#include<complex>
#include<iomanip>
#include<numeric>
#include<cassert>
#include<cstring>
#include<cmath>
#include<ctime>
#include<cctype>
#include<utility>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<set>
#include<list>
#include<bitset>
#include<map>

using namespace std;

template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> T gcd( T a , T b ){ return b==0?a:gcd(b,a%b);}

const double pi=acos(-1.0);
const double eps=(1e-9);
const int Dx[8]={-1,0,1,0,-1,1,1,-1};
const int Dy[8]={0,1,0,-1,1,1,-1,-1};
const int MAXN = 310000;
const int MAXM = 105 ;
const double inf = 1e50;

typedef long long LL ; 
//typedef __int64 LL ;

int child[MAXN][26] , tp = 0 ;// end[310000]
bool in[MAXN] ;
int D,L,N;

char word[505];

int newChild() {
	for(int i=0; i<26; i++) child[tp][i] = 0;
	return tp++;
}
int Insert( char* s ){
	int p ;
	for( p = 0; *s ; s++) {
		int q = *s - 'a' ;
		if(child[p][q] == 0) 
			child[p][q] = newChild();
		p = child[p][q];
	}
//	end[p] ++ ;
	return 1;
}

int Get( char*s ){
	memset( in , false , sizeof(in) ) ;
	queue<int> Q ;
	Q.push( 0 ) ; in[0] = true ;
	while( *s ){
		vector<int> next;
		if( *s == '(' ){ s++ ;
			while( *s != ')' )
				next.push_back( *s-'a' ) , s++ ;
			s++;
		}
		else
			next.push_back( *s-'a' ) ,s++;
		int sz = Q.size() ;
		while( sz -- ){
			int p = Q.front() ; Q.pop() ;
			for( int i = 0 ; i < next.size() ;  i++ ){
				int t = child[p][next[i]] ;
				if( t != 0 && !in[t]  )
					Q.push( t ),in[t] = true;
			}
		}
	}
	return Q.size() ;
}
int main(){
	//int cases ; scanf("%d",&cases)
	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);
	while( scanf("%d%d%d",&L,&D,&N ) != EOF ){
		tp = 0 ; newChild();
		for( int i = 0 ; i < D ; i ++ ){
			scanf("%s",word );
			Insert( word ) ;
		}
		for( int i = 1 ; i <= N ; i ++ ){
			scanf("%s",word);
			printf("Case #%d: %d\n",i,Get( word ) );
		}
	}
}
