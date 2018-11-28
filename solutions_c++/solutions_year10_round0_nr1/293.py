#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <utility>
#include <sstream>
#include <cstring>

using namespace std;

typedef unsigned long long ll;

#define RP(i,s,e) for(int i=s;i<e;i++) 
#define R(i,x) RP(i,0,(x).size())
#define RP3(x,y,z) RP(i,0,x) RP(j,0,y) RP(k,0,z)
#define RI(i,x) for(typeof((x).begin()) i=(x).begin();i!=(x).end();++i)
#define pB push_back
#define P(a) cout << #a << " : " << a << endl;
#define M make_pair

template <class T, class R>
ostream & operator<<(ostream & o, pair<T,R> a){return o<<a._1<<"," << a._2;}

template <class T>
ostream & operator<<(ostream & o, vector<T> a){R(i,a) o<<a[i]<<","; return o;}

int main()
{
	int t,cs=0;
	cin >> t;
	for(int i=0; i<t; ++i)
	{
		int n,k;
		cin >> n >> k;
		cout << "Case #"<< i+1 << ": ";
		if((k&((1<<n)-1)) == ((1<<n)-1)) cout << "ON" << endl;
		else cout << "OFF" << endl;
	}
}
