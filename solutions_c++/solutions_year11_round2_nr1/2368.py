#include<queue>
#include<set>
#include<deque>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<map>
#include<fstream>
using namespace std;
#define dbg(x) cout << #x << " -> " << (x) << "\t";
#define rep(i,n) for(int i=0;i<n;i++)
#define pb push_back
#define sz size()
#define psi pair<string,int>
#define all(x) x.begin(),x.end()
#define GI ({int t;scanf("%d",&t); t;})
#define flush(x) memset(x,0,sizeof(x))
//#define ll long long
#define dl double
struct node {
	int p,w,l;
	dl wp,owp,oowp;
};
double rpi(dl WP,dl OWP,dl OOWP) {
	double RPI;
	RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP;
	return RPI;
}
int main() {
	int t=GI,cases=1;
	while(t--) {
		int n=GI;
		vector<string> s;
		string temp;
		rep(i,n) {
			cin>>temp;
			s.pb(temp);
		}	
		node v[102];
		rep(i,s.sz) v[i].p=0,v[i].w=0,v[i].l=0;
		rep(i,s.sz) {
			rep(j,s[i].sz) {
				if(s[i][j]!='.') {
					v[i].p++;
					if(s[i][j]=='1') v[i].w++;
					else v[i].l++;
				}
//				cout<<"played "<<v[i].p<<" and won "<<v[i].w<<endl;
			}
		}
		rep(i,s.sz)  v[i].wp = (dl) (v[i].w*1.0/v[i].p*1.0);	
		node o[103];
		
		rep(cur,s.sz) {
			dl rr=0.0,count=0.0;
			rep(i,s.sz) {
				if(s[cur][i]!='.') {
				count+=1.0;
				dl ww=0,ll=0,pp=0;
				rep(j,s.sz) {
					if(cur!=i&&cur!=j) {
						if(s[i][j]!='.') {
							pp+=1.0;
							if(s[i][j]=='1') ww+=1.0;
							else ll+=1.0;
						}		
					}
				}
				rr+= (dl) ww/ (dl) pp;
				}
			}
			v[cur].owp=(dl) rr/ (dl) count;
//			cout<<"cur rr dl "<<cur<<" "<<rr<<" "<<count<<" "<<v[cur].owp<<endl;
			
		}
		rep(i,s.sz) {
			dl res=0,cnt1=0.0;
			rep(j,s.sz) if(i!=j&&s[i][j]!='.') res+=v[j].owp,cnt1+=1.0;
		    v[i].oowp=(dl) ((res*1.0)/(cnt1*1.0));
		}
		dl rw=0.0,rop=0.0,roop=0.0;
		cout<<"Case #"<<cases<<":"<<endl;
		rep(i,s.sz) {
		   double result=rpi(v[i].wp,v[i].owp,v[i].oowp);
		   cout<<result<<endl;
		}
		/*rep(i,s.sz) {
			cout<<v[i].p<<" "<<v[i].w<<" "<<v[i].l<<" "<<v[i].wp<<" "<<v[i].owp<<" "<<v[i].oowp<<endl;
		}*/
		cases++;
	}	
	return 0;
}
