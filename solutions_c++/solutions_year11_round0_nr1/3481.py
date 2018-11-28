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


int main(){
	int T; cin>>T;
	rep(iCase,T){
		int N; cin>>N;
		queue<int> bo[2],s,sc;
		rep(i,N){
			char c; int p; cin>>c>>p;
			s.push(p);
			if(c=='B'){
				bo[0].push(p);
				sc.push(0);
			}
			else{
				bo[1].push(p);
				sc.push(1);
			}
		}
		int rp[2]; rp[0]=rp[1]=1;
		int ans;
		for(ans=1;;ans++){
			bool pop=false;
			rep(r,2){
				if(bo[r].size()==0) continue;
				int d=bo[r].front()-rp[r];
				int sign=d<0?-1:1;
				if(d==0){
					if(r==sc.front() && s.front()==bo[r].front()){
						bo[r].pop();
						pop=true;
					}
				}
				else{
					rp[r]+=sign;
				}
			}
			if(pop){
				s.pop();
				sc.pop();
			}
			if(s.size()==0) break;
		}
		
		cout<<"Case #"<<iCase+1<<": ";
		cout<<ans<<endl;
	}
	
	
	return 0;
}
