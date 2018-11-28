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
		
		scanf("%d",&n);
		int s=0;
		int sum=0;
		int x=-1;
		foru(i,1,n) {
			scanf("%d",&j);
			s^=j;
			sum+=j;
			if (x<0 || j<x) x=j;
		}
		if (s!=0) printf("NO\n");
		else printf("%d\n",sum-x);
	}
}    
