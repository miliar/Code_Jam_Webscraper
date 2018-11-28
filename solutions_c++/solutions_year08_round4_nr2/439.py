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
int a,n,m,i,j,k,l;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>cnt;
	for(cc=1;cc<=cnt;cc++)
	{
		cout<<"Case #"<<cc<<": ";
		cin>>n>>m>>a;
		bool ok=false;
		for(i=0;i<=n;i++)
			for(j=0;j<=m;j++)
				for(k=0;k<=n;k++)
					for(l=0;l<=m;l++)
						if (abs(i*l-j*k)==a&&!ok)
						{
							cout<<"0 0 "<<i<<" "<<j<<" "<<k<<" "<<l;
							ok=true;
						}
		if (!ok)
			cout<<"IMPOSSIBLE";
		cout<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}