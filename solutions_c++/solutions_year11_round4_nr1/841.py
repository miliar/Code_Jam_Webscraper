#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
void doo()
{

	vector<pair<double, double> > a;
	int len, w, r,  n;
	double t;
	cin >> len >>  w >> r >> t >> n;
	int tot=0;
	r-=w;
	for(int i=0; i<n; i++){
		int b, e, add;
		cin >> b >> e >> add;
		a.push_back(make_pair(w+add, e-b));
		tot+=e-b;
	}
	a.push_back(make_pair(w, len-tot));
	sort(a.begin(), a.end());
	n++;
	for(int i=0; i<n; i++){
		//cerr<< a[i].first<<" " << a[i].second<<endl;
	}
	double ans=0;
	for(int i=0; i<n; i++){
		double use= a[i].second/(a[i].first+r);
		if(t<use)
			use=t;
		t-=use;
		//cerr<<use<<endl;
		//cerr<<r<<endl;
		ans+= use + (a[i].second - (a[i].first+r)*use)/ a[i].first;
		//cerr<<ans<<endl;
	}
	printf(" %.10lf", ans);
}
int main()
{
	int ncase;
	cin >> ncase;
	for(int i=0; i<ncase; i++)
	{
		cout<<"Case #"<<i+1<<":";
		doo();
		cout<<endl;
	}
}
