#include <iomanip>
#include <ctime>
#include <numeric>
#include <functional>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <climits>
#include <cmath>
#include <cctype>
#include <sstream>
#include <map>
#include <set>
#include <cstdio>
#include <queue>
#define f(i,x,y) for(int i=x;i<y;i++)
#define fd(i,y,x) for(int i=y;i>=x;i--)
#define FOR(it,A) for( typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define impr(A) for( typeof A.begin() chen = A.begin(); chen !=A.end(); chen++ ) cout<<*chen<<" "; cout<<endl
#define ll long long
#define vint vector<int>
#define clr(A,x) memset(A,x,sizeof(A))
#define CLR(v) f(i,0,n) v[i].clear()
#define oo (1<<30)
#define ones(x) __builtin_popcount(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define poner push_back
#define eps (1e-8)
#define cua(x) (x)*(x)
#define MAX 105
#define par pair<int,int>
using namespace std;


int T,w,L,U,G;
int X[MAX],Y[MAX], x[MAX], y[MAX];
int r[2*MAX]; int sz = 0;

int main()
{
	cin >> T;
	f(cases,0,T){
		cin >> w >> L >> U >> G;
		f(i,0,L) cin >> x[i] >> y[i];
		f(i,0,U) cin >> X[i] >> Y[i];
		sz = 0;
		r[sz++] = 0;
		r[sz++] = w;
		f(i,1,L-1) r[sz++] = x[i];
		f(i,1,U-1) r[sz++] = X[i];
		sort(r,r+sz);
		double area = 0;
		f(i,1,U) area += (X[i]-X[i-1]-0.0)*(Y[i]+Y[i-1])/2;
		f(i,1,L) area -= (x[i]-x[i-1]-0.0)*(y[i]+y[i-1])/2;
		area/=G;
//		cout << area << endl;
//		f(i,0,sz) cout << r[i] <<" " ; cout<<endl;
		int veces = 1;
		int t = 1,i = 1,j = 1;
		double ac = 0; double ant;
		printf("Case #%d:\n", cases+1);
		while(veces<G){
			while( ac<veces*area+eps ){
				ant = ac;
				double h0,h1;
				h0 = y[i-1] + (y[i]-y[i-1]+0.0)/(x[i]-x[i-1]) * (r[t-1]-x[i-1]);
				h1 = y[i-1] + (y[i]-y[i-1]+0.0)/(x[i]-x[i-1]) * (r[t]-x[i-1]);
				ac -= (h0+h1)/2 * (r[t]-r[t-1]);
				h0 = Y[j-1] + (Y[j]-Y[j-1]+0.0)/(X[j]-X[j-1]) * (r[t-1]-X[j-1]);
				h1 = Y[j-1] + (Y[j]-Y[j-1]+0.0)/(X[j]-X[j-1]) * (r[t]-X[j-1]);
				ac += (h0+h1)/2 * (r[t]-r[t-1]);
				if( x[i]==r[t] ) i++;
				if( X[j]==r[t] ) j++;
				t++;
//				cout<<ac<<" " <<area<<endl;
//				cout << i<<" " <<j << endl;
   		}
//   		cout << i << " " <<j << endl;
//   		cout << x[i] << "  " << X[j]<< " " <<r[t]<<endl;
			if( x[i-1]==r[t-1] ) i--;
			if( X[j-1]==r[t-1] ) j--;
			t--;
			double a = veces*area-ant;
			double lo = r[t-1], hi = r[t];
//			cout <<i<<" " << j << endl;
//			cout << x[i] << "  " << X[j]<< endl;
//			cout <<a<<" " << lo <<"  "  << hi << endl;
			while( hi-lo>eps ){
				double me = (lo+hi)/2;
				double ame = 0;
				ame += (me-r[t-1]) * (Y[j-1] + (Y[j]-Y[j-1]+0.0)/(X[j]-X[j-1])*((me+r[t-1])/2 - X[j-1]) );
//				cout<<ame<<" ";
				ame -= (me-r[t-1]) * (y[i-1] + (y[i]-y[i-1]+0.0)/(x[i]-x[i-1])*((me+r[t-1])/2 - x[i-1]) );
//				cout<<ame<<" ";
//				cout << me << " " <<ame<<endl;
				if( ame<a ) lo = me;
				else hi = me;
			}
			printf("%.8f\n",hi);
			ac = ant;
			veces++;
		}
	}
}
