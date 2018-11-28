#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <memory.h>

using namespace std;

#define allof(c) ((c).begin()),((c).end())
#define debug(c) cerr<<"> "<<#c<<" = "<<(c)<<endl;
#define iter(c) __typeof((c).begin())
#define tr(i,c) for(iter(c) i=(c).begin();i!=(c).end();i++)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define REP(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define mp make_pair
#define fst first
#define snd second
#define pb push_back

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long ll;


int main(){
	int T; cin>>T;
	for(int iCase=1;iCase<=T;iCase++){
		int X,S,R,N;
		double t; cin>>X>>S>>R>>t>>N;
		vi Bs(N),Es(N),ws(N);
		rep(i,N) cin>>Bs[i]>>Es[i]>>ws[i];
		
		vi d(N);
		rep(i,N) d[i]=Es[i]-Bs[i];
		int D=X;
		rep(i,N) D-=d[i];
		
		d.pb(D);
		ws.pb(0);
		N++;
		
		vector<pair<double,int> > p;
		rep(i,N){
			p.pb(mp((ws[i]+R)/(double)(ws[i]+S),i));
		}
		sort(allof(p));
		reverse(allof(p));
		double ans=0;
		rep(j,N){
			int i=p[j].snd;
			double t1=d[i]/(double)(ws[i]+R);
			if(t>=t1){
				ans+=t1;
				t-=t1;
			}
			else{
				double x=t*(ws[i]+R);
				ans+=t+(d[i]-x)/(double)(ws[i]+S);
				t=0;
			}
		}
		cout<<"Case #"<<iCase<<": ";
		printf("%.10f\n",ans);
		
	}
	return 0;
}
