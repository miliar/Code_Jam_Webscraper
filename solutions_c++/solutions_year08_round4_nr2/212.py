
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


int main(){
	int cas;
	scanf("%d",&cas);
	fup(c,1,cas){
		int n,m,a;
		cin>>n>>m>>a;
		bool tak=0;	
		printf("Case #%d: ",c);
		fup(x1,0,n)fup(y1,0,m)fup(x2,0,n)fup(y2,0,m){
			int pole=x1*y2-x2*y1;
			if(abso(pole)==a){
				tak=1;
				printf("0 0 %d %d %d %d\n",x1,y1,x2,y2);
				goto done;
			
			}
/*			if(x1==0&&y1==0)continue;
			int il=(a+x2*y1);
			if(il%x1)continue;
			int y2=il/x1;
			if(x2==0&&y2==0)continue;
			if(y2>m)continue;
			tak=1;
*/		
		}
		done:;
		if(!tak)printf("IMPOSSIBLE\n");
	}
	return 0;	
}
