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
void solve (int t);
int main ()
{
#ifdef _DEBUG
        freopen ("in.txt", "r", stdin);
        freopen ("out.txt", "w", stdout);
#endif
        int t;
		cin>>t;
		int u=t;
        while (t--)
        solve (u-t);
}
//#define int li
void solve (int t)
{
	int n;
	cin>>n;
	pair <int, char> pos[200];
	vi orange, blue;
	for ( int i=0; i<n; i++ )
	{
		cin>>pos[i].second>>pos[i].first;
		if ( pos[i].second =='O')
			orange.pb(pos[i].first);
		else 
			blue.pb (pos[i].first);
	}
	int timer=0;
	int or=0, bl=0, comp=0;
	int nowor=1, nowbl=1;
	while ( comp<n )
	{
		if ( or<orange.size() )
		{
		if ( orange[or]==nowor )
		{
			if ( pos[comp].second=='O' )
			{
				or++;
				comp++;
				if ( comp<n && pos[comp].first==nowbl && pos[comp].second=='B' )
				{
					timer++;
					continue;
				}
			}
		}
		else 
		if ( orange[or]>nowor )
			nowor++;
		else 
		if ( orange[or]<nowor )
			nowor--;
		}
		if ( bl<blue.size() )
		{
		if ( blue[bl]==nowbl )
		{
			if ( pos[comp].second=='B' )
			{
				bl++;
				comp++;
			}
		}
		else
		if ( blue[bl]>nowbl )
			nowbl++;
		else 
			if ( blue[bl]<nowbl )
				nowbl--;
		}
		timer++;
		//cout<<timer<<' '<<nowor<<' '<<nowbl<<endl;
	}
	cout<<"Case #"<<t<<": "<<timer<<endl;
}