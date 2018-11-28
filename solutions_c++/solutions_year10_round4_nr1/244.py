#pragma comment(linker,"/STACK:256000000")
//#pragma comment(linker,"/STACK:536870912")
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
#include <stack>
#include <cstring>
#include <ctime>
#include <memory.h>
using namespace std;

#define lng long long
#define PB push_back
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
#define forn1(i,n) for(i=0;i<n;++i)
#define forv(i,v) for(int i=0;i<v.size();++i)
#define forvr(i,v) for(int i=v.size()-1;i>=0;--i)
#define fors(i,s) for(int i=0;i<s.length();++i)
#define EPS 1e-12
#define eps EPS
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)
#define iinf 1000000000
#define linf 100000000000000000LL
#define maxll ((1LL<<62)-1+(1LL<<62))
#define dinf 10000000000000000000000.0
#define SQ(a) ((a)*(a))
#define SWAP(t,a,b) {t ____tmpasdasdasd=(a);(a)=(b);(b)=____tmpasdasdasd;}
#define left _left
#define y1 asdy1
#define y2 asdy2
#define y0 asdy0
#define abs(a) ((a)<0?-(a):(a))
#define mat _mat
#define ALL(a) (a).begin(),(a).end()
#ifdef __TRATATA__
//#include "my.h"
#endif

int ar[100][100];

int main(){
#ifdef __TRATATA__
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

	int tc;
	cin>>tc;
	forn(q,tc){
		int n;
		cin>>n;
		forn(i,n*2-1){
			forn(j,min(i+1,n*2-1-i)){
				if(i<n)
					cin>>ar[i-j][j];
				else
					cin>>ar[n-1-j][i+j-n+1];
			}
		}
		int res=iinf;
		for(int a=-n-10;a<n*2+10;++a){
			for(int b=-n-10;b<n*2+10;++b){
				int size=2*max(max(n-a-1,a),max(n-b-1,b))+1;
				if(size>=res)
					continue;
				bool good=true;
				forn(i,n){
					forn(j,n){
						int t1,t2;

						t1=a-b+j;
						t2=b-a+i;
						if(t1>=0&&t1<n&&t2>=0&&t2<n&&ar[t1][t2]!=ar[i][j]){
							good=false;
							break;
						}

						t1=a+b-j;
						t2=a+b-i;
						if(t1>=0&&t1<n&&t2>=0&&t2<n&&ar[t1][t2]!=ar[i][j]){
							good=false;
							break;
						}
					}
					if(!good)
						break;
				}
				if(good)
					res=size;
			}
		}
		for(int a=-n-10;a<n*2+10;++a){
			for(int b=-n-10;b<n*2+10;++b){
				int size=2*max(max(n-a-1,a+1),max(n-b-1,b+1));
				if(size>=res)
					continue;
				bool good=true;
				forn(i,n){
					forn(j,n){
						int t1,t2;

						t1=a-b+j;
						t2=b-a+i;
						if(t1>=0&&t1<n&&t2>=0&&t2<n&&ar[t1][t2]!=ar[i][j]){
							good=false;
							break;
						}

						t1=a+b-j+1;
						t2=a+b-i+1;
						if(t1>=0&&t1<n&&t2>=0&&t2<n&&ar[t1][t2]!=ar[i][j]){
							good=false;
							break;
						}
					}
					if(!good)
						break;
				}
				if(good)
					res=size;
			}
		}
		cout<<"Case #"<<q+1<<": "<<SQ(res)-SQ(n)<<endl;
	}

    return 0;
}