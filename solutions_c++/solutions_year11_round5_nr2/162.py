#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>


 
using namespace std;
 
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
 
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

int N, v[11000];
int cv[11000];
int st[11000];
bool check(int f, int t, int len){
//	cout << f << " "<< t << " "<< len << endl;
	if(len==1)return true;
	FOR(i,0,t-f)cv[i]=v[i+f];
	int N = t-f;
//	cout << N << endl;
	FOR(i,0,N)st[i]=0;
	FOR(i,0,N){
//		cout << i << endl;
		int fw = min(st[i],cv[i]);
		st[i+1]+=fw;
		cv[i]-=fw;
		if(cv[i]==0)continue;
		if(i+len>N)return false;
		FOR(j,1,len){
			cv[j+i]-=cv[i];
			if(cv[j+i]<0){
	//			cout << i << " "<< j <<  " "<< cv[i+j] << " "<<cv[i] <<endl;
	//			cout << N << " "<< len << endl;
	//			cout << "return false\n";
				return false;
			}
		}
		st[i+len]+=cv[i];
	}
//	cout << "T" << endl;
	return true;
}
int calc(int N){
	if(N==0)return 0;
	if(N==1)return 1;
	int maxi = N;
	FOR(i,0,11000)if(v[i]){
		int ei = i;
		while(v[ei])ei++;
		int lo = 1, hi = min(maxi,ei-i);
		while(lo!=hi){
			int mid = lo+(hi-lo+1)/2;
			if(check(i,ei,mid))lo = mid;
			else hi = mid-1;
		}
		maxi = hi;
		i = ei;
	}
	return maxi;
}
int main(){
	int TC;
	scanf("%d",&TC);
	FOR(tc,1,TC+1){
		scanf("%d",&N);
		memset(v,0,sizeof(v));
		FOR(i,0,N){
			int c;
			scanf("%d",&c);
			v[c]++;
		}
		int res = calc(N);
		printf("Case #%d: %d\n",tc,res);
	}
	return 0;
}
