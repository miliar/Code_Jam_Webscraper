//

#include<vector>
#include<utility>
#include<cstring>
#include<iostream>
#include<algorithm>

using namespace std;

int gcd(int a,int b) {
	return b==0?a:gcd(b,a%b);
}



int main() {
     freopen("test.in","r",stdin);
	 freopen("test.out","w",stdout);

	 int ca,i,pd,pg,flag;
	 __int64 n,tmp;

	 scanf("%d",&ca);
	 for(i=1;i<=ca;++i) {
		 scanf("%I64d%d%d",&n,&pd,&pg);

		 flag=0;
		 tmp=100/gcd(100,pd);
		 if( tmp<=n ) {
			 flag=1;
		 }

		 if( pg==100 && pd!=100 ) flag=0;
		 if( pg==0   && pd!=0   ) flag=0;

		 printf("Case #%d: ",i);
		 if( flag ) printf("Possible\n");
		 else       printf("Broken\n");
	 }


	 
     
     return 0;
}