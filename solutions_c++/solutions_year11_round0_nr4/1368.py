#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <sstream>
#include <cmath>

using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)

int n;

int main(){
	int i,j,k,test,cases=0;
	scanf("%d",&test);
	while (test){
		test--;
		cases++;
		printf("Case #%d: ",cases);
		double ans=0;
		scanf("%d",&n);
		foru(i,1,n) {
			scanf("%d",&j);
			if (j!=i) ans++;
		}
		printf("%.6lf\n",ans);
	}
}    
