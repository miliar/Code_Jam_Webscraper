#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <sstream>
#include <algorithm>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cmath>

using namespace std;

#define RP(i,j,k) for(int i=j; i<k; ++i)
#define R(i,x) RP(i,0,(x).size())
#define RP3(x,y,z) RP(i,0,x) RP(j,0,y) RP(k,0,z)
#define RI(i,x) for(typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define pB push_back
#define P(a) cout << #a << " : " << a << endl;
#define M make_pair

template <class T, class R>
ostream & operator<<(ostream & o, pair<T,R> a){return o<<a._1<<"," << a._2;}

template <class T>
ostream & operator<<(ostream & o, vector<T> a){R(i,a) o<<a[i]<<","; return o;}

typedef vector<string> vs;
typedef vector<int> vi;
typedef long long ll;

char f[100][100];

int main()
{
	int C;
	cin >> C;
	
	for(int cs=1; cs<=C; ++cs)
	{
		int h, w;
		cin >> h >> w;
		
		RP3(h,w,1) cin >> f[i][j];
		
		bool ok=true;
		
		RP3(h,w,1){
			if(f[i][j]=='#'){
				
				if(i==h-1 || j==w-1) ok=false;
				else if(!(f[i+1][j]=='#' && f[i+1][j+1]=='#' && f[i][j+1]=='#')) ok=false;
				else{
					f[i][j]='/';
					f[i+1][j]='\\'; 
					f[i+1][j+1]='/';
					f[i][j+1]='\\';
				}
			}
		}
		
		cout << "Case #" << cs << ":" << endl;
		if(ok){
			RP(i,0,h){
				RP(j,0,w)
					cout << f[i][j];
				cout << endl;
			}
		}else
			cout << "Impossible" << endl;
	}
	
	return 0;
}