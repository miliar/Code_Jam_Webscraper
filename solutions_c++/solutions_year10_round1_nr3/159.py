#include <cstdio>

bool win(int a,int b){
    if(a > b){
	return win(b,a);
    }
    
    int q = b/a;
    if(q > 1){
	return true;
    }
    
    int r = b-a*q;
    if(r == 0){
	return false;
    }
    return !win(r,a);
}

int main(){
    int t;
    scanf("%d",&t);
    
    for(int lp=1;lp<=t;++lp){
	int a1,a2,b1,b2;
	scanf("%d %d %d %d",&a1,&a2,&b1,&b2);
	int ret = 0;
	for(int i=a1;i<=a2;++i){
	    for(int j=b1;j<=b2;++j){
		if(win(i,j)){
		    ++ret;
		}
	    }
	}
	
	printf("Case #%d: %d\n",lp,ret);
	
    }
    return 0;
}