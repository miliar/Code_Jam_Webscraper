/*	SURENDRA KUMAR MEENA	*/
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
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long int LL;
#define ALL(s) (s).begin(),(s).end()
#define R(i,m,n)	for(int i=m;i>=n;i--)
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define VI vector<int>
#define PB push_back
#define CLR(s,v) memset(s,v,sizeof(s))
string to_str(LL x){ ostringstream o;o<<x;return o.str();}
LL to_int(string s){ istringstream st(s); LL i;	st>>i;return i;}
#define FR(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)
typedef pair<int,int> PI;
#define MP(x,y) make_pair(x,y)
#define f first
#define s second
#define VP vector<PI>
#define S(t)	scanf("%d",&t)
string s[100];
int n;
bool fn(VI &v){
	F(i,n)	if(v[i]>i+1)	return false;
	return true;
}
int main(){
	int t;
	cin>>t;
	int cas=1;
	while(t--){
		cin>>n;
		F(i,n)	cin>>s[i];
		VI v;
		F(i,n){
			R(j,n-1,0){
				if(s[i][j]=='1'){
					v.PB(j+1);
					break;
				}
			}
			if(v.size()<i+1)	v.PB(0);
		}
		int ans=0;
		while(!fn(v)){
			F(i,n){
				if(v[i]>i+1){
					FF(j,i+1,n){
						if(v[j]<=i+1){
							int el=v[j];
							ans+=j-i;
							v.erase(v.begin()+j);
							v.insert(v.begin()+i,el);
							break;
						}
					}
					break;
				}
			}
		}
		cout<<"Case #"<<cas++<<": "<<ans<<endl;
	}
	return 0;
}
