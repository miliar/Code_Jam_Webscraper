#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<sstream>
#include<stack>
#include<list>

#define Max(x,y) (x>y?x:y)
#define Min(x,y) (x<y?x:y)

using namespace std;
int T;


int n,num[10000];
int ans;

int check()
{
	int res = 0;
	for(int i = 1;i <= n;i++)res ^= num[i];
	return res == 0;
}

void solve()
{
	if(check() == 0)
	{
		printf("NO\n");
		return;
	}
	int mmin = 2147483647;
	ans = 0;
	for(int i = 1;i <= n;i++)
	{
		ans += num[i];
		mmin = Min(mmin,num[i]);
	}
	ans -= mmin;
	cout<<ans<<endl;
}

int main()
{
	freopen("f:\\GJ\\in.txt","r",stdin);
	freopen("f:\\GJ\\out.txt","w",stdout);

////////////////////////////////////////////////////////////////////

	cin>>T;
	int cases;
	for(cases = 1;cases <= T;cases++)
	{
		printf("Case #%d: ",cases);
		cin>>n;
		for(int i = 1;i <= n;i++)
			cin>>num[i];
		solve();
	}

////////////////////////////////////////////////////////////////////

	fclose(stdout);	
	return 0;
}