#include <vector>//»Â ‰«„ Œœ«
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include<fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef pair<int,int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;

#define SORT(c) sort((c).begin(),(c).end())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back
//stringvalues = "125 320 512 750 333";
 // istringstream iss (stringvalues,istringstream::in);
//stringstream oss;
//string i2s(ll x){ stringstream ss; ss<<x; return ss.str(); }
// for(set<int>::const_iterator it = S.begin(); it != S.end(); it++) { 
//      r += *it; 
 //} 
vi a;
int f(int x){
	int i=0;
	int r=0;
	while(x){
		if(x%2){
			r^=a[i];
		}
		i++;
		x/=2;
	}
	return r;
}
int main(){
	
	int t,n;
	ofstream fout("a.out");
	ifstream fin("a.in");
	fin>>t;
	REP(c,t){
		fin>>n;
		a.clear();
		int x,sum=0;
		REP(i,n){
			fin>>x;
			sum+=x;
			a.push_back(x);
		}
		int can=0;
		int r=-1;
		FOR(i,1,(1<<n)-1){
			x=i;
			int y=(1<<n)-1-x;
			if(f(x)!=f(y))
				continue;
			can=1;
			int k=0,s=0;

			while(x){
				if(x%2){
					s+=a[k];
				}
				k++;
				x/=2;
			}
			r=max(r,s);
			r=max(r,sum-s);
		}
		if(!can)
		fout<<"Case #"<<c+1<<": NO"<<endl;
		else
			fout<<"Case #"<<c+1<<": "<<r<<endl;
	}
	return 0;
}
		


