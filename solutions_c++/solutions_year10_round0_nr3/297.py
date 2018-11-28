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

typedef long long ll;

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

ll v[1100];
int nxt[1100];
ll add[1100];

int main()
{
	int t;
	cin >> t;
	for(int c=0; c<t; ++c)
	{
		ll r,k,n,s=0;
		cin >> r >> k >> n;
		
		RP(i,0,n) cin >> v[i];
		RP(i,0,n) s+=v[i];
		
		RP(i,0,n)
		{
			ll pv=k;
			/*
			add[i]=(pv/s)*s;
			pv-=(pv/s)*s;*/
			add[i]=0;
			
			int j;
			for(j=i; pv>=v[j] && (j!=i || pv==k); j=(j+1)%n){
				pv-=v[j];
				add[i]+=v[j];
			}
			nxt[i]=j;
			//cout << add[i] << " " << nxt[i] << endl;
		}
		
		ll m=0;
		
		int p=0;
		RP(i,0,r)
		{
			m+=add[p];
			p=nxt[p];
		}
		
		cout << "Case #" << c+1 << ": " << m << endl;
	}
}