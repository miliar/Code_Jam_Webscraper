#include<fstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<queue>
using namespace std;

long long t,m,n;
int pd,pg,pf,fu;
bool ok,done;
int main()
{
	long long i,j,k;
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	scanf("%lld",&t);
	for(k=1;k<=t;k++){
		scanf("%lld%d%d",&n,&pd,&pg);
		printf("Case #%lld: ",k);
		if((pd!=100 && pg==100) || (pd!=0 && pg==0)){
			printf("Broken\n");
			continue;
		}
		if(n>100)
		         n=100;
		ok=0;done=0;
		for(i=1;i<=n;i++){
			if(i*pd%100==0){
				printf("Possible\n");
				break;
			}
			if(i==n)printf("Broken\n");
		}
	}
	return 0;
}
