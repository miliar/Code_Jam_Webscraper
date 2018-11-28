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

int f[200];

int main()
{
	int C;
	cin >> C;
	
	for(int cs=1; cs<=C; ++cs)
	{
		int n,l,h;
		cin >> n >> l >> h;
		
		for(int i=0; i<n; ++i)
			cin >> f[i];
		
		cout << "Case #" << cs << ": ";
		
		for(int i=l; i<=h; ++i){
			for(int j=0; j<n; ++j){
				if(!(i%f[j]==0 || f[j]%i==0))
					goto le;
			}
			
			cout << i;
			goto end;
			le:;
		}
			
		cout << "NO";
		end:;
		
		cout << endl;
	}
	
	return 0;
}