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
	
	REP(e,x){
		int a,b,ans=0;
		cin>>a>>b;
		for(int i=a;i<b;i++){
			ostringstream os;
			os<<i;
			string c;
			c=os.str();
			bool check[2000010]={0};
			for(int j=1;j<c.size();j++){
				string d=c.substr(j)+c.substr(0,j);
				stringstream is;
				is<<d;	int y; is>>y;
				if(y>i&&y<=b&&!check[y]){
					ans++; check[y]=true;
				}
			}
		}
		cout<<"Case #"<<e+1<<": "<<ans<<endl;
	}
	return 0;
}
