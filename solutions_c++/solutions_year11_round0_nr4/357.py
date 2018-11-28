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
int t,n,a[1111],d[1111],u[1111];
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	rp(num,t)
	{
		cin>>n;
		rp(i,n)
		{
			cin>>a[i];
			d[i]=a[i];
		}
		sort(d,d+n);
		rp(i,n)
			a[i]=lower_bound(d,d+n,a[i])-d;
		C(u);
		int ans=0;
		rp(i,n)
			if (!u[i])
			{
				int len=0;
				int pos=i;
				do
				{
					len++;
					u[pos]=1;
					pos=a[pos];
				}while(!u[pos]);
				if (len>1)
					ans+=len;
			}
			cout<<"Case #"<<num+1<<": "<<ans<<".000000\n";
	}
}
