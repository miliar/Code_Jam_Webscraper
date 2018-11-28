#include<algorithm>
#include<bitset>
#include<cassert>
#include<cmath>
#include<complex>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<fstream>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<vector>
#include<climits>
#define LL long long
using namespace std;

char s[55][55];

int main (){
	int testCase; scanf("%d",&testCase); int iddd=1;
	while( testCase-- ){
		int n,m; cin>>n>>m;
		
		for(int i=0;i<n;i++) scanf("%s",s[i]);
		int flag=0;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				if( s[i][j]=='#' ) {	//cout<<i<<" "<<j<<endl;
					if( j+1<m && i+1<n && s[i][j+1]=='#' && s[i+1][j]=='#' && s[i+1][j+1]=='#' ) {
						s[i][j]='/'; 
						s[i][j+1]='\\'; 
						s[i+1][j]='\\' ; 
						s[i+1][j+1]='/' ;//cout<<"lin"<<endl;
					}
					else {
						flag=1; i=j=10000;
					}
				}
		
		
		
		printf("Case #%d:\n",iddd++);
		if( flag ){ 
			cout<<"Impossible"<<endl;
			
		}
		else {
			for(int i=0;i<n;i++)
				cout<<s[i]<<endl;
		}
		
	}
	return 0;
}
//~vish ( vikas.cse.nitt@gmail.com )
