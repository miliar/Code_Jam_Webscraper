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
int A,B,P;
int i,j,k;
int m[1001][1001];
int u[1001];
inline bool prime(int x)
{
	for(int i=2;i*i<=x;i++)
		if (x%i==0)
			return false;
	return true;
}
void dfs(int v)
{
	u[v]=true;
	for(int i=A;i<=B;i++)
		if (!u[i]&&m[v][i])
			dfs(i);
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>cnt;
	for(cc=1;cc<=cnt;cc++)
	{
		cin>>A>>B>>P;
		C(m,0);
		for(i=A;i<B;i++)
			for(j=i+1;j<=B;j++)
			{
				k=P;
				while(k<=i&&!(prime(k)&&i%k==0&&j%k==0))
					k++;
				if (k<=i)
				{
					m[i][j]=1;
					m[j][i]=1;
				}
			}
		int rez=0;
		C(u,0);
		for(i=A;i<=B;i++)
			if (!u[i])
			{
				rez++;
				dfs(i);
			}
		cout<<"Case #"<<cc<<": "<<rez<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}