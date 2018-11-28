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
		return 0;
}
//#define int li
void solve (int t)
{
	int r, c;
	string s[60];
	int mas[60][60];
	cin>>r>>c;
	for ( int i=0; i<r; i++ )
		cin>>s[i];
	for ( int j=0; j<c; j++ )
	{
		if ( s[0][j]=='#' )
		{
			if ( j<c-1 && s[0][j+1]=='#' )
			{
				s[0][j]='/'; s[0][j+1]='\\';
				mas[0][j]=1; mas[0][j+1]=2;
				j++;
			}
			else
			{
				printf ("Case #"); cout<<t<<":"<<endl<<"Impossible"<<endl;
				return;
			}
		}
	}
	for ( int i=1; i<r; i++ )
	{
		for ( int j=0; j<c; j++ )
		{
			if ( s[i][j]=='#' )
			{
				if ( mas[i-1][j]==1 && s[i-1][j]=='/' && j<c-1 && s[i-1][j+1]=='\\')
				{
					s[i][j]='\\';
					mas[i][j]=1;
				}
				else
				if ( mas[i-1][j]==2 && s[i-1][j]=='\\' && j>0 && s[i-1][j-1]=='/')
				{
					s[i][j]='/';
					mas[i][j]=2;
				}
				else
				{
				if ( j<c-1 && s[i][j+1]=='#' )
				{
				s[i][j]='/'; s[i][j+1]='\\';
				mas[i][j]=1; mas[i][j+1]=2;
				j++;
				}
				else
				{
				printf ("Case #"); cout<<t<<":"<<endl<<"Impossible"<<endl;
				//cout<<i<<endl;
				return;
				}
				}
			}
		}
	}
	for ( int j=0; j<c-1; j++ )
	{
		if ( s[r-1][j]=='\\' )
		{
			j++;
			continue;
		}
		if ( s[r-1][j]=='/' && s[r-1][j+1]=='\\' )
			{
				printf ("Case #"); cout<<t<<":"<<endl<<"Impossible"<<endl;
				return;
			}
	}
	printf ("Case #"); cout<<t<<":"<<endl;
	for ( int i=0; i<r-1; i++ )
		for ( int j=0; j<c-1; j++ )
		{
			if ( mas[i][j]==1 && s[i][j]=='/' )
			{
				if ( mas[i+1][j]!=1 || s[i+1][j]!='\\' )
				{
					printf ("Impossible\n");
					return;
				}
			}
		}
	for ( int i=0; i<r; i++ )
		cout<<s[i]<<endl;
}