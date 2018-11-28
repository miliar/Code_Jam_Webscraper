#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <string.h> 
#include <string>
#include <vector> 
#include <iostream>
#include <sstream>
#include <queue>
using namespace std;

long a,b,d,n,i,k,c,i1,k1,j,m,l,h,w;
long t,cas,k0;
char we[1000];
long tb[20],ta[20];


int main() { //convex hull
//	freopen( "c:\\wojtek\\uva\\uva\\debug\\t1.in", "rt", stdin);
		//int czas=clock();
	

	//czas = clock() - czas;
	//printf("%lf\n",double(czas)/CLOCKS_PER_SEC);
	//while(1){
	
	scanf("%ld",&t);
	
	gets(we);
	for(cas=1;cas<=t;cas++){

		gets(we);

		k=strlen(we);

		for(i=0;i<20;i++){
			tb[i]=0;
			ta[i]=0;
		}

		d=0;

		for(i=0;i<k;i++){
			if(we[i]=='w'){
				tb[0]++;
				ta[0]++;
			}
			else if(we[i]=='e'){
				tb[1]++;
				ta[1]+=ta[0];
				ta[1]%=10000;
				tb[6]++;
				ta[6]+=ta[5];
				ta[6]%=10000;
				
				tb[14]++;
				ta[14]+=ta[13];
				ta[14]%=10000;
				
			}
			else if(we[i]=='l'){
				tb[2]++;
				ta[2]+=ta[1];
				ta[2]%=10000;
			}
			else if(we[i]=='c'){
				tb[3]++;
				ta[3]+=ta[2];
				ta[3]%=10000;
				
				tb[11]++;
				ta[11]+=ta[10];
				ta[11]%=10000;
				
			}
			else if(we[i]=='o'){
				tb[4]++;
				ta[4]+=ta[3];
				ta[4]%=10000;
				tb[9]++;
				ta[9]+=ta[8];
				ta[9]%=10000;
				tb[12]++;
				ta[12]+=ta[11];
				ta[12]%=10000;
				
			}
			else if(we[i]=='m'){
				tb[5]++;
				ta[5]+=ta[4];
				ta[5]%=10000;
				tb[18]++;
				ta[18]+=ta[17];
				ta[18]%=10000;
				d+=ta[18];
				d%=10000;
				

			}
			else if(we[i]==' '){
				tb[7]++;
				ta[7]+=ta[6];
				ta[7]%=10000;
				tb[10]++;
				ta[10]+=ta[9];
				ta[10]%=10000;
				tb[15]++;
				ta[15]+=ta[14];
				ta[15]%=10000;

			}
			else if(we[i]=='t'){
				tb[8]++;
				ta[8]+=ta[7];
				ta[8]%=10000;
				
			}
			else if(we[i]=='d'){
				tb[13]++;
				ta[13]+=ta[12];
				ta[13]%=10000;
				
			}
			else if(we[i]=='j'){
				tb[16]++;
				ta[16]+=ta[15];
				ta[16]%=10000;
				
			}
			else if(we[i]=='a'){
				tb[17]++;
				ta[17]+=ta[16];
				ta[17]%=10000;
				
			}
		}

		
		d=ta[18];
		d%=10000;
		

		printf("Case #%ld: %.4ld\n",cas,d);
		


	}



	
	return 0;
} 
