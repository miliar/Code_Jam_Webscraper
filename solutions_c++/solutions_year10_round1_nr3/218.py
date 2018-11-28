#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<string.h>
using namespace std;
int l[1001000],r[1001000];
bool win(int i,int x){
	if(i==x)return false;
	i-=x;
	return i>=l[x] && i<=r[x];
}
int intersect(int a1,int a2,int b1,int b2){
	if(b1>a2 || b2<a1)return 0;
	return min(a2,b2)-max(a1,b1)+1;
}
int main(){
	int times,a1,b1,a2,b2;
	l[1]=r[1]=1;
	for(int i=2;i<=1000000;i++){
		int low=i/2,high=i,mid;
		if(i&1)low++;
		while(low < high){
			mid=(low+high)>>1;
			if(win(i,mid))
				low=mid+1;
			else
				high=mid;
		}
		l[i]=low;
		r[i]=i+l[i]-1;
	}
	scanf("%d",&times);
	for(int tm=1;tm<=times;tm++){
		printf("Case #%d: ",tm);
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		long long res=0;
		for(int i=a1;i<=a2;i++){
			res+=b2-b1+1;
			res-=intersect(l[i],r[i],b1,b2);
		}
		cout<<res<<endl;
	}
	return 0;
}
