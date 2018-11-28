
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
using namespace std;
typedef long long int64;

int cas;
vector<int> t[2005];
bool stan[2006];
int n,m;
int main(){
	scanf("%d",&cas);
	fup(i,1,cas){
		scanf("%d%d",&n,&m);
		memset(stan,0,sizeof(stan));
		fup(i,1,m){
			t[i].clear();
			int ile;
			scanf("%d",&ile);
			fup(j,1,ile){
				int a,b;
				scanf("%d%d",&a,&b);
				if(b==0)t[i].push_back(a);
				else t[i].push_back(-a);
			}
		}	
		bool poss=1;
		while(1){
			if(poss==0)break;
			bool ok=1;
			fup(i,1,m){
				bool jest=0;
				int malt=0;
				fup(j,0,siz(t[i])-1){
					int x=t[i][j];
					if(x<0)malt=-x;
					if(x<0){if(stan[-x]==1)jest=1;}
					else if(x>0){if(stan[x]==0)jest=1;}
				}
				if(jest)continue;
				if(malt==0){poss=0;break;}
				ok=0;
				stan[malt]=1;
			}
			if(poss==0)break;
			if(ok)break;
		}
	if(poss==0){
		printf("Case #%d: IMPOSSIBLE\n",i);
	}else{
		printf("Case #%d: ",i);
		fup(i,1,n)printf("%d ",stan[i]);
		printf("\n");
	}	
	}
	return 0;	
}
