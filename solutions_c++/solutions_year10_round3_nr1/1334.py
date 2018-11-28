/* GCJ' 10 File Fix-it
 * Radar798
 */
#include<stdio.h>
	long T;
    long  N[100];
	long a[100][500000],b[30][500000];

void init(){
	scanf("%ld",&T);
	for(long i=1;i<=T;i++){
		scanf("%ld",&N[i]);
		for(long j=1;j<=N[i];j++)scanf("%ld %ld",&a[i][j],&b[i][j]);
	}
}

void file(long m){
         long k=0;
	    for(long p=1;p<=N[m];p++)
		for(long q=p+1;q<=N[m];q++)
		{{	 
	 		 if(a[m][p]<a[m][q]&&b[m][p]>b[m][q])k++;	
		     else if(a[m][p]>a[m][q]&&b[m][p]<b[m][q])k++;
		}}
	printf("Case #%ld: %ld\n",m,k);
}

int main(void){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	init();
	for(long a=1;a<=T;a++)file(a);
    return 0;
}	
