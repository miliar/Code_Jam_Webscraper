#pragma comment(linker, "/STACK:65777216")

#include <algorithm>
#include <iostream>
#include <string>
#include<sstream>
#include<string.h>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include<stack>
#include <set>
#include <map>
#include<ctime>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef unsigned long long ull;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back

int a[33][33];
bool b[33][33];

int main(){ 
#ifdef LocalHost
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	int tc;
	cin>>tc;
	REP(TC,tc){
		CL(a,-1);
		int c;
		cin>>c;
		REP(i,c){
			string s;
			cin>>s;
			a[s[0]-'A'][s[1]-'A']=a[s[1]-'A'][s[0]-'A']=s[2]-'A';
		}
		cin>>c;
		CL(b,0);
		REP(i,c){
			string s;
			cin>>s;
			b[s[0]-'A'][s[1]-'A']=b[s[1]-'A'][s[0]-'A']=true;
		}
		int n;
		cin>>n;
		string s;
		cin>>s;
		vector<char> v;
		REP(i,n){
			char C = s[i];
			if(v.size()){
				int t1 = v.back()-'A';
				int t2 = C-'A';
				if(a[t1][t2]!=-1) v.pop_back(),v.pb(char('A'+a[t1][t2]));
				else{
					bool cc = 0;
					REP(j,v.size()) if(b[v[j]-'A'][t2])cc=1;
					if(cc) v.clear();
					else v.pb(C);
				}
			}else v.pb(C);
		}
		printf("Case #%d: [",TC+1);
		REP(i,v.size()){
			if(i) printf(", ");
			printf("%c",v[i]);
		}
		puts("]");
	}
	return 0;
}