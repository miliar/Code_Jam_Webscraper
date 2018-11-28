#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
int main(){
	//freopen("B-small-attempt2.in","r",stdin);
	//freopen("B-small-attempt2.out","w",stdout);
	int cas = 1,sum,T,l,p,c,cc,tem,cn;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d%d",&l,&p,&c);
		sum = 0;
		tem = p;
		cn = c;
		if(tem > c*l)
		while(1){
			if(tem % c == 0) cc = 0;
			else cc = 1;
			p = p/c+cc;
			
			sum ++;
			if(p <= l*cn) break;
			tem = p;
			c *= c;
		}
		printf("Case #%d: %d\n",cas++,sum);
	}
	return 0;
}