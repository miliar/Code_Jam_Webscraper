/*
*  Javier Segovia
*  0.016
*/
#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;
#define SL size()
#define LE length()
#define PB push_back
#define MP make_pair
#define X first
#define Y second
int N,W,L;
vector<pair<int,int> > R;
pair<int,int> r;
//vector<pair<pair<int,int> , pair<int,int> > > T;
pair<int,int> S[1005];
int rad[1005];
int w,l,w0,l0;

bool fit(int p){
	r = R[p];
	w = rand()%(W+1);
	l = rand()%(L+1);
	S[p].X = w;
	S[p].Y = l;
	long long dist,ww,ll,sqr;
	
	for (int i=0; i<p ; i++) {
		w0 = S[i].X;
		l0 = S[i].Y;
		ww = w0 - w; ww = ww*ww;
		ll = l0 - l; ll = ll*ll;
		dist = ww + ll;
		/*cout<<endl;
		cout<<"W: "<<w<<" W0: "<<w0<<endl;
		cout<<"L: "<<l<<" L0: "<<l0<<endl;
		cout<<"DIST: "<<dist<<endl;
		cout<<"RAD["<<p<<"]: "<<rad[p]<<" RAD["<<i<<"]: "<<rad[i]<<endl;*/
		sqr = (rad[i] + rad[p]); sqr = sqr*sqr ;
		if(dist < sqr ) return false;
	}
	return true;
	
}

int main(){
	int kases; cin>>kases;
	for (int k=1; k<=kases; k++) {
		cin>>N>>W>>L;
		R.clear();
		for (int i=0; i<N ; i++) {
			cin>>rad[i];
			r.X = rad[i];
			r.Y = i;
			R.PB(r);
		}
		sort(R.rbegin(),R.rend());
		
		cout<<"Case #"<<k<<": "<<W<<" "<<L;
		S[0].X = W;
		S[0].Y = L;
		for (int i=1; i<N ; i++) {
			while (!fit(i)) { }
			cout<<" "<<S[i].X<<" "<<S[i].Y;
		}cout<<endl;
		//cout<<RAND_MAX<<endl;
	}
}