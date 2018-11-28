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

int main()
{
	int C;
	cin >> C;
	for(int cs=1; cs<=C; ++cs)
	{
		int I;
		cin >> I;
		
		char r; int b;
		
		int op=1,om=0,bp=1,bm=0,t=0;
		
		RP(i,0,I){
			cin >> r >> b;
			
			if(r=='O'){
				
				int fm=(t-om);
				int dist=abs(b-op)+1;
				int pt=t+dist-fm;
				if(pt<t+1) pt=t+1;
				t=pt;
				om=t;
				op=b;
			}else{
				
				int fm=(t-bm);
				int dist=abs(b-bp)+1;
				int pt=t+dist-fm;
				if(pt<t+1) pt=t+1;
				t=pt;
				bm=t;
				bp=b;
			}
			
		}
		
		cout << "Case #" << cs << ": " << t;
		
		cout << endl;
	}
	
	return 0;
}