#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <memory.h>
#include <algorithm>
#include <math.h>
#include <queue>
using namespace std;
typedef long long li;
typedef long double ld;
#define mp make_pair
#define pb push_back
typedef pair <long long, long long> pi;
typedef vector <int> vi;
void solve (li t);
int main ()
{
#ifdef _DEBUG
        freopen ("in.txt", "r", stdin);
        freopen ("out.txt", "w", stdout);
#endif
        li t;
		cin>>t;
		li u=t;
        while (t--)
        solve (u-t);
		return 0;
}
#define int li
int gcd (int q, int w)
{
	if (w==0)
		return q;
	if (q<w)
		swap (q, w);
	while(w>0)
	{
		q%=w;
		swap (q, w);
	}
	return q;
}
void solve (int t)
{
	int n, pd, pg;
	int x, y;
	cin>>n>>pd>>pg;
	int z=gcd(pd, 100);
	int f=100/z;
	if ( n<f )
	{
		cout<<"Case #"<<t<<": "<<"Broken"<<endl;
		return;
	}
	int d, g;
	d=f;
	y=(d*pd)/100;
	z=gcd(100, pg);
	f=100/z;
	g=f;
	//cout<<pg<<' '<<pd;
	for ( g=f; g<=10000*f; g++ )
	{
		x=(pg*g)/100-y;
		if ( x>=0 && g-d>=x )
		{
			cout<<"Case #"<<t<<": "<<"Possible"<<endl;
			return;
		}
	}
	cout<<"Case #"<<t<<": "<<"Broken"<<endl;
}