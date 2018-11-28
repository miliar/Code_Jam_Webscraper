#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
using namespace std;



void solve(int t)
{
	int n,i,x;
	double ans;
	ans = 0.0;
	cin >> n;
	for(i = 1; i <= n; i++)
	{
		cin >> x;
		if(x != i) ans+= 1.0;
	}
	printf("Case #%d: %.6lf\n",t,ans);
}
		
	
int main()
{
    int T,t;
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
	cin >> T;
	for(t = 1; t <= T; t++) solve(t);
}
