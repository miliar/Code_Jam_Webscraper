#include<cstdio>
#include<iostream>
#include<algorithm>
#define L 300

using namespace std;

typedef long long ll;

ll m,f,n;
ll pp,ss,p[L],s[L];
ll l,r;
pair<ll,ll> xl[L];
int T,I=0;

ll calc(ll t){
	ll amount = m-f*t;
	ll each = amount/t;
	ll last=-1;
	ll next=-1;
	ll ans=0;
	for (int i=0;i<n;++i){
		ll days=each/p[i];
		ll times=min(days,s[i]-last);
		ans+=times*t;
		each-=times*p[i];
		amount-=times*p[i]*t;
		if (days<s[i]-last){
			next=p[i];
			break;
		}
		last=s[i];
	}
	if (next!=-1)
		ans+=amount/next;
	return ans;
}

void solve(){
	cin >> m >> f >> n;
	for (int i=0;i<n;++i){
		cin >> pp >> ss;
		xl[i]=make_pair(ss,pp);
	}
	sort(xl,xl+n);
	for (int i=0;i<n;++i){
		p[i]=xl[i].second;
		s[i]=xl[i].first;
	}
	for (int i=n-1;i>0;--i)
		if (p[i]<p[i-1])
			p[i-1]=p[i];
	l=1;
	r=m/f;
	ll ans=-1;

	while (l<r){
		ll mid1=(l+l+r)/3;
		ll mid2=(l+r+r+2)/3;
		ll calc1=calc(mid1);
		ll calc2=calc(mid2);
		if (calc1>calc2)
			r=mid2-1;
		else if (calc1<calc2)
			l=mid1+1;
		else if (calc1==calc2){
			cerr << "delta " << r-l+1 << endl;
			if (r-l>100000){
				r=mid2-1;
				continue;
			}
			ans=-1;
			for (ll i=l;i<=r;++i)
				ans=max(ans,calc(i));
			cout << ans << endl;
			return;
		}
	}

	cout << calc(l) << endl;
}

int main(){
	cin >> T;
	while (T--){
		cout << "Case #" << ++I << ": ";
		solve();
	}
}
