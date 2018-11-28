#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<map>
#include<set>
#include<cstring>
#include<string>
#include<queue>
#include<cctype>
#include<functional>
#include<fstream>
#include<sstream>
#include<complex>
#include<cmath>
#include<cstdlib>
#include<ctime>
using namespace std;

#define EPS 1.0e-10
#define ALL(t) t.begin(),t.end()
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(it,c) for(__typeof((c).begin()) it = (c).begin();it != (c).end();++it)
#define ll long long
#define mp make_pair
#define pb push_back
#define F first
#define S second
const ll mod=1000000007LL;
const int SIZE = 100000;
int main() {
	int x;
	cin>>x;
	string a,b;
	getline(cin,a);
	b="yhesocvxduiglbkrztnwjpfmaq";
	REP(i,x){
		getline(cin,a);
		cout<<"Case #"<<i+1<<": ";
		REP(i,a.size()){
			if(a[i]==' ') cout<<" ";
			else cout<<b[a[i]-'a'];
		}
		cout<<endl;
	}
	return 0;
}
