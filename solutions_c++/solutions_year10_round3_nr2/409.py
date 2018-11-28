#include<iostream>
#include<cmath>
using namespace std;

int main(){
//	freopen("D:\\in.txt","r",stdin);		//////
//	freopen("D:\\B-small-attempt1.in","r",stdin);	//////
//	freopen("D:\\B-small-attempt1.out","w",stdout);	//////
	freopen("D:\\B-large.in","r",stdin);	//////
	freopen("D:\\B-large.out","w",stdout);	//////
	int t,l,p,c,res;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%d%d%d",&l,&p,&c);
		int temp=ceil(log10(p/(double)l)/log10((double)c));
		res=ceil(log10((double)temp)/log10(2.));
		printf("Case #%d: %d\n",i,res);
	}
	return 0;
}