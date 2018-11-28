#include<cstdio>
#include<algorithm>
using namespace std;

int main(){
	
	int T;
	
	scanf("%d\n",&T);
	
	for(int testcase=1;testcase<=T;testcase++){
		long long N;
		int PD,PG;
		scanf("%lld %d %d\n",&N,&PD,&PG);
		bool flag;
		if(PD==0&&PG==0)
			flag=true;
		else if(PD==100&&PG==100)
			flag=true;
		else {
			if(N>100)
				N=100;
			flag=false;
			for(int i=1;i<=N;i++)
				if((PD*i)%100==0&&PG!=100&&PG!=0)
					flag=true;
		}
		
		printf("Case #%d: ",testcase);	
		if(flag)printf("Possible\n");
		else printf("Broken\n");
	}
	
	return 0;
}
