#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>


using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)

int n;

int main(){
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
   int i,j,k,test,cases;
   scanf("%d",&test);
   cases=0;
   while (test){
		test--;
		cases++;
		printf("Case #%d: ",cases);
		scanf("%d%d",&n,&k);
		int ans= k % (1<<n);
		if (ans == (1<<n)-1) printf("ON\n");
		else printf("OFF\n");
	}
   
   return 0;
}
