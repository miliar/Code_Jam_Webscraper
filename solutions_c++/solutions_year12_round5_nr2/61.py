#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<vector>
#define REP(i,m) for(int i=0;i<m;++i)
#define REPN(i,m,in) for(int i=in;i<m;++i)
#define pb push_back
#define mp make_pair
#define fr first
#define sc second
#define dump(x)  cerr << #x << " = " << (x) << endl
#define prl cerr<<"called:"<< __LINE__<<endl
using namespace std;
static const int INF =500000000; 
template<class T> void debug(T a,T b){ for(;a!=b;++a) cerr<<*a<<' ';cerr<<endl;}
typedef long long int lint;
typedef pair<int,int> pi;
int s,m;
int buf[6005][6005];
pi ope[3005];
int cnt;
int dx[]={-1,-1,0,0,1,1},dy[]={-1,0,-1,1,0,1};
void dfs(int a,int b){
	buf[a][b]=-1;
	REP(i,6){
		int px=b+dx[i],py=a+dy[i];
		if(abs(py-px)>=s || px<0 || py<0 || px>=2*s+1 || py>=2*s+1 ||
			buf[py][px]!=0) continue;
		dfs(py,px);
	}
}
int cor;
int edg[10];
void rec(int a,int b){
	buf[a][b]=0;
	if(mp(a,b)==mp(1,1) || mp(a,b)==mp(s,1) || mp(a,b)==mp(1,s) || mp(a,b)==mp(2*s-1,s)||
			mp(a,b)==mp(s,2*s-1) || mp(a,b)==mp(2*s-1,2*s-1)) ++cor;
	else{
		if(a==1) edg[0]=1;
	if(b==1) edg[1]=1;
	if(a==2*s-1) edg[2]=1;
	if(b==2*s-1) edg[3]=1;
	if(abs(a-b)==s-1){
		if(a<b) edg[4]=1;
		else edg[5]=1;
	}
	}
	REP(i,6){
		int px=b+dx[i],py=a+dy[i];
		if(abs(py-px)>=s || px<=0 || py<=0 || px>=2*s || py>=2*s || buf[py][px]==0){
			continue;
		}
		rec(py,px);
	}
}
bool check(int md){
	REP(i,2*s+1) REP(j,2*s+1) buf[i][j]=0;
	REP(i,md) buf[ope[i].fr][ope[i].sc]=1;
	REP(i,md) if(buf[ope[i].fr][ope[i].sc]){
		cor=0;
		memset(edg,0,sizeof(edg));
		rec(ope[i].fr,ope[i].sc);
		if(cor>=2 || count(edg,edg+10,1)>=3) return true;
	}

	REP(i,md) buf[ope[i].fr][ope[i].sc]=1;
	REP(i,2*s+1) REP(j,2*s+1) if((i==0 || j==0 || i==2*s || j==2*s || abs(j-i)>=s) && buf[i][j]==0){
		dfs(i,j);
	}
	REPN(i,2*s,1) REPN(j,2*s,1) if(abs(j-i)<s && buf[i][j]==0) return true;
	return false;
}
int check2(int md){
	int res=0;
	REP(i,2*s+1) REP(j,2*s+1) buf[i][j]=0;
	REP(i,md) buf[ope[i].fr][ope[i].sc]=1;
	REP(i,md) if(buf[ope[i].fr][ope[i].sc]){
		cor=0;
		memset(edg,0,sizeof(edg));
		rec(ope[i].fr,ope[i].sc);
		if(cor>=2) res|=1;
		if(count(edg,edg+10,1)>=3) res|=2;
	}

	REP(i,md) buf[ope[i].fr][ope[i].sc]=1;
	REP(i,2*s+1) REP(j,2*s+1) if((i==0 || j==0 || i==2*s || j==2*s || abs(j-i)>=s) && buf[i][j]==0){
		dfs(i,j);
	}
	REPN(i,2*s,1) REPN(j,2*s,1) if(abs(j-i)<s && buf[i][j]==0) res|=4;
	return res;
}

char name[][100]={"",
	"bridge in move ",
	"fork in move ",
	"bridge-fork in move ",
	"ring in move ",
	"bridge-ring in move ",
	"fork-ring in move ",
	"bridge-fork-ring in move "
};
int main(){
	int t;scanf("%d",&t);
	int setn=0;
	while(t--){
		++setn;
		printf("Case #%d: ",setn);
		scanf("%d%d",&s,&m);
		REP(i,m) scanf("%d%d",&ope[i].fr,&ope[i].sc);
		int flag=0;
		REP(i,m+1) if(check(i)){
			int ind=check2(i);
			printf("%s%d\n",name[ind],i);
			flag=1;break;
		}
		if(!flag) puts("none");
	}
				
	return 0;
}



