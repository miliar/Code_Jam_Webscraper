# include <cstdio>
# include <cstring>
# include <cstdlib>
# include <iostream>
# include <cmath>
# include <string>
# include <algorithm>
# include <vector>
# define REP(i,n) for(int i=0;i<n;i++)
# define REP1(i,n) for(int i=1;i<=n;i++)
# define CLR(a,b) memset(a,b,sizeof(a))
# define For(i,a,b) for(int i=a;i<=b;i++)
# define Trv(p,a) for(int p=head[a];p;p=next[p])
# define INF 0x7FFFFFFF
# define vi vector<int>
# define it iterator
# define pb push_back
using namespace std;

typedef long long int64;
void setIO(string name){
	string	is=name+".in",
			os=name+".out";
	freopen(is.c_str(),"r",stdin);
	freopen(os.c_str(),"w",stdout);
}

int s[40],ns[40];
void prepare(){
	CLR(ns,-1);CLR(s,-1);
	REP(i,11)
		For(j,0,i)
			For(k,0,j)	if(fabs(i-k)<=2&&fabs(j-k)<=2&&fabs(i-j)<=2){
				int t=i+j+k,flag=0;
				if(fabs(i-k)==2||fabs(j-k)==2||fabs(i-j)==2)	flag=1;
				if(flag){
					s[t]=max(i,ns[t]);
				}else	ns[t]=max(i,s[t]);
			}
}

int v[200],dp[200][200];
void work(){
	int n,k,p;scanf("%d %d %d",&n,&k,&p);
	REP1(i,n)
		scanf("%d",v+i);
	CLR(dp,-1);
	dp[0][0]=0;
	REP1(i,n)
		For(j,0,k){
			if(dp[i-1][j]>=0&&ns[v[i]]>=0){
				dp[i][j]=dp[i-1][j];
				if(ns[v[i]]>=p)	dp[i][j]++;
			}		
			if(j>0&&dp[i-1][j-1]>=0&&s[v[i]]>=0){
				int t=dp[i-1][j-1];
				if(s[v[i]]>=p)	t++;
				dp[i][j]=max(dp[i][j],t);
			}
		}
	printf("%d\n",dp[n][k]);
}	
		
int main(){
	setIO("B-large");
	prepare();
	int casen;scanf("%d",&casen);
	REP1(i,casen){
		printf("Case #%d: ",i);		
		work();
	}
	return 0;
}
