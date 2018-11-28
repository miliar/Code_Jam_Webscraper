#include<iostream>
#include<cmath>
#include<algorithm>
#include<cctype>
#include<vector>
#include<cassert>
#include<set>
#include<string>
#include<ctime>
#include<map>
using namespace std;

vector<int> g[1000] ;
int mark[1000] ;
void dfs ( int x ){
	mark[x] = 1;
	for ( int i=0 ; i<g[x].size() ; i++ ){
		if ( mark[g[x][i]] == 0 )
			dfs ( g[x][i] );
		else
			throw 1;
	}

	mark[x] = 2;
}
int main (){
	//freopen ( "A-small-attempt0.in" , "r" , stdin );
	//freopen ( "A-small-attempt0.out" , "w" , stdout ) ;
	freopen ( "A-large.in" , "r" , stdin );
	freopen ( "A-large.out" , "w" , stdout );
	int tc;
	cin >> tc;
	for ( int C = 1 ; C<=tc ; C++ ){
		int n ;
		cin >> n ;
		for ( int i=0 ; i<n ; i++ )
			g[i].clear();
		for ( int i=0 ; i<n ; i++ ){
			int dg;
			cin >> dg;
			for ( int j=0 ; j<dg ; j++ ){
				int adj ;
				cin >> adj;
				g[i].push_back(adj-1);
			}
		}
		bool ok = true ;
		try{
			for ( int i=0 ; i<n ; i++ ){
				memset(mark,0,sizeof mark);
				dfs(i);
			}
		}catch (...){
			ok = false;
		}
		cout << "Case #" << C << ": " << (ok?"No":"Yes") << endl;
	}
	

	
}