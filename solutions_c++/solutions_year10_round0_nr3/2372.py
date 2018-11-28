#include<iostream>
#include<algorithm>
#include<string>
#include<math.h>
#include<vector>
#include<map>
using namespace std;

typedef __int64 llong;
const int maxn = 1100;
int N,R,K;
llong v[maxn],tot[maxn],sum[maxn];
int next[maxn],visit[maxn],len[maxn];

int getnext(int s)
{
	int i,j;
	llong t=v[s];
	int e=(s+1)%N;
	memset(visit,0,sizeof(visit));
	visit[s]=1;
	while( t+v[e]<=K)
	{
		if( visit[e] )break;
		t += v[e] ;
		visit[e]=1;
		e=(e+1)%N;
		
	}
	tot[s]=t;
	next[s]=e;
	return e;
}
int main(){
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	int i,j,t;
	scanf("%d",&t);
	for(int ca=1;ca<=t;ca++)
	{
		scanf("%d%d%d",&R,&K,&N);
		for(i=0;i<N;i++)scanf("%I64d",&v[i]);

		memset(tot,0,sizeof(tot));
		memset(visit,0,sizeof(visit));
		memset(next,-1,sizeof(next));

		int st,ed;
		st=0;
		for(i=0;i<N;i++){
			getnext(i);
			//printf("%I64d ",tot[i]);
		}
		/*cout<<endl;
		for(i=0;i<N;i++){
			cout<<next[i]<<" ";
		}
		cout<<endl;*/

		llong cnt=0,pre_value,circle_value;
		int pre;
		st=0;
		memset(visit,0,sizeof(visit));
		memset(sum,0,sizeof(sum));
		int len=0;
		while(visit[ st ]==0){
			visit[st]=++len;

			ed=next[st];			
			cnt+=tot[st];
			sum[st]=cnt;

			pre=st;
			st=ed;			
		}
		
		llong ret = 0;
		if( st == 0 ){
			ret = (R/visit[pre])*sum[pre];
			R %= visit[pre];
			while(R--){
				ret += tot[st];
				st = next[st];
			}
			printf("Case #%d: %I64d\n",ca,ret);
			//break;
			continue ;
		}

		pre_value = sum[st] - tot[st]  ;
		circle_value = sum[ pre ] - pre_value ;
		int circle_len = visit[pre] - visit[st] + 1;
		
		

		R -=visit[st]-1;

		ret = pre_value + circle_value * ( R/circle_len );
		R %= circle_len;
		while(R--){
			ret += tot[st];
			st = next[st];
		}
		//printf("%I64d %I64d\n",pre_value,circle_value);
		printf("Case #%d: %I64d\n",ca,ret);
		
	}
	
}
