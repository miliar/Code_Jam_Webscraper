#include <iostream>
#include <queue>
using namespace std;
queue <int> q1,q2;
int T,r,k,n;
long long dp[999999];
int nxt[999999];
long long res;
int main(){
	freopen("ins.in","r",stdin);
	freopen("C.out","w",stdout);
	int apa=1;
	scanf("%d",&T);
	while (T--){
		  res=0;
		  while (!q1.empty()) q1.pop();
		  while (!q2.empty()) q2.pop();
		  
		  scanf("%d%d%d",&r,&k,&n);
		  for (int i=1;i<=n;i++){
		  	  int x;
				scanf("%d",&x);
				q1.push(x);
				}
			int j=0;
			bool udahh=0;
			memset(dp,-1,sizeof(dp));
			memset(nxt,-1,sizeof(nxt));	
			long long sums=0;
		  for (int i=1;i<=r;i++){
		  	  int cap=k;
		  	  if (j==0 && dp[j]!=-1 && !udahh){
			  	 	   int warp=i-1;
			  	 	   i--;
			  	 	   udahh=1;
			  	 	   while (i+warp<=r) {res+=sums; i+=warp; }
						  //res+=dp[j];
						  }
  				  else 
					{
		  	  if (dp[j]!=-1) {res+=dp[j]; j=nxt[j];}
		  	  else{
			  	   int jj=j;
			  	   dp[jj]=0;
				while (q1.size() && cap>=q1.front()){
			  		j++;
			  		j%=n;
					  cap-=q1.front();
			  		q2.push(q1.front());
			  		dp[jj]+=q1.front();
			  		q1.pop();
					  }
				while (!q2.empty()){ q1.push(q2.front()); q2.pop();}
				res+=dp[jj];
				sums+=dp[jj];
				nxt[jj]=j;
				}
				}
				}
				//cout<<dp[0]<<endl;
		  printf("Case #%d: %lld\n",apa,res);
		  apa++;
		  }
	
	}
