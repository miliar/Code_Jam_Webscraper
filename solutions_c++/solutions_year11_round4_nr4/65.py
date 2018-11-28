#pragma comment(linker, "/STACK:65777216")

#include <algorithm>
#include <iostream>
#include <string>
#include<sstream>
#include<string.h>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include<stack>
#include <set>
#include <map>
#include<ctime>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef unsigned long long ull;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back

int a[444][444];
int n,m;
int c[555];
int r[444][444];

int p[444];
int stupid(int ver,int pos = 0){
	p[pos] = ver;
	if(ver == 1){
		int c = 1;
		REP(i,n){
			bool g = 1;
			REP(j,pos+1) if(p[j]==i){g=0;break;}
			if(!g) continue;
			g=0;
			REP(j,pos) if(a[p[j]][i]==1) g=1;
			if(g) c++;
		}
		return c;
	}
	int r = -1;
	REP(i,n)if(a[ver][i]==1 && a[i][1] == a[ver][1] - 1){
		r=max(r,stupid(i,pos+1));
	}
	return r;
}

int main(){ 
#ifdef LocalHost
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	
	int tc;
	cin>>tc;
	REP(TC,tc){
		CL(a,-1);CL(c,0);CL(r,-1);
		cin>>n>>m;
		REP(i,m){
			int x,y;
			scanf("%d,%d",&x,&y);
			a[x][y]=a[y][x]=1;
		}
		REP(i,n) a[i][i]=0;
		REP(k,n)REP(i,n)REP(j,n)if(a[i][k]!=-1 && a[k][j]!=-1)
			if(a[i][j]==-1 || a[i][j] > a[i][k] + a[k][j])
				a[i][j] = a[i][k] + a[k][j];
		
		printf("Case #%d: %d ",TC+1,a[0][1]-1);
		r[0][0] = 0;
		int res = 0;
		REP(i,n)REP(j,n)if(r[i][j]!=-1){
			REP(k,n)if(a[0][k] + a[k][1] == a[0][1] && a[0][k] == a[0][j] + 1 && a[j][k]==1){
				int next = r[i][j];

				REP(q,n)if(q!=i && q!=j && q!=k && q!=1 && q){
					if(j && a[i][q]==1) continue;

					if(a[0][q] + a[1][q] != a[0][1]){
						if(a[j][q]==1) next++;
					}else{
						if(a[0][q] == a[0][k]){
							if(a[j][q]==1) next++;
						}else{
							if(a[0][q]== a[0][j]){
								if(a[j][q]==1 || a[k][q]==1) next++;
							}
						}
					}

				}

				r[j][k] = max(r[j][k], next);
				if(k==1) res = max(res, next);
			}
		}
		
		//cout<<res+1<<' '<<stupid(0);
		cout<<stupid(0);
		puts("");
	}
	
/*#ifdef LocalHost
	cout<<endl<<endl<<clock()<<endl;
#endif*/
	return 0;
}