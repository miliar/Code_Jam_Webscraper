#define _CRT_SECURE_NO_WARNINGS
#include <ctime>
#include <cfloat>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
#define pb push_back
#define L(s) (int)(s).size()
#define rp(i,n) for(int (i)=0;(i)<(n);++(i))
#define fr(i,st,fn) for(int (i)=(st);(i)<=(fn);++(i))
#define VI vector<int>
#define inf 1000000000
#define ll long long
#define C(a) memset((a),0,sizeof((a)))
#define all(s) (s).begin(),s.end()
#define pi 3.1415926535897932384626433832795
#define pii pair<int,int>
#define mp make_pair
//#define x first
//#define y second
int r,k,n;
int a[1111];
ll add;
int pos,step;
void doit()
{
	do
	{
		ll cur=0;
		while(pos<n&&cur<=k)
			cur+=(ll)a[pos++];
		if (pos==n&&cur<=k)
		{
			pos=0;
			while(cur<=k)
				cur+=(ll)a[pos++];
		}
		--pos;
		cur-=a[pos];
		add+=cur;
		++step;
	}while(pos!=0&&step<r);
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ts;
	scanf("%d",&ts);
	for(int test=1;test<=ts;++test)
	{
		printf("Case #%d: ",test);
		scanf("%d%d%d",&r,&k,&n);
		ll sum=0;
		for(int i=0;i<n;++i)
		{
			scanf("%d",&a[i]);
			sum=sum+(ll)a[i];
		}
		if (sum<=k)
		{
			cout<<(ll)r*(ll)sum<<endl;
			continue;
		}
		add=0;
		pos=0;
		step=0;
		doit();
		if (step==r)
		{
			cout<<add<<endl;
			continue;
		}
		add*=(ll)(r/step);
		r%=step;
		step=0;
		pos=0;
		if (r)
			doit();
		cout<<add<<endl;
	}
}