
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set> 
#include<queue>
#include<string>
#include<stack>
#include<sstream>
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it) 
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) cerr << #x << " = "; FOREACH(it,(x)) cerr << *it << ","; cerr << "\n"; 
#define fup(i,a,b) for(int i=a;i<=b;i++)
#define fdo(i,a,b) for(int i=a;i>=b;i--)
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) (int)a.size()
#define inf 1000000000
#define SQR(a) ((a)*(a))
#define maxn 10005
using namespace std;
typedef long long int64;

int change[maxn];
bool typ[maxn];
int n,val;
int ile[maxn][2];
int eval(int typ,int a,int b){
	if(typ==1)return a&&b;
	else return a||b;
}
int main(){
	int cas;
	scanf("%d",&cas);
	fup(c,1,cas){
		memset(change,0,sizeof(change));
		memset(typ,0,sizeof(typ));
		memset(ile,0,sizeof(ile));
		scanf("%d%d",&n,&val);
		int wew=(n-1)/2;
		fup(i,1,wew){
			scanf("%d%d",&typ[i],&change[i]);	
		}
		fup(i,wew+1,n){
			scanf("%d",&typ[i]);
		}
		fup(i,wew+1,n){
			ile[i][0]=ile[i][1]=inf;
			ile[i][typ[i]]=0;
		}

		fdo(i,wew,1){
			ile[i][0]=ile[i][1]=inf;
			int ty=typ[i];
			int lef,rig;
			lef=2*i;
			rig=2*i+1;
			fup(l,0,1){
				fup(r,0,1){
					if(ile[lef][l]>=inf)continue;
					if(ile[rig][r]>=inf)continue;
					int v=eval(ty,l,r);
					int cost=ile[lef][l]+ile[rig][r];
					if(cost<ile[i][v])ile[i][v]=cost;
				}	
			}
			if(change[i]){
				ty=!ty;
				fup(l,0,1){
				fup(r,0,1){
					if(ile[lef][l]>=inf)continue;
					if(ile[rig][r]>=inf)continue;
					int v=eval(ty,l,r);
					int cost=ile[lef][l]+ile[rig][r]+1;
					if(cost<ile[i][v])ile[i][v]=cost;
				}	
			}
			
			}


		}

		printf("Case #%d: ",c);
		if(ile[1][val]>=inf){
			printf("IMPOSSIBLE\n");
		}else printf("%d\n",ile[1][val]);
	}
	return 0;	
}
