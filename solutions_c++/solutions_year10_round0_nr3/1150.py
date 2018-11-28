#include<iostream>
using namespace std;
typedef  long long LL ;

		int next[1100];
		LL total[1100];

LL simulate(int x,int r)
{
	LL ret=0;
	while(r--){
		ret+=total[x];
		x=next[x];
	}
	return ret;
}
		
		



int main()
{
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cases=1;cases<=T;cases++){
		int R,K,N;
		LL a[1100];
		scanf("%d %d %d",&R,&K,&N);
	
		for(int i=0;i<N;i++){
			scanf("%lld",&a[i]);
		}	
		LL sum;
		memset(next,-1,sizeof(next));
		for(int i=0;i<N;i++){

			int j=i;
			sum=0;
			for( ; j<N;j++){
				if( sum+a[j] >K ){
					total[i]=sum;
					next[i]=j;
					break;
				}
				sum+=a[j];
			}
			if(next[i]!=-1 )continue;
			for( j=0;j<i;j++){
				if( sum+a[j]>K ){
					next[i]=j;
					total[i]=sum;
					break;
				}
				sum+=a[j];
			}
			if( next[i]==-1 ){next[i]=i;total[i]=sum;}
		}

		int cnt=1;
		int visited[1100];memset(visited,0,sizeof(visited));
		int x=0;
		do{
			visited[x]=cnt++;
			x=next[x];
		}while(!visited[x]);

		int loop=cnt-visited[x];

		//printf("%d %d %d %d\n",cnt,visited[x],x,loop);
		LL ans;
		if( R<visited[x] )ans=simulate(0,R);
		else {
			ans=simulate(0,visited[x]-1);
			R-=visited[x]-1;
			ans+=(R/loop)* simulate(x,loop);
			ans+=simulate(x,R%loop);
		}
		printf("Case #%d: %lld\n",cases,ans);
	}
	return 0;
}






