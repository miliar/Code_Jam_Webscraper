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
#define par pair<int,int>
using namespace std;

int A[101], B[101];
par instruccion[101];
int sza = 0, szb = 0;
int posa = 1, posb = 1;
int t = 0;

int main()
{
	int pa = 0, pb = 0;
	int T; cin >> T;
	f(cases,0,T){
		sza = szb = 0;
		posa = posb = 1;
		t = 0;
		int ordenes; cin >> ordenes;
		char c; int x;
		f(i,0,ordenes){
			cin >> c >> x;
			if( c=='O' ) A[sza++] = x;
			else B[szb++] = x;
			instruccion[i] = par(x,c=='B');
		}
//		f(i,0,sza)cout<<A[i]<<" "; cout<<endl;
//		f(i,0,szb)cout<<B[i]<<" "; cout<<endl;
		int a = 0, b = 0;
		f(I,0,ordenes){
			par p = instruccion[I];
			if( p.second==0 ){
				int mov = abs(posa-A[a]) + 1;
				t += mov;
				f(i,0,mov ){
					if( posa < A[a] ) posa++;
					if( posa > A[a] ) posa--;
					if( posb < B[b] ) posb++;
					if( posb > B[b] ) posb--;
				}
				a++;
			}else{
				int mov = abs(posb-B[b]) + 1;
				t += mov;
				f(i,0,mov){
               if( posa < A[a] ) posa++;
					if( posa > A[a] ) posa--;
					if( posb < B[b] ) posb++;
					if( posb > B[b] ) posb--;
				}
				b++;
			}
		}
		printf("Case #%d: %d\n", cases+1,t );
	}
}
