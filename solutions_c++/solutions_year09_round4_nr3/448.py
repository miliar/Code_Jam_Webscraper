#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;
typedef vector<int> VI;
#define PB push_back
#define REP(i,n) for(int i=0;i<(n);i++)

const bool dbg = 0;
const bool dbg1 = 0;
const int MAXN  = 101;
const int NIL = -1;
int n,k;
VI sto[MAXN];
int len[MAXN];
bool ok[MAXN];
int p[MAXN][MAXN];
void read(){
	scanf("%d%d",&n,&k);
	REP(i,n){
		REP(j,n)p[i][j] = NIL;
		sto[i].clear();
		ok[i] = 0;
		len[i] =0;
		REP(j,k){
			int a;
			scanf("%d",&a);
			sto[i].PB(a);
		}
	}
}

bool prz(int a,int b){
	if(p[a][b] != NIL)return p[a][b];
	if(sto[a][0]>sto[b][0])swap(a,b);
	REP(i,k){
		if(sto[a][i]>=sto[b][i])
		{
			p[a][b] = 1;
			return 1;
		}
	}
	p[a][b] = 0;
	return 0;
}

void compute(int cas){
	sort(sto,sto+n);
	int res = n;
	queue<int> q;
	q.push(1);
	for(int i=n-2;i>=0;i--){
		int id = n-1-i;
		while(true){
			int f = q.front();
			if(f>=(1<<id))break;
			q.pop();
			int ok = 0;
			for(int j=i;j<n;j++){
				int b = (1<<(n-1-j));
				if((!(f&b)) || prz(i,j) )continue;
				else {q.push((f|(1<<id))^b);ok=1;}
			}
			if(!ok)q.push(f|(1<<id));
		}
		if(dbg)printf("q.size():%d\n",int(q.size()));
	}
	while(!q.empty()){
		int f = q.front();
		q.pop();
		res = min(res,__builtin_popcount(f));
	}
	printf("Case #%d: %d\n",cas+1,res);
}

int main(){
	int t;
	scanf("%d",&t);
	REP(i,t){
		read();
		compute(i);
	}
	return 0;
}





