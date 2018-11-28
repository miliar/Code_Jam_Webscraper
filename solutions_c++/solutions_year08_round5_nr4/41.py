
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
#define maxn 200
typedef long long int64;
const int mod=10007;
int ile[maxn][maxn];
bool rock[maxn][maxn];
int main(){
	int cas;
	cin>>cas;
	fup(c,1,cas){
		int w,h,r;
		cin>>w>>h>>r;
		memset(ile,0,sizeof(ile));
		memset(rock,0,sizeof(rock));
		ile[1][1]=1;
		fup(i,1,r){
			int x,y;cin>>x>>y;rock[x][y]=1;
		}
		fup(i,1,w){
			fup(j,1,h){
				if(rock[i+1][j+2]==0){ile[i+1][j+2]+=ile[i][j];ile[i+1][j+2]%=mod;}
				if(rock[i+2][j+1]==0){ile[i+2][j+1]+=ile[i][j];ile[i+2][j+1]%=mod;}
			}
		}
		int wyn=ile[w][h];
		printf("Case #%d: %d\n",c,wyn);
	}
	return 0;	
}
