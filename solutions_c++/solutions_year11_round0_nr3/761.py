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
void solve (long long t);
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
int n;
int c[2000];
void solve (int t)
{
	cin>>n;
	int mn=1<<30;
	int xor=0;
	int s=0;
	for ( int i=0; i<n; i++ )
	{
		cin>>c[i];
		s+=c[i];
		mn=min (mn, c[i]);
		xor=xor^c[i];
	}
	if ( xor!=0 )
	{
		cout<<"Case #"<<t<<": NO"<<endl;
		return;
	}
	cout<<"Case #"<<t<<": "<<s-mn<<endl;
}