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

long long calc( int a, int b, int c, int d ){
	int t1=max(a,c), t2=min(b,d);
	if ( t2>=t1 ) return t2-t1+1; else return 0;
}

long long A1,A2,B1,B2;
int f[1001000];

int main(){
	f[1]=1; int now=0;
	for ( int i=2; i<=1000000; ++i ){
		while ( now+1<i && f[now+1]<i ) ++now;
		f[i]=i+now;
	}
	//for ( int i=1; i<=6; ++i ) printf("%d %d\n", i, f[i]);
	int test=0;
	scanf("%d", &test);
	for ( int T=1; T<=test; ++T ){
		cin>>A1>>A2>>B1>>B2;
		long long ans=(A2-A1+1)*(B2-B1+1);
		for ( int i=A1; i<=A2; ++i ){
			long long t=calc(i,f[i],B1,B2);
			ans-=t;
		}
		for ( int i=B1; i<=B2; ++i ){
			long long t=calc(i+1,f[i],A1,A2);
			ans-=t;
		}
		cout<<"Case #"<<T<<": "<<ans<<endl;
	}
}
