#include <iostream>
#include <vector>
#include <cstdio>
#include <set>
#include <algorithm>
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
using namespace std;
typedef long long int lld;
typedef double lf;

int t,tt,res,ruch,a,b,c,d,x,y,wygr;
int main(){
	scanf("%d",&t);
	while(t--){
		tt++;
		res=0;
		scanf("%d %d %d %d",&a,&b,&c,&d);
		for(int i=a;i<=b;i++)
			for(int j=c;j<=d;j++){
				x=i; y=j;
				ruch=0;
				while(x>0 && y>0){
					if(x>y)
						if(x>2*y){
							wygr=ruch;
							goto end;
						}
						else
							x-=y;
					else
						if(y>2*x){
							wygr=ruch;
							goto end;
						}
						else
							y-=x;
					ruch^=1;
				}
				wygr=ruch;
				end:
				if(wygr==0)
					res++;
			}
			printf("Case #%d: %d\n",tt,res);
	}
}
				
				
				
		
