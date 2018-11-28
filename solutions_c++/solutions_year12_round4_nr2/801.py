#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <math.h>
using namespace std;
#define LL __int64
#define MIN(a,b) (((a)<(b))?(a):(b))
#define SQR(x) ((x)*(x))
LL R[1000];
LL X[1000];
LL Y[1000];
LL W,L;
LL N;
void placeCircles(void){
	X[0]=0;
	Y[0]=0;
	LL f=0;
	vector<LL> h;
	vector<LL> v;
	vector<LL> hi;
	vector<LL> vi;
	h.push_back(0);
	v.push_back(0);
	hi.push_back(0);
	vi.push_back(0);

	bool h_ok=true;
	bool v_ok=true;
	LL current=1;
	while((h_ok || v_ok) && (current<N)){
		if(f==0){
			if(h[h.size()-1]+R[hi[hi.size()-1]]+R[current]<=W){
				X[current]=h[h.size()-1]+R[hi[hi.size()-1]]+R[current];
				Y[current]=0;
				h.push_back(X[current]);
				hi.push_back(current);
				++current;
			}else{
				h_ok=false;
			}
		}else{
			if(v[v.size()-1]+R[vi[vi.size()-1]]+R[current]<=L){
				Y[current]=v[v.size()-1]+R[vi[vi.size()-1]]+R[current];
				X[current]=0;
				v.push_back(Y[current]);
				vi.push_back(current);
				++current;
			}else{
				v_ok=false;
			}
		}
		//--
		f=1-f;
	}
	for(unsigned i=1;(i<h.size())&&(current<N);++i){
		for(unsigned j=1;(j<v.size())&&(current<N);++j,++current){
			X[current]=h[i];
			Y[current]=v[j];
		}
	}
	//---check
	/*if(current<N){
		cerr<<"Missing circles"<<endl;
	}
	for(int i=0;i<N;++i){
		for(int j=i+1;j<N;++j){
			//cerr<<"Diff: "<<i<<", "<<j<<":\t"<<SQR(X[i]-X[j])+SQR(Y[i]-Y[j])-SQR(R[i]+R[j])<<endl;
			if(SQR(X[i]-X[j])+SQR(Y[i]-Y[j])<SQR(R[i]+R[j])){
				cerr<<"Intersection: "<<i<<", "<<j<<endl;
			}
		}
	}*/

}

int main(int argc, char *argv[]){
	LL T;
	cin>>T;
	for(LL c=1;c<=T;++c){
		cin>>N;
		cin>>W>>L;
		/*W*=2;
		L*=2;*/
		vector<pair<LL, LL> >v;
		for(LL i=0;i<N;++i){
			cin>>R[i];
//			R[i]*=2;
			v.push_back(make_pair(R[i],i));
		}
		sort(v.rbegin(), v.rend());
		for(int i=0;i<N;++i){
			R[i]=v[i].first;
		}
		placeCircles();
		cout<<"Case #"<<c<<":";
		for(int i=0;i<N;++i){
			for(int j=0;j<N;++j)if(v[j].second==i){
				cout<<" "<<X[j]<<" "<<Y[j];
			}
			//cout<<" "<<0.5*X[v[i].second]<<" "<<0.5*Y[v[i].second];
			
		}
		cout<<endl;
	}

	return 0;
}

