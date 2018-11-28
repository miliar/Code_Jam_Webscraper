#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

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
/*
void fun(){
	REPEAT(i,A,(B+1)){
			string s,fix;
			stringstream par;
			par<<i;
			par>>s;
			fix = s;
			s = s + s;
			REP(j,s.sz/2){	
				string w;
				int n;
				w = s.substr(j,s.sz/2);
				stringstream par;
				par<<w;
				par>>n;
				//cout<<w<<" "<<n<<endl;
				if(w[0]!='0'){
					if(n<=B && n>=A && n>i){
						cout<<fix<<" "<<w<<endl;
						ans++;
						}
						
					}
				}
			//101101 101 011 110 101
			}
	}
*/
int main(){
	int T;
	cin>>T;
	REP(i,T){
		int A,B;
		ll ans=0;
		cin>>A>>B;
		//map < pair <int,int> , bool > mp;
		REPEAT(i,A,(B+1)){
			set <int> st;
			pair<set<int>::iterator,bool> ret;
			string s,fix;
			stringstream par;
			par<<i;
			par>>s;
			fix = s;
			s = s + s;
			REP(j,s.sz/2){	
				//map<int,bool>::iterator it;
				string w;
				int n;
				w = s.substr(j,s.sz/2);
				stringstream par;
				par<<w;
				par>>n;
				//cout<<w<<" "<<n<<endl;
				if(w[0]!='0'){
					if(n<=B && n>=A && n<i){
						//cout<<i<<" "<<n<<endl;
						//v.pb(mkp(i,n));
						ret = st.insert(n);
						if(ret.second == false);	
							//cout<<n<<endl;
						else
							ans++;
						}
						
					}
				//EACH(it,st)cout<<*it<<" ";
				//ans+= (int) st.sz;
				}
			st.clear();
			}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
		//EACH(it,v) cout<<it->first<<" "<<it->second<<endl;
		}
	return 0;
	}