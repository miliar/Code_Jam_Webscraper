#include<iostream>
#include<cstdlib>
#include<cstdio>
using namespace std;
int T;
long long int PG,PD;
long long int N;
bool chk(){
    if(PG==100){
	if(PD==100) return 1;
	else return 0;
    }else if(PG==0){
	if(PD==0)  return 1;
	else return 0;
    }else{
	if(N>=100) return 1;
	else{
	    int nn = (int)N;
	    for(int D=1;D<=nn;D++){		
		if((D * PD) % 100 ==0){
		    return 1;
		}
	    }
	}
	return 0;
    }
}
int main(){
    int f=0;
    scanf("%d",&T);
    while(T--){
	scanf("%I64d%I64d%I64d",&N,&PD,&PG);
	printf("Case #%d: ",++f);
	if(chk()) puts("Possible");
	else puts("Broken");
    }
}
