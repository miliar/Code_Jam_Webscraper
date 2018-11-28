/*
Nguyen Tran Nam Khanh
microsoft
*/
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cmath>
#include <cstdio>

using namespace std;

#define Clear(t) memset((t),0,sizeof(t))
#define For(i,a,b) for (int i=(int)(a),_t = (int)(b);i<=_t;i++)
#define Ford(i,a,b) for (int i=(int)(a), _t = (int)(b);i>=_t;i--)
#define Rep(i,n) for (int i=0, _t = (int)(n);i<_t;i++)
#define tr(it, c) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define SZ(t) ((int)((t).size()))
#define All(v) (v).begin(),(v).end()
#define Sort(v) sort(All(v))
#define pb push_back

typedef vector<int> VI;
typedef long long ll;
typedef vector<ll> VL;
typedef vector<string> VS;

string i2s(int x) { ostringstream o; o<<x; return o.str(); }
int s2i(string s) { int x; istringstream i(s); i>>x; return x; }

map<string,string> mc;
set<string> mo;
int c, n;
string s;

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int st;
	scanf("%d",&st);
	
	For(ts,1,st) {
		mc.clear();
		mo.clear();
		cin>>c;
		Rep(i,c) {
			string ss;
			cin>>ss;
			mc[ss.substr(0,2)]=ss.substr(2,1);
			swap(ss[0],ss[1]);
			mc[ss.substr(0,2)]=ss.substr(2,1);
		}
		
		cin>>c;
		Rep(i,c) {
			string ss;
			cin>>ss;
			mo.insert(ss);
			swap(ss[0],ss[1]);
			mo.insert(ss);
		}
		
		cin>>n;
		cin>>s;
		
		string res = "";
		int len = 0;
		Rep(i,n) {
			res+=s[i];
			len++;
			
			bool stop = false;
			while (!stop) {
				stop = true;
				if (len>=2) {
					string last2 = res.substr(len-2,2);
					if (mc.find(last2)!=mc.end()) {
						res = res.substr(0,len-2);
						res+=mc[last2];
						len--;
						stop = false;
					}
				}
			}

			Rep(j,len-1) {
				string popp = "";
				popp+=res[j];
				popp+=res[len-1];
				if (mo.find(popp)!=mo.end()) {
					res = "";
					len = 0;
					break;
				}
				popp = "";
				popp+=res[len-1];
				popp+=res[j];
				if (mo.find(popp)!=mo.end()) {
					res = "";
					len = 0;
					break;
				}
			}			
		}
		cout<<"Case #"<<ts<<": [";
		if (len>0) cout<<res[0];
		For(i,1,len-1) cout<<", "<<res[i];
		cout<<"]"<<endl;
		
	}

	return 0;
}
