#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define AL(x) x.begin(),x.end()
#define pw(x) (1ull<<(x))
#define M 1000000007
using namespace std;
typedef pair<int,int> pt;
typedef vector<int> vt;

string ans;
int d[111111],l[111111],f[111111],w,n;

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);	
	int T=0;
	cin >> T;
	for (int E=1;E<=T;E++){
		cin >> n;
		for (int i=0;i<n;i++)cin >> d[i] >> l[i];
		for (int i=0;i<n;i++)f[i]=-1;
		f[0]=d[0];
		for (int i=0;i<n;i++)for (int j=i+1;j<n;j++)if (d[j]-d[i]<=f[i])f[j]=max(f[j],min(l[j],d[j]-d[i]));	
		cin >> w;
		ans="NO";
		for (int i=0;i<n;i++)if (w-d[i]<=f[i])ans="YES";
		cout << "Case #" << E << ": " << ans << endl;
	}
	return 0;
}


