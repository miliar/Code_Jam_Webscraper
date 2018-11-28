#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#define INF (1<<30)
#define EPS 1e-8
#define LLD long long int
using namespace std;

int c,d,n,m,a[15],p[1000005];

int mx,x,y,e,C,AC;

void gen_prime(int n){
	for (int i=2;i<=n;i++) p[i]=1;
	for (int i=2;i<=n;i++)
		if (p[i])
			for (int j=i+i;j<=n;j+=i) p[j]=0;
}


int main(){

	gen_prime(1000000);

	scanf("%d",&c);
	for (int tc=1;tc<=c;tc++){

		scanf("%d%d",&d,&n);
		mx=0;
		for (int i=0;i<n;i++) scanf("%d",&a[i]),mx=max(mx,a[i]);
		m=1;
		while (d--) m*=10;
		
//  p = i
//  a = 0..i-1 = j
//  b = y

		AC=-1;
		
		if (n==1){
			printf("Case #%d: I don't know.\n",tc);
			continue;
		}
		
		
 		for (int i=mx+1;i<=m;i++)
			if (p[i])
				for (int j=0;j<i;j++){
					x=((LLD)j*(LLD)a[0])%i;
					
					y=(a[1]-x+i)%i;
					
					e=1;
					
					for (int k=2;k<n;k++)
					    if (a[k]!=((LLD)a[k-1]*(LLD)j+(LLD)y)%i) e=0;
					
					if (e){
						C=((LLD)a[n-1]*(LLD)j+(LLD)y)%i;
						
						if (AC==-1) AC=C;
						else if (AC>=0&&AC!=C) AC=-2;
					}
					
					if (AC==-2) break;


				}

		printf("Case #%d: ",tc);
		
		if (AC==-2) printf("I don't know.\n");
		else printf("%d\n",AC);
		
		
	}
	return 0;
}
