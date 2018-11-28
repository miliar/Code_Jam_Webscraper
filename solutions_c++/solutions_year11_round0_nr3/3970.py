#include<queue>
#include<set>
#include<deque>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<map>
#include<fstream>
using namespace std;
#define dbg(x) cout << #x << " -> " << (x) << "\t";
#define rep(i,n) for(int i=0;i<n;i++)
#define pb push_back
#define sz size()
#define psi pair<string,int>
#define all(x) x.begin(),x.end()
#define GI ({int t;scanf("%d",&t); t;})
#define flush(x) memset(x,0,sizeof(x))
#define ll long long
int main() {
	int t=GI,cases=1;
	while(t--) {
		int n=GI;
		int a[16];
		rep(i,n) cin>>a[i];
		int res = -(1<<20);
		rep(i,(1<<n)) {
			int val1=0,val2=0,tval1=0,tval2=0,cnt=0;
			rep(j,n) {
				if(i&(1<<j)) {
					val1=val1^a[j];
					tval1+=a[j];
					cnt++;
				}
				else {
					val2=val2^a[j];
					tval2+=a[j];
				}
			}	
	 		if(val1==val2&&cnt!=0&&cnt!=n) {
	 			res=max(tval1,res);
	 			res=max(tval2,res);
	 		}	 		
		}
		if(res<0) {
			cout<<"Case #"<<cases<<": NO"<<endl; 
		}
		else {
			cout<<"Case #"<<cases<<": "<<res<<endl;
		}
		cases++;
	}
	return 0;
}
