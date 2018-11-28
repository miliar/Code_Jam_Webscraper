#include <ios>
#define IFILE "input.txt"
#define OFILE "output.txt"
int grp[1001];
int mon[1001];
int nxt[1001];
bool vis[1001];
int cyc[1001];
__int64 ans;
int main(){
	int t,T;
	freopen(IFILE,"r",stdin);
	freopen(OFILE,"w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		int R,k,N,i;
		scanf("%d%d%d",&R,&k,&N);
		for(i=1;i<=N;i++)
			scanf("%d",&grp[i]);
		int st,ed,sum;
		ed=0;sum=0;
		for(st=1;st<=N;st++){
			while(sum+grp[ed+1]<=k){
				sum+=grp[++ed];
				if(ed==N)
					ed=0;
				if(sum!=0&&ed+1==st)
					break;
			}
			mon[st]=sum;
			nxt[st]=ed+1;
			sum-=grp[st];
		}
		int cnt;
		st=1;
		for(cnt=0;cnt<R;cnt++){
			if(vis[st])
				break;
			cyc[cnt]=st;
			ans+=mon[st];
			vis[st]=true;
			st=nxt[st];
		}
		sum=0;
		for(i=0;i<cnt;i++){
			if(cyc[i]==st)
				break;
			sum+=mon[cyc[i]];
		}
		ans-=sum;
		cnt-=i;
		R-=i;
		if(cnt!=0){
			ans*=(R/cnt);
			R%=cnt;
			int j;
			for(j=0;j<R;j++)
				ans+=mon[cyc[i+j]];
		}
		ans+=sum;
		printf("Case #%d: %I64d\n",t,ans);
		ans=0;
		memset(grp,0,sizeof(grp));
		memset(mon,0,sizeof(mon));
		memset(nxt,0,sizeof(nxt));
		memset(vis,0,sizeof(vis));
		memset(cyc,0,sizeof(cyc));
	}
}
