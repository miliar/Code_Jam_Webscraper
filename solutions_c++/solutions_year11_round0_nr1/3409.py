#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cmath>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <queue>
#include <cstring>
#include <ctime>
using namespace std;

#define pii pair<int,int>
#define MPII make_pair<int,int>
#define PLL pair<lng,lng>
#define MPLL make_pair<lng,lng>
#define PI 3.1415926535897932384626433832795
#define DEG2RAD (PI/180.0)
#define RAD2DEG (1.0/DEG2RAD)
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>
#define VD vector<double>
#define forn(i,n) for(int i=0;i<n;++i)
#define fornr(i,n) for(int i=n-1;i>=0;--i)
#define forn1(i,n) for(int i=0;i<n+1;++i)
#define forv(i,v) for(int i=0;i<v.size();++i)
#define forvr(i,v) for(int i=v.size()-1;i>=0;--i)
#define fors(i,s) for(int i=0;i<s.length();++i)
#define EPS 1e-12
#define eps EPS
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)
#define maxll ((1LL<<62)-1+(1LL<<62))
#define SQ(a) ((a)*(a))
#define SWAP(t,a,b) {t ____tmpasdasdasd=(a);(a)=(b);(b)=____tmpasdasdasd;}
#define abs(a) ((a)<0?-(a):(a))
#define ALL(a) (a).begin(),(a).end()


int c;
int b[100];
int o[100];

char type;

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int tc;
	cin>>tc;
	long long res;

	forn(q,tc){
		res=0;
		cin >> c;
		memset(b,0,100);
		memset(o,0,100);
		int temp;
		forn(i,c) {
			scanf(" %c %d", &type, &temp);
			if (type=='B') {b[i]=temp;} else {o[i]=temp;} 
		}
	
		int curb=1;
		int curo=1;
		forn(i,c) {
			if (b[i]>0) {
				int turn=abs(b[i]-curb)+1;
				res+=turn;
				curb=b[i];
				int j=i+1;
				for(j=i+1;j<c;j++) if (o[j]>0) break;
				if (j<c) {
					if (abs(curo-o[j])>turn) {
						if (curo>o[j]) {
							curo = curo-turn;
						} else {
							curo = curo+turn;
						}						
					} else {
						curo=o[j];
					}
				}
			} else {
				int turn=abs(o[i]-curo)+1;
				res+=turn;
				curo=o[i];
				int j=i+1;
				for(j=i+1;j<c;j++) if (b[j]>0) break;
				if (j<c) {
					if (abs(curb-b[j])>turn) {
						if (curb>b[j]) {
							curb = curb-turn;
						} else {
							curb = curb+turn;
						}						
					} else {
						curb=b[j];
					}
				}
			}
		}

		cout<<"Case #"<<q+1<<": "<<res<<endl;		
	}

	return 0;
}
