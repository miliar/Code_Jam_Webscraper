#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
using namespace std;

#define inf (1e9)
#define lng long long
#define linf (1e18)
#define pb push_back
#define eps (1e-7)
//#define eq(a,b) (abs(a-b)<eps)
#define leq(a,b) (eq(a,b)||a<b)
#define geq(a,b) (eq(a,b)||a>b)
#define pii pair<int,int>
#define mpii make_pair<int,int>
#define deg2rad 0.017453292519943295769236907684886
#define VI vector<int>
#define forn(i,n)for (int i=0;i<n;++i)
#define all(a) a.begin(),a.end()
#define VS vector<string>
#define forv(i,v) for(int i=0;i<(int)v.size();++i)
#define PII pair<int,int>
#define mp make_pair


inline bool eq(double a,double b){
	return (a-b<eps)&&(b-a<eps);
}
inline int gcd(int a,int b){
	if(!a)return b;
	if(!b)return a;
	while(true){
		a%=b;
		if(!a)return b;
		b%=a;
		if(!b)return a;
	}
}
inline int max(int a,int b){
	if(a<b)return b;return a;
}
inline int min(int a,int b){
	if(a>b)return b;return a;
}

int dx[8]={-2,-1};
int dy[8]={-1,-2};

#define filename "mole"
int main()
{
	freopen(filename".in","r",stdin);
	freopen(filename".out","w",stdout);
	int tests;
	cin >> tests;
	forn(iii,tests){
		long long ans[110][110];
		memset(ans,0,sizeof(ans));
		int h,w,n;		
		cin >> h >> w >> n;
		set< PII > a;
		
		forn(i,n){
			int x,y;
			cin >> x >> y;
			a.insert(mp(x,y));
		}

	
		ans[1][1]=1;
		if (a.count(mp(1,1)))ans[1][1]=0;
		for (int i=2;i<=h;++i)for (int j=2;j<=w;++j){
			if (a.count(mp(i,j)))continue;
			forn(jj,2){
				int x=i+dx[jj];
				int y=j+dy[jj];
				if (x>0&&y>0&&x<=h&&y<=w){
					ans[i][j]+=ans[x][y];
					ans[i][j]%=10007;
				}
			}
		}
	/*	for (int i=1;i<=h;++i){
			for (int j=1;j<=w;++j)cout << ans[i][j] << " " ;
			cout << endl;
		}
		cout << endl << endl;*/
		cout << "Case #" << iii+1 <<": "<< ans[h][w] << endl;

	}	
	

	return 0;
}

