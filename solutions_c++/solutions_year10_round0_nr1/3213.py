#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <math.h>
#include "stdio.h"
using namespace std ;

int main(){

	long long int a[]={0,0,1
		,3
		,7
		,15
		,31
		,63
		,127
		,255
		,511
		,1023
		,2047
		,4095
		,8191
		,16383
		,32767
		,65535
		,131071
		,262143
		,524287
		,1048575
		,2097151
		,4194303
		,8388607
		,16777215
		,33554431
		,67108863
		,134217727
		,268435455
		,536870911
	    ,1073741823};
int i=0,b=0,c=0,d=0,t=0,n=0;
long long int k=0,q=0;

FILE *sf,*rf;

sf=fopen("j:\\alarge.in","r");
rf=fopen("j:\\olarge12.txt","w+");

fscanf(sf,"%d",&t);
//scanf("%d",&t);

for(int i1=1;i1<t+1;i1++){

fscanf(sf,"%d %lld",&n,&k);
//scanf("%d %lld",&n,&k);

 { for(i=0;i<10000000;i++){
             q=(a[n+1]*i)+(i-1);
            if(q==k)
                {fprintf(rf,"Case #%d: ON\n",i1);
                //fprintf(rf,"Case #%d: ON\n",i1);printf("ON %d  %lld\n",n,k);
                break;}
            else if(q>k)
               {//fprintf(rf,"Case #%d: OFF\n",k);
               fprintf(rf,"Case #%d: OFF\n",i1);break;}
            else
               continue;
        }}
}
 fclose(rf);
fclose(sf);
    return 0;
}
