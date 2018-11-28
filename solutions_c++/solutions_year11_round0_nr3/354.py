#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <bitset>
#include <string>
#include <vector>
#include <algorithm>
#include <ctime>
#include <queue>
#include <cstring>
#include <set>
#include <map>
#include <sstream>
#include <cmath>
#include <fstream>
#include <list>
using namespace std;
#define rp(i,n) for(int (i)=0;(i)<(n);++(i))
#define pb push_back
#define L(s) (int)s.size()
#define mp make_pair
#define pii pair<int,int>
#define x first 
#define y second
#define inf 1000000000
#define VI vector<int>
#define ll long long
#define all(s) (s).begin(),(s).end()
#define C(u) memset((u),0,sizeof((u)))
#define ull unsigned ll
#define uint unsigned int 
int t,n,s,xx;
int a[1111];
int c[1<<20];
int cc[1<<20];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	rp(num,t)
	{
		cerr<<num<<endl;
		cin>>n;
		s=0;
		xx=0;
		memset(c,-1,sizeof(c));
		c[0]=0;
		rp(i,n)
		{
			memset(cc,-1,sizeof(cc));
			int x;
			cin>>x;
			s+=x;
			xx^=x;
			rp(j,1<<20)
				if (c[j]!=-1)
					cc[j^x]=max(cc[j^x],c[j]+x);
			rp(j,1<<20)
				c[j]=max(c[j],cc[j]);
		}
		cout<<"Case #"<<num+1<<": ";
		if (xx)
			cout<<"NO\n";
		else
			cout<<*max_element(c+1,c+(1<<20))<<endl;

	}
}