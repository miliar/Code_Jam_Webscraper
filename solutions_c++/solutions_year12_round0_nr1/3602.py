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

using namespace std;

#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define mkp make_pair
typedef long long ll;

int main(){
	char m[27]= "yhesocvxduiglbkrztnwjpfmaq";
	int T;
	cin>>T;
	cin.ignore();
	REP(x,T){
		string s;		
		getline(cin,s);
		cout<<"Case #"<<x+1<<": ";
		REP(i,s.sz){
			if(s[i] == ' ') 
				cout<<" ";
			else 
				cout<<m[s[i]-'a'];
			}
		cout<<endl;
		}
	return 0;
	}