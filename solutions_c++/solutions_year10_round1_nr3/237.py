#include<stdio.h>
/*
Google Code Jam 2010
Round 1A
Number Game
winning position: small*2<=big
step to winning position is even
lose position: a==b
*/
long iswin(long a,long b){
	long t,cnt=0;
	if(a>b){t=a;a=b;b=t;}
	while(a!=b&&a*2>b){
		t=b-a;
		b=a;
		a=t;
		cnt++;
	}
	if(a==b)return (cnt&1);
	else return !(cnt&1);
}
long segins(long a1,long a2,long b1,long b2){
	if(b2<a1||b1>a2)return 0;
	if(b2>=a2&&b1<=a1)return a2-a1+1;
	if(b2<=a2&&b1>=a1)return b2-b1+1;
	if(b1<a1)return b2-a1+1;
	return a2-b1+1;
}
long winning(long a,long b1,long b2,long cnt=0){
	long t;
	if(a<b1){
		if(a*2<=b1)return b2-b1+1;
		if(a*2<=b2)return winning(a,b1,a*2-1)+(b2-a*2+1);
		return winning(a,b1-a,b2-a,1);
	}else if(a>=b1&&a<=b2){
		if(a*2<=b2)return winning(a,b1,a-1)+winning(a,a+1,a*2-1)+(b2-a*2+1);
		else return winning(a,b1,a-1)+winning(a,a+1,b2);
	}else{
		if(b2<=a/2){
			if(cnt)return 0;
			else return b2-b1+1;
		}
		if(b1<=a/2){
			if(cnt)return winning(a,a/2+1,b2,cnt);
			else return winning(a,a/2+1,b2,cnt)+(a/2-b1+1);
		}
	}
	long lo=1,hi=a/2;
	while(hi-lo>1){
		long mid=(lo+hi)/2;
		if(iswin(mid,a-mid))lo=mid;
		else hi=mid;
	}
	if(iswin(hi,a-hi))lo=hi;
	if(!iswin(lo,a-lo))lo--;
	if((cnt&1)==0){
		return segins(lo+1,a-lo-1,b1,b2);
	}else{
		return segins(1,lo,b1,b2)+segins(a-lo,a,b1,b2);
	}
}
typedef long long I;
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	long z,zi;
	scanf("%ld",&z);
	for(zi=1;zi<=z;zi++){
		long a1,a2,b1,b2;
		scanf("%ld%ld%ld%ld",&a1,&a2,&b1,&b2);
		long a;
		I ans=0;
		for(a=a1;a<=a2;a++){
			ans+=winning(a,b1,b2);
		}
		printf("Case #%ld: %I64d\n",zi,ans);
		fflush(stdout);
	}
	return 0;
}
