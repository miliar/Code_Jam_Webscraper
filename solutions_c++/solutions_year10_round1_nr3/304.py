#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define all(x) x.begin(),x.end()
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define bits(x) __builtin_popcount(x)

#define MAX 50
#define INF 100000000LL

long long a1,a2,b1,b2;
long long fibo[MAX];

long long inter(long long d1, long long h1, long long d2, long long h2) {
	d1=max(0LL,d1); d2=max(0LL,d2);
	if (h1<d1 || h2<d2) return 0;
	if (d2<d1) {
		swap(d1,d2); swap(h1,h2);
	}
	return max(0LL,min(h1,h2)-d2+1);
}

int main(){
	int casos,c;
	
	fibo[0]=0; fibo[1]=1;
	for (int i=2;i<MAX;i++) fibo[i]=fibo[i-1]+fibo[i-2];
	cin>>casos;
	for (c=0;c<casos;c++){
		cout<<"Case #"<<(c+1)<<": ";
		cin>>a1>>a2>>b1>>b2;
		
		long long res=0;
		
		for (int i=0;fibo[2*i+2]<=a2;i++) {
			for (long long suma=fibo[2*i+2];suma<=a2;suma+=fibo[2*i+2]) {
				long long suma2=(suma/fibo[2*i+2])*fibo[2*i+3];
				if (i>0 && b2>=suma2) res+=inter((a1-suma+fibo[2*i]-1)/fibo[2*i],(a2-suma)/fibo[2*i], (b1-suma2+fibo[2*i+1]-1)/fibo[2*i+1],(b2-suma2)/fibo[2*i+1]);
				else if (a1<=suma && b2>=suma2) res+=inter(0,INF, (b1-suma2+fibo[2*i+1]-1)/fibo[2*i+1],(b2-suma2)/fibo[2*i+1]);
			}
		}

		for (int i=0;fibo[2*i+2]<=b2;i++) {
			for (long long suma=fibo[2*i+2];suma<=b2;suma+=fibo[2*i+2]) {
				long long suma2=(suma/fibo[2*i+2])*fibo[2*i+3];
				if (i>0 && a2>=suma2) res+=inter((b1-suma+fibo[2*i]-1)/fibo[2*i],(b2-suma)/fibo[2*i], (a1-suma2+fibo[2*i+1]-1)/fibo[2*i+1],(a2-suma2)/fibo[2*i+1]);
				else if (b1<=suma && a2>=suma2) res+=inter(0,INF, (a1-suma2+fibo[2*i+1]-1)/fibo[2*i+1],(a2-suma2)/fibo[2*i+1]);
			}
		}

		cout<<res<<endl;
	}
	
	return 0;
}
