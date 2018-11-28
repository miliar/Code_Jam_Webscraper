#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define mkp make_pair

typedef long long ll;
int main(){
	int T;
	cin>>T;
	REP(i,T){
		int Pd,Pg;
		ll N;
		bool t = false;
		cin>>N>>Pd>>Pg;
		if(Pd != 100 && Pg == 100) t = false;
		else if(Pd != 0 && Pg == 0) t = false;
		else{
			REPEAT(j,1,101){
				int x;
				x = (Pd*j)%100;
				if(!x && j<=N) {
					t = true;
					break;
					}
				}
			}
		if(t)
			cout<<"Case #"<<i+1<<": Possible"<<endl;
		else 
			cout<<"Case #"<<i+1<<": Broken"<<endl;
		}	
	return 0;
	}