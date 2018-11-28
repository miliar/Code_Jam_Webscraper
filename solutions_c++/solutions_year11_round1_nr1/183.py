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

bool fn(LL n,LL pd,LL pg){
	LL D=1LL;
	for(D=1LL;D<101;D++){
		if((D*pd)%100)	continue;
		if(D>n)	return false;
		break;
	}
	LL win = (D*pd)/100LL;
	LL lost = D-win;
	if(lost>0 && pg==100)	return false;
	if(win>0 && pg==0)		return false;
	return true;
}

int main(){
	int t;
	cin>>t;
	FF(kase,1,t+1){
		cout<<"Case #"<<kase<<": ";
		LL n,pd,pg;
		cin>>n>>pd>>pg;
		if(fn(n,pd,pg))	cout<<"Possible\n";
		else					cout<<"Broken\n";
	}
	return 0;
}
