#include <string.h>
#include <math.h>
#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;


void Kevinew(){
#ifndef  ONLINE_JUDGE
	freopen("C:\\TDdownload\\C-small-attempt0.in","r",stdin);
	freopen("C:\\TDdownload\\C-small-attempt0.out","w",stdout);
#endif
}





int main(){
	int  icase,flag[110],nflag;
	int ncase,nS,n,ans;
	double temp; 
	int hash[50] = {0, 0, 27, 143, 751, 935, 607, 903, 991, 335, 47, 943, 471, 55, 447, 463, 991, 95, 607, 263, 151, 855, 527, 743, 351, 135, 407, 903, 791, 135, 647};

	Kevinew();
	scanf("%d\n",&ncase);
	for(icase=0;icase<ncase;icase++) {
		
		scanf("%d\n",&n);
		temp=pow(3+sqrt(5.0),n); 
		ans =(int) temp;
		ans %= 1000;
		
		if (hash[n]<100)
		{
			printf("Case #%d: 0%d\n",icase+1,hash[n]);
		}else 
		printf("Case #%d: %d\n",icase+1,hash[n]);

	}

	return 0;

}


