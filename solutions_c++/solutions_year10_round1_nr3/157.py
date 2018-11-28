#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

bool chk(int a, int b){
	if(a == 0 || b== 0)
		return 1;
	if(a < b)
		swap(a,b);
	if(!chk(a%b,b))
		return 1;
	if(a>=2*b){
		return !chk(a%b+b,b);
	}else{
		return 0;
	}
}

int main(){
	int T;
	scanf("%d",&T);
	for(int TT = 1; TT <=T; TT++){
		int a1,a2,b1,b2;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		int ret=0;
		for(int i=a1;i<=a2;i++){
			for(int j=b1;j<=b2;j++){
				if(chk(i,j)){
					ret++;
				}
			}
		}
		printf("Case #%d: %d\n", TT, ret);
	}
}