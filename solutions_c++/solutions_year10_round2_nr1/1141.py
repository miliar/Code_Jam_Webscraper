#include <iostream>
#include <string>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;

int n, m;
char str[10010];
map<string,int> dict;

int main(){
	int test;
	
	freopen("A.in", "r", stdin );
	freopen("b.txt", "w", stdout );
	
	scanf("%d",&test );
	for( int te= 1; te<= test; ++te ){
		scanf("%d%d",&n,&m );
		dict.clear();
		
		for( int i= 1; i<= n; ++i ){
			scanf("%s", str );
			int len= strlen(str), j= 1, num= 1;
			
			string tot;
			while( j< len ){
				string ts;
				
				while( j< len && str[j]!= '/' ) ts= ts+ str[j++]; 
				ts= ts+ '/'; j++;	
				
				tot.append( ts );
				dict[tot]= 1;
			}
		}
		
		int ans= 0;
		for( int i= 1; i<= m; ++i ){
			scanf("%s",str);
			
			string tot;
			
			int len= strlen(str), j= 1, num= 1;
			while( j< len ){
				string ts;
				
				while( j< len && str[j]!= '/' ) ts= ts+ str[j++]; 
				ts= ts+ '/'; j++;	
				
				tot.append( ts );
				if( dict[tot]== 0 ){
					ans++; dict[tot]= 1; }
			}
		}

		printf("Case #%d: %d\n", te, ans );
	}
	
//	while(1);
	return 0;
}
