#include<iostream>
#include<algorithm>
#include<cmath>
#define MAX 20
using namespace std;
int n,k,p,temp;
int main(){
//	freopen("A-large.in","r",stdin);
//	freopen("b.txt","w",stdout);
	int tc,flag;
	scanf("%d",&tc);
	for(int z=0;z<tc;z++){
		scanf("%d %d",&n,&k);
		p=pow(2,n);
		flag=0;
		temp=p-1;
		if(k==temp) flag=1;
		if(k>temp){
			if(((k-temp)%p)==0) flag=1;
		}
			
		if(flag)
			printf("Case #%d: ON\n",z+1);
		else 
			printf("Case #%d: OFF\n",z+1);

		


	}
	return 0;
}