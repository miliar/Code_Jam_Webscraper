#define _CRT_SECURE_NO_WARNINGS
#include <ctime>
#include <cfloat>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <complex>

using namespace std;

#define pb push_back
#define L(s) (int)((s).end()-(s).begin())
#define rep(i,n) for(int (i)=0;(i)<(n);++(i))
#define all(s) (s).begin(),s.end()
#define pi 3.1415926535897932384626433832795
#define vi vector<int>
#define inf 1000000000
#define ll long long
#define C(a) memset((a),0,sizeof((a)))
#pragma comment(linker, "/STACK:16777216")
int tests;
char a[40][40];
int n;
bool ok(int i,int X)
{
	for(int j=n-1;j>X;--j)
		if (a[i][j]=='1')
			return false;
	return true;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>tests;
	for(int test=1;test<=tests;++test)
	{
		cin>>n;
		for(int i=0;i<n;++i)
			for(int j=0;j<n;++j)
				cin>>a[i][j];
		int rez=0;
		for(int i=0;i<n;++i)
		{
			int j=i;
			while(!ok(j,i))
				++j;
			for(int k=j-1;k>=i;--k)
			{
				++rez;
				for(int l=0;l<n;++l)
					swap(a[k][l],a[k+1][l]);
			}
		}
		cout<<"Case #"<<test<<": "<<rez<<endl; 
	}	
	return 0;
}
