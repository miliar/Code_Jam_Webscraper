#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
using namespace std;



void solve(int t)
{
	int n,ans,minn,y,x,i;
	ans = 0;
	y = 0;
	minn = 10000000;
	cin >> n;
	for(i = 0; i < n; i++)
	{
		cin >> x;
		ans += x;
		y ^= x;
		if( x < minn ) minn = x;
	}
	ans -= minn;
	if(y != 0) printf("Case #%d: NO\n",t);
	else printf("Case #%d: %d\n",t,ans);
}
		
	
int main()
{
    int T,t;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
	cin >> T;
	for(t = 1; t <= T; t++) solve(t);
}
