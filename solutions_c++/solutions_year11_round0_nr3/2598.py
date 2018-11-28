#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#define FORN(i,n) FOR(i,0,(n))
#define FOR(i,a,n) for(int i=(a);i<(n);i++)
#define sz size()
#define PB push_back
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define PRESENT(container, element) (container.find(element) != container.end())
#define ALL(x) x.begin(), x.end()
#define TR(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define DIST(x1,y1,x2,y2) sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
#define foreach(i, c) for( __typeof( (c).begin() ) i = (c).begin(); i != (c).end(); ++i )


using namespace std;
typedef unsigned long long ull;

bool menor(int A,int B){
	return A>=B;
}



int main(){
	int t,candies,val;

	cin>>t;
	FORN(casos,t){
		vector<int>V;
		cin>>candies;
		
		FORN(ww,candies){
			cin>>val;
			V.PB(val);
		}
		printf("Case #%d: ",casos+1);
		bool mal=false;
		FORN(i,25){
			int g=0;
			FORN(w,V.sz){
				if (V[w]&(1<<i)){
					g++;
			//		cout<<"Bit "<<i<<" de "<<V[w]<<endl; 
				}
			}
			if (g%2)
				mal=true;
		}
				
		if (mal)cout<<"NO"<<endl;
		else{
			sort(ALL(V));
			long long res=0;
			FOR(i,1,V.sz)
				res+=V[i];
			cout<<res<<endl;
		}
		
	}
	

  return 0;
}
