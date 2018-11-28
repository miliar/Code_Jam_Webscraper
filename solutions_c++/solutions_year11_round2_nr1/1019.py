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
#define ll long long
#define vint vector<int>
#define clr(A,x) memset(A,x,sizeof(A))
#define CLR(v) f(i,0,n) v[i].clear()
#define oo (1<<30)
#define ones(x) __builtin_popcount(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define poner push_back
#define eps (1e-9)
using namespace std;

int T;
string A[100];
vint adj[100];

int main()
{
	cin >> T;
	f(cases,0,T){
		int n; cin >> n;
		f(i,0,100) adj[i].clear();
		f(i,0,n) cin >> A[i];
		f(i,0,n)f(j,0,n)if( A[i][j]!='.' ) adj[i].poner(j);
		
		double wp[100],owp[100],oowp[100], rpi[100];
		f(i,0,n){
			double x = 0;
			f(k,0,adj[i].size())if( A[i][ adj[i][k] ]=='1' ) x++;
			wp[i] = x/adj[i].size();
		}
		f(i,0,n){
			double x = 0;
			f(k,0,adj[i].size()){
				int j = adj[i][k];
				double y = 0;
				f(kk,0,adj[j].size()) if( adj[j][kk]!=i && A[j][adj[j][kk]]=='1' ) y++;
				x += y/(adj[j].size()-1);
			}
			owp[i] = x/adj[i].size();
		}
		f(i,0,n){
			double x = 0;
			f(k,0,adj[i].size()) x += owp[ adj[i][k] ];
			oowp[i] = x/adj[i].size();
		}
		f(i,0,n){
			double x = 0;
			x += owp[i]; x+= owp[i];
			x += wp[i];  x+= oowp[i];
			rpi[i] = x/4;
		}
//		f(i,0,n) cout<<wp[i]<<" "; cout << endl;
//		f(i,0,n) cout<<owp[i]<<" "; cout << endl;
//		f(i,0,n) cout<<oowp[i]<<" "; cout << endl;
		printf( "Case #%d:\n", cases+1 );
		f(i,0,n) printf( "%.10f\n", rpi[i] );
	}
}
