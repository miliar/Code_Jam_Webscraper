#include <iostream>
using namespace std;
int n;
struct rp{
	int d, l, ind, ans;
};
rp r[10001];
bool operator<(const rp& a,const rp& b){
	return a.d<b.d;
}
int main(){
	int tnum, tcou=0;
	cin>>tnum;
	while (tnum--){
		cin>>n;
		for (int i=0;i<n;++i)
			cin>>r[i].d>>r[i].l;
		int D;cin>>D;
		r[n].d=D;
		r[n].l=0;
		++n;
		for (int i=0;i<n;++i){
			r[i].ind=i;
			r[i].ans=-1;
		}
		r[0].ans=r[0].d;
		sort(r, r+n);
		for (int i=0;i<n;++i){
			if (r[i].ans==-1)
				continue;
			if (r[i].ans>r[i].l)
				r[i].ans=r[i].l;
			for (int j=i+1;j<n && r[j].d-r[i].d<=r[i].ans;++j)
				r[j].ans=max(r[j].ans,r[j].d-r[i].d);
		}
		bool ans;
		for (int i=0;i<n;++i)
			if (r[i].ind==n-1)
				ans=(r[i].ans>=0);
		cout<<"Case #"<<++tcou<<": "<<(ans?"YES":"NO")<<endl;
	}
	return 0;
}
