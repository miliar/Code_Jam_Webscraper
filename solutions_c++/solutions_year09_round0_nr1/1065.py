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
int n,l,d;
string a[5000];
bool ok[5000];
bool b[15][255];
string t;
int main()
{	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>l>>d>>n;
	for(int i=0;i<d;++i)
		cin>>a[i];
	for(int test=1;test<=n;++test)
	{
		for(int i=0;i<d;++i)
			ok[i]=true;
		C(b);
		cin>>t;
		for(int i=0,j=0;i<L(t);++i,++j)
			if (t[i]!='(')
				b[j][t[i]]=true;
			else
			{
				++i;
				while(t[i]!=')')
				{
					b[j][t[i]]=true;
					++i;
				}
			}
		for(int i=0;i<l;++i)
			for(int j=0;j<d;++j)
				if (!(b[i][a[j][i]]))
					ok[j]=false;
		int rez=0;
		for(int i=0;i<d;++i)
			rez+=ok[i];
		cout<<"Case #"<<test<<": "<<rez<<endl;
	}
	return 0;
}