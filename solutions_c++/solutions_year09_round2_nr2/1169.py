#include <iostream>
#include <cstdio>
#include <cctype>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <ctime>
#include <cassert>
#include <string.h>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define GI64 ({int64 t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define GS ({string s;cin>>s;s;})
#define f(i,a,b) for(int i=a;i<b;i++)
#define rf(i,a,b) for(int i=a;i>b;i--)
#define SET(x,a) memset(x,a,sizeof(x));
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define tr(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define pb push_back
#define sz(a) (int)(a.size())
#define INF (int)1e9
#define EPS (double)1e-9

typedef long long int64;
typedef pair< int,int > ii;
typedef vector< ii > vii;
typedef vector < vii > vvii;
typedef vector< int > vi;
typedef vector< vi > vvi;

#define is istringstream
#define os ostringstream

//char ch;

string bring(int from,int to,string str){
	if(str[from]<=str[to])return str;
	swap(str[from],str[to]);
	string tmp="",sr="";	
	f(j,0,to+1)tmp+=str[j];
	f(j,to+1,sz(str))sr+=str[j];
	sort(all(sr));
	tmp+=sr;
	return tmp;
}

string minstr(string a,string b){
	if(a=="")return b;
	if(b=="")return a;
	if(a<b)return a;
	return b;
}

int main(){
	int t=GI;
	f(i,1,t+1){
		string s=GS;
		string ans="";
		for(int to=0;to<sz(s)-1;to++)
			for(int from=to+1;from<sz(s);from++){
				string tmp=bring(from,to,s);
				if(tmp!=s)ans=minstr(ans,tmp);
			}
		if(ans==""){
			sort(all(s));
			string tmp1="",tmp2="",tmp3="";
			tmp2+='0';
			int ct=0;
			while(s[ct]=='0'){tmp2+='0';ct++;}
			tmp1+=s[ct];ct++;
			f(j,ct,sz(s))tmp3+=s[j];
			ans+=tmp1+tmp2+tmp3;
		}	
		cout<<"Case #"<<i<<": "<<ans<<endl;	
		}
	return 0;	
}
