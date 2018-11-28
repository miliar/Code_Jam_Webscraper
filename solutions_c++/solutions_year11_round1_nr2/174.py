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
#define VP vector<PI>
#define S(t)	scanf("%d",&t)

bool isSame(string& s,string& ss,char& ch){
	int len=s.size();
	F(i,len){
		if(s[i]!='.' && s[i]!=ss[i])	return false;
		if(s[i]=='.' && ss[i]==ch)		return false;
	}
	return true;
}

int main(){
	int t;
	cin>>t;
	FF(kase,1,t+1){
		cout<<"Case #"<<kase<<": ";
		int n,m;
		cin>>n>>m;
		vector<string> D(n);
		F(i,n)	cin>>D[i];
		vector<string> list(m);
		F(i,m)	cin>>list[i];
		F(i,m){
			string ans="";
			string slist = list[i];
			int sLen = slist.size();
			int mxPoint = -1;
			F(j,n){
				int point = 0;
				string s = D[j];
				int len=s.size();
				vector<string> vString;
				F(k,n)	if(D[k].size()==len)	vString.PB(D[k]);
				int k=0;
				string temp = string(len,'.');
				while(vString.size()!=1){
					char ch = slist[k++];
					bool ok=true;
					F(l,vString.size()){
						if(vString[l].find(ch) != string::npos){
							ok=false;
							break;
						}
					}
					if(ok)	continue;
					if(s.find(ch)==string::npos){
						point++;
						for(int l=0;l<vString.size();){
							if(vString[l].find(ch) != string::npos){
								vString.erase(vString.begin()+l);
							}
							else	l++;
						}
					}
					else{
						F(l,len)	if(s[l]==ch)	temp[l]=ch;
						for(int l=0;l<vString.size();){
							if(isSame(temp,vString[l],ch))	l++;
							else									vString.erase(vString.begin()+l);
						}
					}
				}
				if(mxPoint < point){
					mxPoint = point;
					ans = s;
				}
			}
			if(i)	cout<<" ";
			cout<<ans;
		}
		cout<<endl;
	}
	return 0;
}
