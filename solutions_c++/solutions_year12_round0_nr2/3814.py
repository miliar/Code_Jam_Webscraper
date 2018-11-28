#include<iostream>
#include<cstdio>

using namespace std;

int main(){
	int t;
	scanf("%d\n",&t);
	int n,s,p;
	int res;
	int v;
	for(int i=1;i<=t;i++) {
		res = 0;
		scanf("%d %d %d",&n,&s,&p);
		for(int j=0;j<n;j++){
			cin>>v;			
			if(v%3==0){
				if(p<=v/3 ){
					res++;
					continue;
				}
				else if(p<=(v/3+1) && v>0 && s>0){
					res++;
					s--;
					continue;
				}
			}
			else if(v%3==1){
				if(p<=(v/3+1)){
					res++;
					continue;
				}
			} else {
				if(p<=(v/3+1)){
					res++;
					continue;
				}
				else if(p<=(v/3+2) && s>0){
					res++;
					s--;
					continue;
				}
			}
		}
		printf("Case #%d: %d\n",i,res);
	}
	return 0;
}
