#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>


 
using namespace std;
 
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef vector<ll > vl;
 
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

char buf[60];
string calc(string in){
	FOR(i,0,sz(in)){
		if(in[i]=='?'){
			in[i]='0';
			string s1 =calc(in);
			if(s1!="")return s1;
			in[i]='1';
			s1 = calc(in);
			in[i]='?';
			return s1;
		}
	}
	FOR(i,0,60)buf[i]='0';
	int N = sz(in);
	FOR(i,0,N)buf[i+60-N]=in[i];
//	FOR(i,0,60)cout << buf[i];
//	cout << endl;
	vl cur = vl(4);
	FOR(i,0,60){
		if(buf[i]=='1'){
//			cout <<"nz "<< i <<  endl;
			int od = i/15;
			int rt = 14-(i-15*od);
//			cout << od << " " << rt << endl;
			cur[od]|=1<<rt;
		}
	}
	ll lo = 1, hi = (1LL<<31)-1;
//	cout << in << endl;
//	FOR(i,0,4)cout << cur[i] << " ";
//	cout << endl;
	while(lo<=hi){
		ll mid = lo + (hi-lo)/2;
//		cout << mid << endl;
		vl res = vl(4);
		ll p1 = mid >>15;
		ll p2 = mid &((1<<15)-1);
		res[1]=p1*p1;
		res[2]=2*p1*p2;
		res[3]=p2*p2;
		FORD(i,1,4){
			res[i-1]+=res[i]>>15;
			res[i]&=(1<<15)-1;
		}
//		FOR(i,0,4)cout << res[i] << " ";
//		cout << endl;
		if(res==cur)return in;
		if(res<cur){
			lo = mid+1;
		} else {
			hi = mid-1;
		}
	}
//	cout << endl;
	return "";
}
int main(){
	int TC;
	cin>>TC;
	FOR(tc,1,TC+1){
		string in;
		cin >> in;
		cout << "Case #" << tc << ": "<<calc(in) << endl;
	}
	return 0;
}
