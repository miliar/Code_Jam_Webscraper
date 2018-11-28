#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

#define all(c) ((c).begin()), ((c).end()) 
#define present(c, e) ((c).find((e)) != (c).end()) 
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define inf (1<<29)

int gcd (int a,int b) {
	while (b) {
		a %= b;
		swap(a,b);
	}
	return a;
}

int C,N;

int a[1007];
int b[1007];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&C);
	for(int i=1;i<=C;i++){
		scanf("%d",&N);	
		for(int j=0;j<N;j++) 
			scanf("%d",&a[j]);
		sort(a,a+N);

		for(int j=1;j<N;j++)
	    		b[j-1]=a[j]-a[j-1];

		int T=gcd(b[0],b[1]); 
		for(int j=2;j<N-1;j++)	
			T=gcd(T,b[j]);
                if(N==2) T=b[0];
		int  mx = 0;
		for(int j=0;j<N;j++){
			int x=a[j]/T;
			if(a[j]%T) x++;
			mx=max(((T*x)-a[j]),mx);
		}
		printf("Case #%d: %d\n",i,mx);
	}			

		
	
	return 0;
}
