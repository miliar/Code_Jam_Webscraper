#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>
#include <sstream>
#include <map>
using namespace std;
int main(){
	long long n,m,c,i,j,t,test,T,count;
	long long x,y,z,ok,p,q,size;
	scanf("%lld",&T);
	for (test=1;test<=T;test++){
		printf("Case #%lld: ",test);
	//	printf("\n");
		scanf("%lld%lld%lld",&n,&m,&c);
		t=0;
		while(n*c<m){
			t++;
			n=n*c;
		}
		count=0;
		while(t){
			count++;
			t/=2;
		}
		printf("%lld\n",count);		
	}
  return 0;
}
