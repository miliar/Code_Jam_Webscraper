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

typedef long long ll; 
typedef vector<int> vi; 
typedef pair<int,int> pii;

int main(){
	int T; cin>>T;
	for(int iCase=1;iCase<=T;iCase++){
		int N; cin>>N;
		vector<string> sd(N);
		rep(i,N) cin>>sd[i];
		vector<double> wp(N,0),owp(N,0),oowp(N,0);
		rep(i,N){
			int pn=0;
			rep(j,N) if(sd[i][j]!='.'){
				wp[i]+=(sd[i][j]=='1');
				pn++;
			}
			wp[i]/=pn;
		}
		
		rep(i,N){
			int pn=0;
			rep(j,N) if(sd[i][j]!='.'){
				double wp2=0;
				int pn2=0;
				rep(k,N) if(i!=k) if(sd[j][k]!='.'){
					wp2+=(sd[j][k]=='1');
					pn2++;
				}
				owp[i]+=wp2/pn2;
				pn++;
			}
			owp[i]/=pn;
		}
		rep(i,N){
			int pn=0;
			rep(j,N) if(sd[i][j]!='.'){
				oowp[i]+=owp[j];
				pn++;
			}
			oowp[i]/=pn;
		}
		cout<<"Case #"<<iCase<<": "<<endl;
		rep(i,N) cout<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
	}
	
	return 0;
}
