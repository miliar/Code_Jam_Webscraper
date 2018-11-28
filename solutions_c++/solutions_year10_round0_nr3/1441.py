/*	SURENDRA KUMAR MEENA	*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long int LL;
#define ALL(s) (s).begin(),(s).end()
#define R(i,m,n)	for(int i=m;i>=n;i--)
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define VI vector<int>
#define PB push_back
#define CLR(s,v) memset(s,v,sizeof(s))
#define FR(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)
typedef pair<int,int> PI;
#define f first
#define s second

LL a[100000];

int main(){
	int t;
	cin>>t;
	FF(cas,1,t+1){
		cout<<"Case #"<<cas<<": ";
		LL r,k,n;
		cin>>r>>k>>n;
		vector<LL> v(n);
		LL ans=0;
		F(i,n){
			cin>>v[i];
			ans+=v[i];
		}
		if(ans<=k){
			cout<<r*ans<<endl;
			continue;
		}
		map< vector<LL> , int > mp;
		int cnt=0;
		ans=0;
		while(cnt<r && mp.find(v)==mp.end()){
			if(cnt){
				mp[v]=cnt;
			}
			LL sum=0;
			while(sum+v[0]<=k){
				LL val=v[0];
				sum+=v[0];
				v.erase(v.begin());
				v.PB(val);
			}
			ans+=sum;
			a[cnt]=ans;
			cnt++;
		}
		if(cnt>=r)	cout<<ans<<endl;
		else{
			LL pos=mp[v];
			LL cyclen=cnt-mp[v];
			LL rem=r-pos;
			LL sum=ans-(pos?a[pos-1]:0);
			LL md=rem % cyclen;
			LL valMod=0;
			if(md){
				md--;
				valMod=a[pos+md]-(pos?a[pos-1]:0);
			}
//			cout<<pos+md<<endl;
//			cout<<cnt<<" "<<pos<<" "<<cyclen<<" "<<rem<<" "<<sum<<" "<<md<<" "<<valMod<<endl;
			cout<<(pos?a[pos-1]:0)+(rem/cyclen)*sum + valMod <<endl;
		}
	}
	return 0;
}
