#include <iostream>
#define REP(i,n) for(int i=0;i<(n);i++)
using namespace std;

int M[2000]={0};
int buf[20][3000]={0};
int sum=0;

void dfs(int m,int n)
{
	if(m==n) return;
	int tag=0;
	for(int i=m;i<=n;i++)
	{
		if(M[i]>0) {tag=1;break;}
	}
	if(tag==1){
	sum++;
	for(int i=m;i<=n;i++) M[i]--;}
	int mid=(m+n)/2;
	if(n==m+1) return;
	dfs(m,mid);
	dfs(mid+1,n);
}

int main(void)
{
	freopen("s.in","r",stdin);
	freopen("s.out","w",stdout);
	int T,P;
	cin>>T;
	REP(W,T)//W+1
	{
		sum=0;
		scanf("%d",&P);
		REP(i,1<<P) {int t;scanf("%d",&t); M[i]=P-t;}
		REP(i,P) REP(j,1<<(P-i-1)) scanf("%d",&buf[i][j]);
		dfs(0,(1<<P)-1);
		printf("Case #%d: %d\n",W+1,sum);
	}
}