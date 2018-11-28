#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>
#include <queue>
#include <utility>
#include <functional>
#include <algorithm>
#include <numeric>
#include <bitset>
#include <cmath>
#include <sstream>
#include <complex>
using namespace std;

#define pb push_back
#define mp make_pair
#define pii pair<int,int>

#define fo(i,n) for(int i=0; i < (n) ; ++i)
#define FO(i,a,b) for(int i=a;i<=(b);++i)
#define ALL(v) (v).begin(),(v).end()
#define SORT(v) sort(ALL(v))
#define REV(v) reverse(ALL(v))
#define UNIQ(v) (v).erase(unique(ALL(v)),(v).end())

#define VDebug(x)  {fo(i,(x).size()) cout<<(x)[i]<<" ";cout<<endl;}
#define VVDebug(x) {fo(j,(x).size()) VDebug(x[j])}
				     
typedef istringstream iss;
typedef ostringstream oss;
typedef long long int lint;
typedef complex<double> point;
				     
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef vector<VS> VVS;
				     
const char eof = -123;

void printBits(unsigned int x,int end = 32,int start = 0){for(int i = end-1;i>=start;i--) if(x & (1<<i)) cout<<1<<" "; else cout<<0<<" ";}
int readInt(){	int x;if(scanf("%d",&x) != 1) return eof;return x;}
char readChar() { char c; if(scanf("%c",&c) != 1) return eof; return c;}
lint readLL(){lint x; if(cin>>x) return x; return eof;}
double readDouble(){double f;if(scanf("%lf",&f) == 1)return f;return eof;}

int A[1600], B[1600];
int x = 0, y= 0;
int getTime()
{
	int a, b;
	scanf("%d:%d",&a,&b);
	return a*60 + b; 
}
int getNext(vector<pair<int,int> >& A, vector<pair<int,int> >& B, int a, int b)
{
	int ret = 1599;
	if(a == A.size() && b == B.size()) return ret;
	if(a == A.size()) return B[b].first;
	if(b == B.size()) return A[a].first;
	return min(A[a].first, B[b].first);
}
main()
{
	int cases = readInt();
	int caseNum = 0;
	while(cases--){
		int turnAround = readInt();
		++caseNum;
		vector<pair<int,int> > P, Q;
		int temp = readInt();
		int tempB = readInt();
		while(temp--){
			int f = getTime();
			int g = getTime();
			P.pb(mp(f,g));
		}
		while(tempB--){
			int f = getTime();
			int g = getTime();
			Q.pb(mp(f,g));
		}
		SORT(P);
		SORT(Q);
		fo(i,1600) A[i] = B[i] = 0;
		x = y = 0;
		int a = 0, b = 0;
		while(a < P.size() || b < Q.size()){
			int next = 1599;
			int t=0;
			if(b==Q.size() || a < P.size() && P[a].first <= Q[b].first){
				int t1 = P[a].first, t2 = P[a].second;
				t = t1;
				if(A[t1] > 0){
					A[t1]--;
					B[t2+turnAround]++;
				}
				else{
					x++;
					B[t2+turnAround]++;
				}
				next = getNext(P,Q,a+1,b);
				a++;
			}
			else {
				int t1 = Q[b].first, t2 = Q[b].second;
				t = t1;
				if(B[t1] > 0){
					B[t1]--;
					A[t2+turnAround]++;
				}
				else{
					y++;
					A[t2+turnAround]++;
				}
				next = getNext(P,Q,a,b+1);				
				b++;
			}
			for(int i=t;i<next;i++) A[next] += A[i], B[next] += B[i];
		}
		printf("Case #%d: %d %d\n",caseNum,x,y);
	}
}

