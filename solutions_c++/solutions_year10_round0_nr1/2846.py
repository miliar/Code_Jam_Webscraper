
#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,n,k,num,i,j,no=1;
    scanf("%d",&t);
    while(t--){
	    scanf("%d%d",&n,&k);
	    printf("Case #%d: ",no++);
	    num=1;
	    if(k==0) {
			 printf("OFF\n");
			 continue;
        }
	    for(i=0;i<n;i++){
		    num*=2;
		}
		if(k%num==num-1) printf("ON\n");
		else printf("OFF\n");
	}
    //system("pause");
    return 0;
}
