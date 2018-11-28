#include<cstdio>
bool test(__int64 n,int pd,int pg){
	if(pd!=0&&pg==0){
		return false;
	}
	if(pd!=100&&pg==100){
		return false;
	}
	if(n>=100){
		return true;
	}
	for(int i=n;i>0;--i){
		if(i*pd%100==0){
			return true;
		}
	}
	return false;
}
int main(){
	int T;
	scanf("%d",&T);
	for(int nCase=1;nCase<=T;++nCase){
		__int64 n;
		int pd,pg;
		scanf("%I64d%d%d",&n,&pd,&pg);
		printf("Case #%d: %s\n",nCase,test(n,pd,pg)?"Possible":"Broken");
	}
	return 0;
}