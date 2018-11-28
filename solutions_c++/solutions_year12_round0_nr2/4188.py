#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main(){
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++){
		int cnt=0,n,s,p;
		scanf("%d%d%d",&n,&s,&p);
		for(int i=0;i<n;i++){
			int x;
			scanf("%d",&x);
			if(x%3==0){
				if(x/3>=p) cnt++;
				else if(x>=3&&x/3+1>=p&&s>0) cnt++,s--;
			}else if(x%3==1){
				if(x/3+1>=p) cnt++;
			}else if(x%3==2){
				if(x/3+1>=p) cnt++;
				else if(x/3+2>=p&&s>0) cnt++,s--;
			}
		}
		printf("Case #%d: %d\n",cas,cnt);
	}
	return 0;
}
