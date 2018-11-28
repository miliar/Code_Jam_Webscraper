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
int main()
{
	int i,j,k;
	int t;
	cin>>t;
	int test=1;
	while(t--) {
		map<char,int>M;
		string s;
		cin>>s;
		int cnt=1;
		M[s[0]]=1;
		char c=s[0];
		cout<<"Case #"<<test<<": ";
		for(i=1;i<sz(s);i++) {
			if(s[i]!=c) 
			break;
		}
		if(i<sz(s)) {
			M[s[i]]=-1;
			cnt=2;
			for(i++;i<sz(s);i++) {
				if(M[s[i]])
				{}
				else {
					M[s[i]]=cnt;
					cnt++;
				}
			}
		}
		else {
			cnt=2;
		}
		//cout<<endl<<endl<<endl;
		LL  num=0;
		//cout<<cnt<<endl;		
		for(i=0;i<sz(s);i++) {
			if(M[s[i]]==-1) 
			{
				M[s[i]]=0;
			}
			num=num*cnt+M[s[i]];
		}
		cout<<num<<endl;
		test++;
	}
	return 0;
}
