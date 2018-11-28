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
	//cin >> C;
	int L,D,N;
	cin >> L >> D >> N;
	
	vector<string> w(D,"");
		
	RP(i,0,D) cin >> w[i];
	
	
	for(int cs=1; cs<=N; ++cs)
	{
		string p;
		cin >> p;
		
		ll m=0;
		
		RP(i,0,D)
		{
			int y=1,k=0;
			
			R(j,w[i])
			{
				int f=0;
				if(p[k]=='(')
				{
					while(p[++k]!=')') {
						if(w[i][j]==p[k]) f=1;
					}
				}
				else
				if(w[i][j]==p[k]) f=1;
				
				if(!f) y=0;
				//y<?=f;
				++k;
			}
			
			m+=y;
		}
		
		cout << "Case #" << cs << ": " << m;
		
		cout << endl;
	}
	
	return 0;
}