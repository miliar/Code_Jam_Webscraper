#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cmath>
#include <set>
#include <cassert>
#include <cstdio>
#include <queue>
using namespace std;
#define LET(x,a) __typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) FOR(it,(v).begin(),(v).end())
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define GI ({int t;scanf("%d",&t);t;})
#define GII ({LL t;scanf("%Ld",&t);t;})
#define INF (int)1e8
#define MAX 55
#define mkp make_pair
typedef long long LL;
typedef double D;
#define sz size()
#define bset(i,j) (((1)<<(j))&(i))
int s, q;
vector <int> qr;
int main()
{
	int runs=GI, caseno=1;
	while(runs--) {
		s=GI;
		qr.clear();
		vector<string> ss;
		string line;
		cin.ignore();
		REP(i,s) {
			getline(cin,line);
			ss.pb(line);
		}
		q=GI;
		int ans=-1;
		if(q) {
			cin.ignore();
			REP(i,q) {
				getline(cin,line);
				REP(j,ss.sz) if(line.compare(ss[j]) == 0) {
					qr.pb(j);
					break;
				}
			}
			int curser=qr[0];
			REP(i,q) if(qr[i] == curser) {
				int ttime[s], max=0;
				REP(j,s) {
					ttime[j]=2*q;
					FOR(k,i,q) if(qr[k] == j) 
					ttime[j]<?=k;
				}
				REP(j,s) {
					if(ttime[j] > max) max=ttime[j], curser=j;		
				}
				ans++;
			}			
		}
		else ans=0;
		printf("Case #%d: %d\n", caseno++, ans);	
	}
}
	
	
	
	
	
	
	
	
	
