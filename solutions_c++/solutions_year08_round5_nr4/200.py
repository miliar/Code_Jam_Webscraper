#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <fstream>
using namespace std;
#define pb push_back
#define ppb pop_back
#define mp make_pair
//#define pi 2*acos(0.0)
#define mp make_pair
//#define x first
//#define y second
#define sqr(a) (a)*(a)
#define pii pair<int,int>
#define pdd pair<double,double>
#define sz(c) (int)((c).size())
#define inf 1000000000
#define all(c) (c).begin(), (c).end()
#define vi vector<int>
#define vpii vector< pii >
#define vpdd vector< pdd >
#define L(s) (int)((s).end()-(s).begin())
#define ll long long
#define C(a,b) memset((a),(b),sizeof((a)))
int cnt,cc;
ll a[100][100],b[100][100];
int n,m,i,j,k;
vi r,c;
inline bool nm(int p,int q)
{
	if (p<0||q<0)
		return false;
	else
		return true;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>cnt;
	for(cc=1;cc<=cnt;cc++)
	{
		cout<<"Case #"<<cc<<": ";
		cin>>n>>m>>k;
		r.clear();
		c.clear();
		for(i=0;i<k;i++)
		{
			cin>>j;
			r.pb(j);
			cin>>j;
			c.pb(j);
		}
	a[0][0]=1;
	for(int cn=0;cn<(n+m)/3;cn++)
	{
		C(b,0);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				k=0;
				while(k<L(r)&&!(r[k]==i+1&&c[k]==j+1))
					k++;
				if (k<L(r))
					continue;
				if (nm(i-1,j-2))
					b[i][j]+=a[i-1][j-2];
				if (nm(i-2,j-1))
					b[i][j]+=a[i-2][j-1];
			}
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				a[i][j]=(b[i][j])%10007;
	}
	cout<<a[n-1][m-1]<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}