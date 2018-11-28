#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T,t,N,ai[1001],i,k,tmp,cnt;
	double hits,minh,tmph;
	bool visit[1001];
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		memset(visit,0,sizeof(visit));
		hits=0;
		scanf("%d",&N);
		for(i=1;i<=N;i++)scanf("%d",&ai[i]);
		for(i=1;i<=N;i++){
			if(!visit[ai[i]]){
				visit[ai[i]]=1;tmp=ai[i];cnt=1;
				while(tmp!=i){
					cnt++;
					tmp=ai[tmp];
					visit[tmp]=1;
				}
				minh=2*(cnt-1);
				for(tmph=0,k=1;k<=cnt-1;k++){
					tmph+=cnt*1.0/(cnt-1);
					if(minh>tmph+2*(cnt-k-1))minh=tmph+2*(cnt-k-1);
				}
				hits+=minh;
			}
		}
		printf("Case #%d: %.6f\n",t,hits);
	}
	
	return 0;
}
