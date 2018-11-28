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

int main (){
	int testCase; scanf("%d",&testCase); int iddd=1;
	while( testCase-- ){
		int n;scanf("%d",&n);
		char a[n][3]; int b[n];
		for(int i=0;i<n;i++)
			scanf("%s %d",a[i],&b[i]);
			
		int op=1,bp=1;
		int t[n+1],O,B; O=B=n; t[n]=0;
		for(int i=0;i<n;i++){
			if( a[i][0]=='O'){ 
				t[i]=abs(op-b[i])+t[O]; 
				O=i; op=b[i];
			}
			else{ 
				t[i]=abs(bp-b[i])+t[B]; 
				B=i; bp=b[i];
			}
			
			if(i && t[i]<t[i-1] ) t[i]=t[i-1];
			t[i]++;		
		}
		printf("Case #%d: %d\n",iddd++,t[n-1]);
	
	}
	return 0;
}
//~vish ( vikas.cse.nitt@gmail.com )
