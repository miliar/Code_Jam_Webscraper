
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
int main(){
	cin>>cas;
	fup(i,1,cas){
		int64 odp=0;
		int n;scanf("%d",&n);
		vector<int64> aa,bb;
		fup(i,1,n){int a;scanf("%d",&a);aa.push_back(a);}
		fup(i,1,n){int a;scanf("%d",&a);bb.push_back(a);}
		sort(aa.begin(),aa.end());
		sort(bb.begin(),bb.end());
		reverse(bb.begin(),bb.end());
		fup(i,0,n-1){
			odp+=aa[i]*bb[i];
		}

		printf("Case #%d: %lld\n",i,odp);
	}
	return 0;	
}
