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

int n,o,b,x[1111],y[1111];

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);	
	int T=0;
	cin >> T;
	for (int E=1;E<=T;E++){
		cin >> n;
		for (int i=0;i<n-1;i++)cin >> x[i],x[i]--;
		o=0;
		b=0;
		for (int i=0;i<n-1;i++)for (int j=i+1;j<n-1;j++)if (j<x[i]&&x[j]>x[i])b=1;
		if (b){
			cout << "Case #" << E << ": Impossible" << endl;
			continue;
		}
		m0(y);
		for(;;){
			int w=0;
			for (int i=0;i<n-1;i++){
				int a=0,b=1,u;
				for (int j=i+1;j<n;j++)if ((y[j]-y[i])*b>a*(j-i))u=j,a=(y[j]-y[i]),b=(j-i);
				if (u!=x[i])w=1,y[x[i]]++;
			}
			if (!w)break;
		}
		cout << "Case #" << E << ":";
		for (int i=0;i<n;i++)cout << " " << y[i];
		puts("");
	}
	return 0;
}


