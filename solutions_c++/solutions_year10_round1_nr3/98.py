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
typedef long double ld;

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


ld sv2(ld A, ld B)
{
	if(A<B) return sv2(B,A);
	if(A>=B*2) return 1;
	if(A<= B*3/2) return 0;
	return 1-sv2(B,A-B);
}

ld fd()
{
	ld s=1, e=2,m;
	for(int i=0; i<2000; ++i)
	{
		m=(e+s)/2;
		if(sv2(m,1)) e=m;
		else s=m;
	}
	return s;
}

ld magic;

ll sv(ll A, ll B)
{
	if(A<B) return sv(B,A);
	if(A>=B*2) return 1;
	if(A<= B*3/2) return 0;
	return 1-sv(B,A-B);
}

//first win
ll fd2(ll B)
{
	ll s=B+1, e=B*2,m;
	while(e-s>1)
	{
		m=(e+s)/2;
		if(sv(m,B)) e=m;
		else s=m;
	}
	if(sv(s,B)) return s;
	return e;
}

int main()
{
	magic=fd();
	//cout << magic << endl;
	int C;
	cin >> C;
	for(int cs=0; cs<C; ++cs)
	{
		ll a1,a2,b1,b2;
		cin >> a1 >> a2 >> b1 >> b2;
		
		ll ct=0;
		
		for(ll i=a1; i<=a2; ++i)
		{
			ll b=i;
			
			ll c1=b1, c2=b2;
			if(c1<b) c1=b;
			
			ll c3=b*magic;
			
			if(c1-1>c3) c3=c1-1;
			
			ll area=c2-c3;
			if(area<0) area=0;
			ct+=area;
			//cout <<b << " " << c1 << " " << c2 << " " << c3 << " a  " << area << endl;
		}
		
		for(ll i=b1; i<=b2; ++i)
		{
			ll b=i;
			
			ll c1=a1, c2=a2;
			if(c1<b) c1=b;
			
			ll c3=b*magic;
			if(c1-1>c3) c3=c1-1;
			
			ll area=c2-c3;
			if(area<0) area=0;
			ct+=area;
			//cout <<b << " " << c1 << " " << c2 << " " << c3 << " a  " << area << endl;
		}
		
		
		
		cout << "Case #" << cs+1 << ": ";
		cout << ct;
		cout << endl;
	}
}


