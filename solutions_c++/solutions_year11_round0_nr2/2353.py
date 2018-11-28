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

char comb[200][200],opp[200][200];

int main (){
	int testCase; scanf("%d",&testCase); int idd=1;
	while( testCase-- ){
		int c,d,n;
		char s[111];
		memset(comb,-1,sizeof(comb));
		memset(opp,-1,sizeof(opp));
		
		scanf("%d",&c);
		for(int i=0;i<c;i++){
			scanf("%s",s);
			comb[ s[0] ][ s[1] ]=s[2];
			comb[ s[1] ][ s[0] ]=s[2];
		}
		scanf("%d",&d);
		for(int i=0;i<d;i++){
			scanf("%s",s);
			opp[ s[0] ][ s[1] ]=1;
			opp[ s[1] ][ s[0] ]=1;
		}
		scanf("%d",&n); scanf("%s",s);
		vector<char> a;
		for(int i=0;i<n;i++){
			a.push_back(s[i]);
			if( a.size()>1 ){
				if( comb[ a[ a.size()-1 ] ][ a[ a.size()-2 ] ]!=-1 ){
					char ch=comb[ a[ a.size()-1 ] ][ a[ a.size()-2 ] ];
					a.pop_back(); a.pop_back(); a.push_back(ch);
				} 
				else {
					for(int j=0;j<a.size()-1;j++)
					   if( opp[ a[ a.size()-1 ] ][ a[ j ] ]!=-1 ){
						a.clear(); break;
					} 
				
				}
			}
		}
		printf("Case #%d: [",idd++);
		if( a.size() ) printf("%c",a[0]);
		for(int i=1;i<a.size();i++) printf(", %c",a[i]);
		printf("]\n");
	}
	return 0;
}
//~vish ( vikas.cse.nitt@gmail.com )
