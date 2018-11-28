#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <set>
#include <queue>

using namespace std;

bool check(int k)
{
     for (int i = 2 ;i <= k/2; ++i)
         if(k % i == 0)
             return false;
     return true;
}

void solve()
{
	int n; 
     cin >> n;
     int ans1= 0, ans2 = 1;
     for (int i = 2; i <= n; i++)
     {
         if (check(i))
             ans1++;
     }
     
     for (int i = 2 ; i <= n; i++)
     {
         if(check(i) == false)
             continue;
		 int t = i;
         while(t <= n)
         {
			 ans2++;
             t=t*i;
         }
     }
	 if(ans1==0)
		 ans1=1;
     cout<< ans2 - ans1;
}

int main()
{
	cout.precision(10);
	freopen("file.in","r",stdin);
	freopen("file.out","w",stdout);

	int t;
	cin>>t;

	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<(i+1)<<": ";
		solve();
		cout<<endl;
	}

	return 0;
}