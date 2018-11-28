#include <stdio.h>
using namespace std;

void solve(){
	int a,b,digs=0;
	scanf("%d %d",&a,&b);
	for (int x=a;x!=0;x/=10) digs++;
	int tot = 0;
  int pow = 1;
	for (int j=1;j<digs;j++) pow*=10;
	for (int i=a;i<b;i++){
   	 int x = i;
		 while ( 1 ){   
			x = (x % 10) * pow + x/10;
			if ( x== i ) break;
			tot+= (x>i  && x<=b);
		 }
	}
  printf("%d",tot);
}

int main(){
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++){
		printf("Case #%d: ",i);
		solve();
		putchar('\n');
	}
	return 0;
}
