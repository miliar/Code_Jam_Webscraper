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

int n, m;
char input[1000][1000];

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int tc;
	cin>>tc;
	long long res=-1;

	forn(q,tc){
		cin >> n;
		cin >> m;
		forn(i,n) {
			char temp;
			scanf("%c", &temp);
			forn(j,m) 
				{scanf("%c", &input[j][i]);
			}
		}

		int wrong = 0;
		forn(i,n) {
			forn(j,m) {
				if (input[j][i] == '#') {
					if (i==n-1 || j==m-1) {
						wrong=1;
						break;
					} 
					if (input[j+1][i] != '#' || 
						input[j+1][i+1] != '#' ||
						input[j][i+1]!= '#') {
						wrong=1;
						break;
					}
					input[j][i]='/';					
					input[j+1][i]='\\';					
					input[j][i+1]='\\';					
					input[j+1][i+1]='/';
				}
			}
			if (wrong) break;
		}
		if (wrong) {
			cout<<"Case #"<<q+1<<": "<<endl<<"Impossible"<<endl;
		} else {
			cout<<"Case #"<<q+1<<":";
			forn(i,n) {
				cout<<endl;
				forn(j,m) 
					{
						printf("%c", input[j][i]);
				}
			}
			cout<<endl;
		}
	}

	return 0;
}
