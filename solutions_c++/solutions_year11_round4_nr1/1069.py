#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<utility>
#include<algorithm>
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(a) ((a)>0?(a):(-(a)))

using namespace std;

double bs[2000];
double es[2000];
double ss[2000];
pair <double, pair<double, double> > go[2000];
int main(){
	int cas;
	cin>>cas;
	for(int ca = 1; ca<=cas; ++ca){
		double sp, dst;
		double X, S,R,t;
		int n;
		cin>>X>>S>>R>>t>>n;
		double nob = 0;
		double rtn  = 0;
		double le = 0;
		for(int i=0; i<n; ++i){
			cin>>go[i].second.first>>go[i].second.second>>go[i].first;
			nob += go[i].second.first - le;
			le = go[i].second.second;
		}
		nob += X-le;
		//cout<<nob<<endl;
		double tt = nob/R;
		if (tt>t){
			nob -= R*t;
			rtn += t + (nob/S);
			t = 0;
		}else {
			t-= tt;
			rtn += tt;
		}
		
		sort(go, go+n);
		
		for(int i=0; i<n; ++i){
			double r = R+go[i].first;
			double s = S+go[i].first;
			nob = go[i].second.second-go[i].second.first;
			tt = nob/r;
			if (tt>t){
				nob -= r*t;
				rtn += t + (nob/s);
				t = 0;
			}else {
				t-= tt;
				rtn += tt;
			}
		}
		
		printf ("Case #%d: %.8f\n", ca, rtn);
	}
}