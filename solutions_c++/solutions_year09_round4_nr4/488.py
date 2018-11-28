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
bool c[100][100];
bool on[100];
int n,m;
int y[100][30];
int X[3],Y[3],R[3];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>tests;
	for(int test=1;test<=tests;++test)
	{
/*		cin>>n>>m;
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
				cin>>y[i][j];
		C(c);
		for(int i=0;i<n;++i)
			for(int j=i+1;j<n;++j)
				for(int k=0;k<m-1;++k)
				{
					ll val=(ll)(y[i][k]-y[j][k])*(ll)(y[i][k+1]-y[j][k+1]);
					if (val<=0)
						c[i][j]=c[j][i]=true;
				}
		C(on);
		int rez=0;
		for(int i=0;i<n;++i)
			if (!on[i])
			{
				++rez;
				on[i]=true;
				for(int j=i+1;j<n;++j)
					if (!c[i][j]&&!on[j])
						on[j]=true;
			}
		cout<<"Case #"<<test<<": "<<rez<<endl;*/
		cin>>n;
		for(int i=0;i<n;++i)
			cin>>X[i]>>Y[i]>>R[i];
		if (n==1)
			printf("Case #%d: %0.8f\n",test,(double)R[0]);
		else
		if (n==2)
			printf("Case #%d: %0.8f\n",test,max((double)R[0],(double)R[1]));
		else
		{
			double d1=sqrt((double)(X[0]-X[1])*(X[0]-X[1])+(Y[0]-Y[1])*(Y[0]-Y[1]))+R[0]+R[1];
			double d2=sqrt((double)(X[0]-X[2])*(X[0]-X[2])+(Y[0]-Y[2])*(Y[0]-Y[2]))+R[0]+R[2];
			double d3=sqrt((double)(X[2]-X[1])*(X[2]-X[1])+(Y[2]-Y[1])*(Y[2]-Y[1]))+R[2]+R[1];
			d1=max(d1/2,(double)R[2]);
			d2=max(d2/2,(double)R[1]);
			d3=max(d3/2,(double)R[0]);
			printf("Case #%d: %0.8f\n",test,min((double)min((double)d1,d2),d3));
		}
	}	
	return 0;
}
