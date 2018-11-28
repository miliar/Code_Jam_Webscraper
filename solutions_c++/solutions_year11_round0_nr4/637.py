#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<sstream>
#include<stack>
#include<vector>
#include<list>

#define Max(x,y) (x>y?x:y)
#define Min(x,y) (x<y?x:y)

using namespace std;
int T;

int n,num[2000];

void solve()
{
	int ans = 0;
	for(int i = 1;i <= n;i++)
		if(num[i] != i)
			ans++;
	cout<<ans<<".000000"<<endl;
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
		for(int i = 1;i <= n;i++)cin>>num[i];
		solve();
	}

////////////////////////////////////////////////////////////////////

	fclose(stdout);	
	return 0;
}