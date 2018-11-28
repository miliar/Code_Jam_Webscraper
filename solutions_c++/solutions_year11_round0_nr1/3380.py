//

#include<cmath>
#include<vector>
#include<utility>
#include<cstring>
#include<iostream>
#include<algorithm>

using namespace std;

int main() {
     freopen("A-large (1).in","r",stdin);
	 freopen("test.out","w",stdout);

	 char c;
	 int ca,n,o,b,num,lo,lb,cnt(1),res;
	 cin>>ca;
	 while( ca-- ) {
		 cin>>n;
		 lo=lb=1;
		 o=b=0;

		 while( n-- ) {
			 cin>>c>>num;
			 if( c=='O' ) {
				 o+=abs(num-lo);
				 lo=num;

				 if( o<b ) o=b;

				 o+=1;
			 }
			 else {
				 b+=abs(num-lb);
				 lb=num;

				 if( b<o ) b=o;

				 b+=1;
			 }
		 }

		 if( o<b ) res=b;
		 else      res=o;

		 printf("Case #%d: %d\n",cnt++,res);
	 }



     
     return 0;
}