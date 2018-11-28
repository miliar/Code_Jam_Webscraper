#include <iostream>

using namespace std;
int a[32],p;
long long ans[33],x;
void go(int s)
{
	a[s] = abs(a[s]-1);
	if(s==p)	
	{
		ans[p] = x;
		p++;
	}
	if(!a[s]) go(s+1);
}
bool rep(int x1,long y)
{
	if(y == ans[x1]) return true;
	if(y < ans[x1]) return false;
	if((y+1)%(ans[x1]+1) == 0) return true; else return false;
	/*int j;
	while(y > ans[x1])
	{
		j = 0;
		while(ans[j] <= y) j++;
		y -= (ans[j-1]+1);
	}
	if(ans[x1] == y) return true;
	else return false;*/
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int t,n,k;
	cin >> t;
	p = 1;
	while(x < 100000003)
	{
		go(0);
		x++;
	}
	for(int i=0;i<t;i++)
	{
		cin >> n >> k;
		if(ans[n] == 0) cout << "Case #" << i+1 << ": OFF" << endl;
		else
		{
			if(rep(n,k))
				cout << "Case #" << i+1 << ": ON" << endl;
			else
				cout << "Case #" << i+1 << ": OFF" << endl;
		}	
	}
	return 0;
}
