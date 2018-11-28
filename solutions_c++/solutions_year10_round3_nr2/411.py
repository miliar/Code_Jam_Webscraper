#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
using namespace std;
int main(){
	int t,T=1;
	cin>>t;
	while(T<=t){
		long long int l,p,c;
		cin>>l>>p>>c;
		int cnt=0,hh=l,xx=p,result;
		float swapnil,tm;
		int y;
		y=(xx+c-1)/c;
		while(y>l){
			cnt++;
			xx=y;
			y=(xx+c-1)/c;
		}
		if(cnt==0)result=0;
		else{
			swapnil=log(cnt)/log(2)+1;
			result=swapnil;
			/*tm=result;
			if(swapnil>tm){
				result--;
			}*/
		}
		printf("Case #%d: %d\n",T,result);
		T++;
	}
	return 0;
}
