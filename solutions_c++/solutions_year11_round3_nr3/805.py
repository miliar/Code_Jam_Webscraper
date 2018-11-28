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
		int n,l,h;cin>>n>>l>>h;
		int a[n];
		for(int i=0;i<n;i++) cin>>a[i];
		
		int flag=-1;
		for(int i=l;i<=h;i++){
			int c=0;
			for(int j=0;j<n;j++) if( i%a[j]==0 || a[j]%i==0 ) ; else { c=1;break;}
			if( c==0 ){
				flag=i; break;
			}
		}
		
		printf("Case #%d: ",iddd++);
		if( flag==-1 ) cout<<"NO\n";
		else cout<<flag<<endl;
	}
	return 0;
}
//~vish ( vikas.cse.nitt@gmail.com )
