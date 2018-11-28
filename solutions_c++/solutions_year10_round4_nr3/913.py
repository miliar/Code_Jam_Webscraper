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
#include <climits>
#include <cstring>
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

bool b[111][111];

bool bb[111][111];

bool fn(){
	F(i,101) F(j,101) if(b[i][j])	return true;
	return false;
}

void Print(){
	cout<<endl;
	FF(i,1,7){
		FF(j,1,7) cout<<b[i][j];
		cout<<endl;
	}
	cout<<endl;
}

int main(){
	int tst,kas=1;
	cin>>tst;
	while(tst--){
		cout<<"Case #"<<kas++<<": ";
		int R;
		cin>>R;
		CLR(b,0);
		while(R--){
			int x1,y1,x2,y2;
			cin>>x1>>y1>>x2>>y2;
			FF(i,x1,x2+1)
				FF(j,y1,y2+1)
					b[j][i]=1;
		}
		int ans=0;
//		Print();
		while(fn()){
			memcpy(bb,b,sizeof(bb));
			FF(i,1,101){
				FF(j,1,101){
					if(b[i-1][j] && b[i][j-1])	bb[i][j]=1;
					if(!b[i-1][j] && !b[i][j-1])	bb[i][j]=0;
				}
			}
			memcpy(b,bb,sizeof(bb));
//			Print();
			ans++;
		}
		cout<<ans<<endl;
	}
	return 0;
}
