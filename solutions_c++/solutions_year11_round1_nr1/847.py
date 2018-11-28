#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <math.h>
#include <map>
#include <set> 
#include <queue>
#define  rep(i,a,b) for ( int i = a; i<=b; i++ )
const double EPS = 1E-8; 
const double PI  = 3.14159265; 
const int dx[4]={0,1,0,-1};
const int dy[4]={1,0,-1,0};

using namespace std; 

typedef  vector<int> VI; 
typedef  vector<VI>  VV; 
typedef  string      SS; 
typedef  vector<SS> VS; 
typedef  long long   LL;
typedef  map<int,int>MII;
typedef  priority_queue<int> maxpq; 
typedef  priority_queue<int,VI, greater<int>> minpq;
LL  MAX_N=1000000000000000; 

void main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T; 
	cin >> T; 
	LL ans; 
	LL N, PD, PG; 
	LL x2[21], x5[21]; 
	x2[0]=1;
	x5[0]=1;
	rep(i,1,20){
		x2[i]=x2[i-1]*2;
		x5[i]=x5[i-1]*5; 
	}
	LL x[1000]; 
	LL top = -1; 
	rep(i,0,20){
		rep(j,0,20){
			top++;
			x[top]=x2[i]*x5[j]; 
			if (x[top]>MAX_N) {break; }
		}
	}
	sort(x,x+top); 

	rep(t,1,T){
		cin >> N >> PD >> PG; 
		LL D,G; 
		bool found; 
		found = false;
		LL TD, TG; 
		rep(i,0,top) {
			if (x[i]>N) break; 
			rep(j,i,top) {
				D=x[i];
				G=x[j]; 
				if (((G*PG)%100==0)&&((D*PD)%100==0)) {
					TD=D*PD/100;
					TG=G*PG/100; 
					if (TG>=TD&&(G-TG>=D-TD)) {
						found = true; 
						break; 
					}
				}
			if (found) break; 
			}
		}
		if (found)	cout << "Case #"<<t<<": Possible" << endl; 
		else cout << "Case #"<<t<<": Broken" << endl;
	}

}