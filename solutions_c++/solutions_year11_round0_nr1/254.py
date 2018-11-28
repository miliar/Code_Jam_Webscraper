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

int main(){ 
#ifdef LocalHost
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	int tc;
	cin>>tc;
	REP(TC,tc){
		printf("Case #%d: ",TC+1);
		int n;
		cin>>n;
		int pos1=1,t1=0;
		int pos2=1,t2=0;
		REP(i,n){
			char c;
			int t;
			scanf(" %c %d",&c,&t);
			if(c=='O'){
				t1 += abs(pos1-t);
				pos1 = t;
				t1 = max(t1,t2) + 1;
			}else{
				
				t2 += abs(pos2-t);
				pos2 = t;
				t2 = max(t1,t2) + 1;
			}
		}
		cout<<max(t1,t2)<<endl;
	}
	return 0;
}