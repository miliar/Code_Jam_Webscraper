#define _CRT_SECURE_NO_DEPRECATE
#include <iostream> 
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;
vector<vector<pair<ll, ll> > > p;
vector<vector<pair<ll, ll> > > p2;
int n,m;
pair<ll,ll> operator+(const pair<ll,ll>& a,const pair<ll, ll>& b) {
	pair<ll,ll> res;
	res.first = a.first+ b.first;
	res.second = a.second + b.second;
	return res;
}
pair<ll,ll> operator-(const pair<ll,ll>& a,const pair<ll, ll>& b) {
	pair<ll,ll> res;
	res.first = a.first- b.first;
	res.second = a.second - b.second;
	return res;
}
pair<ll,ll> get(int ifrom,int ito, int jfrom , int jto) {
	pair<ll, ll> res;
	res.first = p[ito+1][jto+1].first + p[ifrom][jfrom].first - p[ifrom][jto+1].first - p[ito+1][jfrom].first;
	res.second = p[ito+1][jto+1].second + p[ifrom][jfrom].second - p[ifrom][jto+1].second - p[ito+1][jfrom].second;
	return res;
}
pair<ll,ll> get2(int ifrom,int ito, int jfrom , int jto) {
	pair<ll, ll> res;
	res.first = p2[ito+1][jto+1].first + p2[ifrom][jfrom].first - p2[ifrom][jto+1].first - p2[ito+1][jfrom].first;
	res.second = p2[ito+1][jto+1].second + p2[ifrom][jfrom].second - p2[ifrom][jto+1].second - p2[ito+1][jfrom].second;
	return res;
}
bool can(int i, int j, int k){
	if (i +k > n || j + k > m){
		return false;
	}
	pair<ll,ll> tmp = get(i, i+k-1, j, j+k-1) - get(i,i,j,j) - get(i+k-1,i+k-1,j,j) - get(i+k-1,i+k-1,j + k- 1,j + k-1) - get(i,i,j + k- 1,j + k-1);
	pair<ll, ll> w = get2(i,i+k-1, j, j+k-1)- get2(i,i,j,j) - get2(i+k-1,i+k-1,j,j) - get2(i+k-1,i+k-1,j + k- 1,j + k-1) - get2(i,i,j + k- 1,j + k-1);;

	return 	w.first*(2LL*i + k - 1LL) == tmp.first*2LL && w.first*(2LL*j + k - 1LL) == tmp.second*2LL; 
}
int main()
{
	freopen("google.in","r",stdin);
	freopen("google.out","w",stdout);
	int nt;
	cin>>nt;
	for(int it=1;it<=nt;it++)
	{
		int d;
		string tmp;
		cin >> n >>m >> d;
		vector<vector<pair<ll,ll> > > a(n);
		for (int i=0;i<n;++i){
			a[i].resize(m);
			cin >> tmp;
			for (int j=0;j<m;++j){
				a[i][j].first = ((tmp[j] - '0')+d);
				a[i][j].second = ((tmp[j] - '0')+d);
			}
		}
		p.clear();
		p.resize(n+1);
		p2.resize(n+1);
		for (int i=0;i<n+1;++i){
			p[i].resize(m+1,mpair(0,0));
		}
		for (int i=0;i<n+1;++i){
			p2[i].resize(m+1,mpair(0,0));
		}
		for (int i=0;i<n;++i){
			for (int j=0;j<m;++j){
				p[i+1][j+1].first = p[i][j+1].first + p[i+1][j].first - p[i][j].first + i*a[i][j].first; 
				p[i+1][j+1].second = p[i][j+1].second + p[i+1][j].second - p[i][j].second + j*a[i][j].second; 
			}
		}
		for (int i=0;i<n;++i){
			for (int j=0;j<m;++j){
				p2[i+1][j+1].first = p2[i][j+1].first + p2[i+1][j].first - p2[i][j].first + a[i][j].first; 
				p2[i+1][j+1].second = p2[i][j+1].second + p2[i+1][j].second - p2[i][j].second + a[i][j].second; 
			}
		}
		int ans = -1;
		for (int i=0;i<n;++i){
			for (int j=0;j<m;++j){
				for (int k=max(3,ans);k<=n && k <= m;++k){
					if (can(i,j,k)) {
						ans = k;
					}
				}
			}
		}
		cout<<"Case #"<<it<<": ";
		if (ans == -1){
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << ans << endl;
		}
	}
	return 0;
}
