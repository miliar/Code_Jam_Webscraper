#include <vector>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <cctype>
#include <cstring>
#include <queue>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define FOR(i,a,b) for( int i=(a); i<(b); ++i)
#define FORD(i,a,b) for( int i=(a); i>(b); --i)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) (int)(X).size()
#define FORE(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end();++it)

int dt[64];
int go[64];
bool chk[64];
int n;

int main()
{
	int tn;

	cin>>tn;
	FOR(qq,1,tn+1) {
		cin>>n;
		REP(i,n) {
			string str;
			cin>>str;
			dt[i]=0;
			FORD(j,n-1,-1) if (str[j]=='1') {
				dt[i]=j+1;
				break;
			}
//			cout<<dt[i]<<" ";
		}
//		cout<<endl;

		REP(i,n) chk[i]=false;
		FORD(i,n,0) {
			FORD(j,n-1,-1) if (!chk[j]) {
				chk[j]=true;
				VI ka;
				REP(k,n) if (!chk[k])
					ka.PB(dt[k]);
				sort(ALL(ka));

				bool possib=true;
				REP(k,i-1) if (ka[k]>k+1) {
					possib=false;
					break;
				}

				if (!possib) {
					chk[j]=false;
					continue;
				}
				
				go[j]=i-1;
				break;
			}
		}

	//	REP(i,n) cout<<go[i]<<" "; cout<<endl;
		
		int dp=0;
		FORD(i,n-1,0) {
			REP(j,n) if (go[j]==i) {
				while(j<i) {
					swap(go[j],go[j+1]);
					j++;
					dp++;
				}
			}
		}

		printf("Case #%d: %d\n",qq,dp);
	}

	return 0;
}
