#include<iostream>
#include<string>
#include<vector>
#include<utility>
#include<algorithm>

using namespace std;

struct way{
	double l;
	double v;
	bool operator<(const way &w)const{
		return v<w.v;
	}
};

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int Q;
	cin >> Q;
	for(int q=0;q<Q;q++){
		cout << "Case #" << q+1 << ": ";
		double L,S,R,r;
		int n;
		cin >> L >> S >> R >> r>>n;
		vector<way> a;
		int l=0;
		for(int i=0;i<n;i++){
			way w;
			int x,y;
			cin >> x >> y >> w.v;
			w.l=y-x;
			l+=y-x;
			a.push_back(w);
		}
		way w;
		w.l=L-l;
		w.v=0;
		a.push_back(w);
		sort(a.begin(),a.end());
		double t=0;
		int i=0;
		while(r>0 && i<a.size()){
			double l=a[i].l;
			double v=a[i].v;
			if(l/(v+R)>r){
				t+=r+(l-(v+R)*r)/(v+S);
				r=0;
			}
			else{
				t+=l/(v+R);
				r-=l/(v+R);
			}
			i++;
		}
		for(;i<a.size();i++){
			t+=a[i].l/(a[i].v+S);
		}
		printf("%.7f\n",t);
	}
	return 0;
}


