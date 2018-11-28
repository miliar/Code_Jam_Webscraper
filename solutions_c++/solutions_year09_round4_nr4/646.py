#include<iostream>
#include<vector>
#include<string>
#include <iomanip>
#include<map>
#include<cmath>
#define mmax 1000
using namespace std;
int N;
vector<int>  which_t;
vector<int>  x;
vector<int>  y;
vector<int>  r;

double get_r(int ind){
	double le=0; double ri = 1000000; double R;
	while(fabs(le-ri)>1e-10){
		R=(le+ri)/2;
		bool anyt=false;
		bool rgood=true;
		for(int i=0; i<N; i++){
			if(which_t[i]==ind){
				anyt=true; if(R<r[i]){
					rgood=false; break;
				}
			}
			for(int j=0; j<i; j++){
				if(which_t[i]!=ind || which_t[j]!=ind)continue;
				double dist = 
sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]))+r[i]+r[j];
				if(dist>2*R){
					rgood=false; break;
				}
			}
			if(!rgood)break;
		}
		if(!anyt) return 0;
		if(rgood){
			ri=R;
		}else{
			le=R;
		}
	}
	return R;
}
int main(){
	int T;
	cin>>T;
	for(int ii=0; ii<T; ii++){
		cin>>N;
		which_t.clear(); which_t.resize(N, 1);
		r.clear(); r.resize(0);
		x.clear(); x.resize(0);
		y.clear(); y.resize(0);
	//	t.clear(); t.resize(N, 2);
		for(int j=0; j<N; j++){
			int X, Y, R;
			cin>>X>>Y>>R;
			x.push_back(X);
			y.push_back(Y);
			r.push_back(R);
		}
		
		double res=1000000;
		double tmp = max(get_r(1), get_r(2));
		res=min(res, tmp);
		for(int i=0; i<N; i++){
			which_t.clear(); which_t.resize(N, 1);
			which_t[i]=2;
			tmp = max(get_r(1), get_r(2));
			res=min(res, tmp);
		}
		cout<<"Case #"<<ii+1<<": " << res<<"\n";
	}
	
}
