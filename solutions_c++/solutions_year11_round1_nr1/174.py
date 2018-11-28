#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<utility>
#include<set>
#include<sstream>
#define fr(a,b,c) for (a=b;a<=c;a++)
#define frr(a,b,c) for (a=b;a>=c;a--)
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define F first
#define S second
#define oo 1000111222
using namespace std;
typedef long long ll;
const int dx[]={-1,0,1,0,-1,1,1,-1};
      int dy[]={0,1,0,-1,1,1,-1,-1};

int need[111];

int gcd(int x,int y)
{
	if (!x || !y) return x+y;
	return gcd(y,x%y);
}

int main()
{
	freopen("alarge.in","r",stdin); freopen("alarge.out","w",stdout);
	int test,it,wd,wg,i,re;
	long long n;
	fr(i,1,99) need[i]=100/gcd(i,100);
	cin >> test;
	fr(it,1,test)
	{
		cin >> n >> wd >> wg;
		if (!wg) re=(!wd);
		else
			if (wg==100) re=(wd==100);
			else re=(n>=need[wd]);
		cout << "Case #" << it << ": ";
		if (re) cout << "Possible" << endl;
		else cout << "Broken" << endl;
	}
	fclose(stdin); fclose(stdout);
   return 0;
}
