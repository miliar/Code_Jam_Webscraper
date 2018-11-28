#include<iostream>
using namespace std;

#define ME(s) memset((s), 0, sizeof((s)))
#define MM(s,a) memset((s),(a),sizeof((s)))
#define MCP(s,a) memcpy((s), (a), sizeof(s))
#define LL long long
#define PII pair<int, int>
#define mkp(a,b) make_pair((a),(b))
#define x first
#define y second
#define FOR(i,n) for (int (i)=0;(i)<(n);++(i))

int map[600][600],down[600][600],rig[600][600],dp[600][600],n,m;

int qmin(int a,int b,int c){
	int ret=min(a,b);
	ret=min(ret,c);
}
void hzz(){
	scanf("%d%d",&n,&m);
	ME(map);
	FOR(i,n){
		char ch;
		int p;
		FOR(j,m/4){
			cin>>ch;
			if (ch<='9') p=ch-'0';else p=ch-'A'+10;
			FOR(k,4) if ((p&(1<<(3-k)))>0) map[i][j*4+k]=1;
		}
	}

	
	FOR(i,n){
		rig[i][m-1]=1;
		for (int j=m-2;j>=0;--j) if ((map[i][j]^map[i][j+1])==1) rig[i][j]=rig[i][j+1]+1;
		else rig[i][j]=1;
	}
		
	FOR(j,m){
		down[n-1][j]=1;
		for (int i=n-2;i>=0;--i) if ((map[i][j]^map[i+1][j])==1) down[i][j]=down[i+1][j]+1;
		else down[i][j]=1;
	}
	

	
	FOR(i,n) dp[i][m-1]=1;
	FOR(j,m) dp[n-1][j]=1;
	for (int i=n-2;i>=0;--i)
	for (int j=m-2;j>=0;--j) if (map[i][j]==map[i+1][j+1]) dp[i][j]=qmin(dp[i+1][j+1]+1,down[i][j],rig[i][j]);
	else dp[i][j]=1;
	

}

int size[600*600],num[600*600],next[600][600],tot;
bool done[600][600];

int check(int x,int y){
	int ret=dp[x][y];
	FOR(i,dp[x][y]) FOR(j,dp[x][y])
	if (done[x+i][y+j]) ret=min(ret,max(i,j));
	dp[x][y]=ret;
	return ret;
}
void count(){
	tot=0;
	ME(done);ME(num);ME(next);
	int l=n*m;
	int h=0;
	FOR(z,n*m){
		int mx=-1,mi,mj;
		
		
		for(int i=0;i<n;++i) {
			if (tot>0) if (mx==size[tot-1]) break;
			int j=0;
			while (j<m){
				if (next[i][j]!=0){j=next[i][j];continue;}
				if (!done[i][j]) if (dp[i][j]>mx) if (check(i,j)>mx){
					mx=check(i,j);
					mi=i;mj=j;
				}
				++j;
			}
		}
		
	/*	if (tot>0) if (mx!=size[tot-1]){
			h=0;
			for(int i=h;i<n;++i) {
				if (tot>0) if (mx==size[tot-1]) break;
				int j=0;
				while (j<m){
					if (next[i][j]!=0){j=next[i][j];continue;}
					if (!done[i][j]) if (dp[i][j]>mx) if (check(i,j)>mx){
						mx=check(i,j);
						mi=i;mj=j;
					}
					++j;
				}
			}
		}
		
		*/
		h=mi;
		if (mx<=0) break;
		FOR(t1,mx) FOR(t2,mx) done[mi+t1][mj+t2]=true;
		FOR(t1,mx) next[mi+t1][mj]=mj+mx;
		
		if (tot==0) {++tot;size[0]=mx;++num[0];}
		else if (size[tot-1]==mx) ++num[tot-1];
		else {size[tot]=mx;++num[tot];++tot;}
		
		if (size[tot-1]==1) {num[tot-1]=l;break;}
		l-=mx*mx;
		
		
		
		
		
		
	//	cout<<mx<<" "<<mi<<" "<<mj<<endl;
	}
	cout<<tot<<endl;
	FOR(i,tot) cout<<size[i]<<" "<<num[i]<<endl;
}
int main(){
	freopen("C-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,z=1;
	cin>>T;
		
	while (z<=T){
		cout<<"Case #"<<z<<": ";
		hzz();
		count();
		++z;
	}
	
}
