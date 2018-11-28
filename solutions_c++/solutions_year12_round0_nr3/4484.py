#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

#define pb push_back
#define mp make_pair
#define sz size()
#define all(a) (a).begin(),(a).end()
#define rall(a) (a).rbegin(),(a).rend()
#define vint vector<int>
#define forn(i,n) for (int (i)=0; (i)<(n); (i)++)

using namespace std;
const int INF=~(1<<31);
const double EPS=1e-6;
const double PI=3.141592653589793;

int main(){
#ifdef HOME
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
   int n,a,b,q,l,x,y,r=0,k;
   cin>>n;
   forn(t,n) {
	   r=0;
	   cin>>a>>b;
	   q=a;
	   l=10;
	   while (q/=10) l*=10;
	   for (int i=a; i<b; i++) {
		   k=10;
		   set<int>s;
		   while (l/k>1) {
			   x=i%(l/k);
			   y=i/(l/k);
			   q=x*k+y;
			   k*=10;			   
			   if (x/(l/k)>0 && q>i && q<=b && s.count(q)==0 ) {
				   r++;
				   s.insert(q);
				   //cout<<i<<' '<<q<<endl;
			   }
		   }
	   }
	   cout<<"Case #"<<t+1<<": "<<r<<endl;
   }
   return 0;
}