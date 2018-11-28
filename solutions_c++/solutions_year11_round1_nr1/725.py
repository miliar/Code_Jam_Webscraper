#include<iostream>
#include<cstdio>
#include<vector>

using namespace std;

int main(){
	int T,N,d,g;
	scanf("%d",&T);
	for(int I=1;I<=T;I++){
		scanf("%d%d%d",&N,&d,&g);
		int x=d,y=100;
		while(x && x%2==0 && y%2==0){
			x/=2;y/=2;
		}
		for(int i=3;i<=x;i+=2){
			while(x && x%i==0 && y%i==0){
				x/=i,y/=i;
			}
		}
		if(d==0) y=1;
		//cout<<x<<" "<<y<<endl;
		if(y>N || (g==100 && d!=100) || (g==0 && d!=0)) printf("Case #%d: Broken\n",I);
		else printf("Case #%d: Possible\n",I);
	}
	return 0;
}
