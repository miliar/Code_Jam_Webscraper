#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <map>
#include <queue>
#include <algorithm>
#include <sstream>
#include <vector>

using namespace std;

int M[150][150];
int n;
int tot;

bool ok(){
	for ( int i=0; i<=120; ++i )
		for ( int j=0; j<=120; ++j )
			if ( M[i][j] ) return true;
	return false;
}

int main(){
	int test=0;
	scanf("%d", &test);
	for ( int T=1; T<=test; ++T ){
		scanf("%d", &n);
		for ( int i=0; i<n; ++i ){
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2); 
			for ( int j=x1; j<=x2; ++j )
				for ( int k=y1; k<=y2; ++k )
					M[j][k]=1;
		}
		int ans=0;
		while ( ok() ){
			++ans;
			for ( int i=120; i>=0; --i )
				for ( int j=120; j>=0; --j ){
					int t1=0,t2=0;
					if ( i>0 ) t1=M[i-1][j];
					if ( j>0 ) t2=M[i][j-1];
					if ( ! M[i][j] ){
						if ( t1 && t2 )
							M[i][j]=true;
					} else
						if ( ! t1 && ! t2 )
							M[i][j]=false;
				}
		}
		printf("Case #%d: %d\n" , T, ans);
	}
}
