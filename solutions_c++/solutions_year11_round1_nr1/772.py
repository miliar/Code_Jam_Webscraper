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
		ll N;
		int pd,pg;
		cin>>N>>pd>>pg;
		
		int k;
		for(k=1;k<=101;k++) if((k*pd)%100==0) break;
		//debug(k)
		cout<<"Case #"<<iCase<<": ";
		if(k!=101 && k<=N){
			if(pd!=100 && pg==100) cout<<"Broken"<<endl;
			else if(pd>0 && pg==0) cout<<"Broken"<<endl;
			else cout<<"Possible"<<endl;
		}
		else cout<<"Broken"<<endl;
		
	}
	
	return 0;
}
