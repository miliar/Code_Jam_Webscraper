#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <algorithm>
#include <iterator>
#include <functional>
#include <utility>
#include <numeric>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cassert>

using namespace std;

#define allof(c) ((c).begin()),((c).end())
#define debug(c) cout<<"> "<<#c<<" = "<<c<<endl;
#define iter(c) __typeof((c).begin())
#define tr(i,c) for(iter(c) i=(c).begin();i!=(c).end();i++)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define repd(i,n) for(int i=(int)(n-1);i>=0;i--)
#define repi(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define mp make_pair
#define fst first
#define snd second
#define pb push_back

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef pair<double,double> pdd;

#define INFTY 1000000000




int main(){
	int L,D,N; cin>>L>>D>>N;
	vector<string> ss(D);
	rep(i,D){
		cin>>ss[i];
	}
	rep(i,N){
		vector<vector<bool> > ps(L,vector<bool>(26,false));
		bool isin=false;
		string s; cin>>s;
		for(int j=0,p=0;j<L;p++){
			char c=s[p];
			if(c=='(') isin=true;
			if(c==')') isin=false;
			if(isalpha(c)) ps[j][c-'a']=true;
			if(!isin) j++;
		}
		int ans=0;
		rep(j,D){
			bool flg=true;
			rep(k,L){
				flg&=ps[k][ss[j][k]-'a'];
			}
			if(flg) ans++;
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
	
	return 0;
}
