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
int l,d,n;
string a[6000];
map<char,int> m[200];

bool isValid(int j){
	F(i,l)	if(!m[i][a[j][i]])	return false;
	return true;
}

int main(){
	cin>>l>>d>>n;
	F(i,d)	cin>>a[i];
	FF(t,1,n+1){
		cout<<"Case #"<<t<<": ";
		F(i,200)	m[i].clear();
		string s;
		cin>>s;
		int i=0,cnt=0,len=s.size(),pos=0;
		while(i<len){
			if(s[i]=='('){
				i++;
				while(s[i]!=')'){
					m[pos][s[i]]=1;
					i++;
				}
			}
			else	m[pos][s[i]]=1;
			i++;
			pos++;
		}
		F(j,d)	if(isValid(j))	cnt++;
		cout<<cnt<<endl;
	}
	return 0;
}
