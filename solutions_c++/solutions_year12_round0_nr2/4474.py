#include<cstdio>
#include<iostream>
#include<algorithm>
#include<utility>
using namespace std;

int T,n,s,p,score[101],res;

int main(void){
	scanf("%d\n",&T);
	for(int t=1;t<=T;++t){
		res=0;
		scanf("%d%d%d",&n,&s,&p);
		for(int i=0;i<n;++i)scanf("%d",&score[i]);
		sort(score,score+n);
		for(int i=0;i<n;++i){
			if(score[i]%3==0){
				if(score[i]/3>=p)res++;
				else if(s&&2<=score[i]&&score[i]<=28&&score[i]/3+1>=p)res++,s--;
			}
			if(score[i]%3==1){
				if(score[i]/3+1>=p)res++;
			}
			if(score[i]%3==2){
				if(score[i]/3+1>=p)res++;
				else if(s&&2<=score[i]&&score[i]<=28&&score[i]/3+2>=p)res++,s--;
			}
		}
		printf("Case #%d: %d\n",t,res);
	}
	return 0;
}
