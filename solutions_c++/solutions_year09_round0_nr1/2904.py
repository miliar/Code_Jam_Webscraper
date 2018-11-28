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
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define REP(i,n) for(i=0;i<n;i++)
#define FOR(i,A,n) for(i=A;i<n;i++)
#define sz(c) (signed int) c.size()
#define pb(c) push_back(c)
#define INF (int) 1e9
#define all(c) c.begin(),c.end()
typedef long long LL;

using namespace std;

map<pair<char,int>,string >M;

bool Check(char a,int i,vector<string>v,int k,int l);

int main() 
{
	int i,j,k;
	int l,d,n;
	cin>>l>>d>>n;
	string s,t;
	pair<char,int>P;
	vector<string>dict;
	REP(i,d) {
		cin>>s;
		dict.pb(s);
	}
	
	REP(i,n) {
		cin>>s;
		vector<string>v;
		int br=0;
		t="";
		for(j=0;j<sz(s);j++) {
			if(br==0 && s[j]!='(') {
				t.pb(s[j]);
				v.pb(t);
				t="";
			}
			else {
				if(s[j]=='(') {
				br=1;
				continue;
				}
				if(s[j]==')' && br) {
					v.pb(t);
					br=0;
					t="";
				}
				if(br==1) {
					t.pb(s[j]);
				}
				
			}
		}
		/*REP(j,l) {
			s=v[j];
			cout<<s<<endl;
		}
		cout<<endl;
		*/
		
		int cnt=0;
		int flag=1;
		for(k=0;k<sz(dict);k++) {
			t=dict[k];
			flag=1;
			for(j=0;j<sz(v);j++) {
				s=v[j];
				if(s.find(t[j],0)==string::npos) {
					flag=0;
				}
			}
			if(flag) {
				cnt++;
			}
		}	
		cout<<"Case #"<<i+1<<": "<<cnt<<endl;

	}


	return 0;
}

bool Check(char a,int i,vector<string>v,int k,int l) {
	if(k==l)
	return true;
	else {
		int j;
		pair<char,int>P;
		P.first=a;
		P.second=i;
		string s=v[k];
		string t=M[P];
		cout<<t<<"\t"<<s<<endl;
		if(sz(t)>0) {
		for(j=0;j<sz(t);j++) {
			if(s.find(t[j],0)!=string::npos) {
			//cout<<"found match\n";
			return Check(t[j],i+1,v,k+1,l);
			}
		}
		return false;
		}
		else return false;
	}
}
