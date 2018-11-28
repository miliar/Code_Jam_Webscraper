#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<sstream>
using namespace std;

#define FOR(i,a,b) for(int i = (a); i < int(b); ++ i)
#define REP(i,n) FOR(i,0,n)
#define sz size()
#define pb push_back
#define cs c_str()
#define V(x) vector< x >

typedef V(int) VI;
typedef V(VI) VVI;
typedef V(string) VS;

int toInt(string s){ int r=0; istringstream sin(s); sin>>r; return r; }

int main() {
	string t;
	int num;
	getline(cin,t);
	num = toInt(t);
		
	REP(z,num) {
		int P, K ,L;
		cin>> P >> K >>L;
		VI arr(L);
		REP(i,L) cin >> arr[i];
		sort(arr.begin(),arr.end());
		reverse(arr.begin(),arr.end());
		long long ct =1, res =0;
		for(int a=0 ;a<arr.sz && ct<=P;ct++) {
			for(int j=a;j<a+K && j< arr.sz;++j) res += ct*arr[j];
			a += K;
		}
		//if(a < arr.sz && ct>P) cout << "Case #" << z+1 << ": "<<endl;
		cout << "Case #" << z+1 << ": "<< res <<endl;
	}
	return 0;
}
