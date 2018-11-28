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
	int c, d, n;
	string s[30];
	vector <pair <char, char> > q[30];
	cin>>c;
	for ( int i=0; i<c; i++ )
	{
		char h, g, l;
		cin>>h>>g>>l;
		q[h-'A'].pb(mp (g, l) );
		q[g-'A'].pb( mp (h, l) );
	}
	cin>>d;
	for ( int i=0; i<d; i++ )
	{
		char e, r;
		cin>>e>>r;
		s[e-'A'].pb(r);
		s[r-'A'].pb(e);
	}
	cin>>n;
	int was[30];
	memset (was, 0, sizeof (was));
	string res;
	for ( int i=0; i<n; i++ )
	{
		char cur;
		cin>>cur;
		res.pb(cur);
		//cout<<res.size()<<"     ";
		was[cur-'A']++;
		//cout<<was[0]<<endl;
		if ( res.size()>1 )
		{
			bool flag=false;
			char now=res[res.size()-2];
			for ( int j=0; j<q[now-'A'].size(); j++ )
			{
				char need=q[now-'A'][j].first;
				if ( need==cur )
				{
					char z=q[now-'A'][j].second;
					was[need-'A']--;
					was[now-'A']--;
					res.pop_back();
					res.pop_back();
					res.pb(z);
					was[z-'A']++;
					flag=true;
					break;
				}
			}
			if ( !flag )
			{
				for ( int j=0; j<s[cur-'A'].size(); j++ )
				{
					char now=s[cur-'A'][j];
					//cout<<now<<' '<<was[now-'A']<<endl;
					if ( was[now-'A']>0 )
					{
						res.resize(0);
						memset (was, 0, sizeof (was));
						break;
					}
				}
			}
		}
	}
	cout<<"Case #"<<t<<": "<<"[";
	if ( res.size()>0 )
	for ( int i=0; i<res.size(); i++ )
	{
		cout<<res[i];
		if ( i<res.size()-1 )
			cout<<", ";
	}
	cout<<"]"<<endl;
}