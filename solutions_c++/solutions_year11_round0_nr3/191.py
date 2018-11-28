#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int T,n,f=0;
long long int num,sum,mn,tmp;
int main(){
    scanf("%d",&T);
    while(T--){
	scanf("%d",&n);
	mn = 2147483647;
	tmp = 0;
	sum = 0;
	for(int i=0;i<n;i++){
	    scanf("%I64d",&num);
	    tmp^=num;
	    if(mn>num){
		mn = num;
	    }
	    sum+=num;
	}
	printf("Case #%d: ",++f);
	if(tmp!=0){
	    printf("NO\n");
	}else{
	    printf("%I64d\n",sum-mn);
	}
    }
}
