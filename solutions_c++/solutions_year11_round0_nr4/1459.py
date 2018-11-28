#include<iostream>
using namespace std;

int work(int test_now)
{
	int n;
	cin>>n;
	int ans=0;
	for (int i=0; i<n; i++)
		{
			int x;
			cin>>x;
			if (x-1==i)	
				ans++;
		}
	cout<<"Case #"<<test_now+1<<": ";
	cout<<n-ans<<".000000"<<endl;
}


int main()
{
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
	int test_num;
	cin>>test_num;
	for (int i=0; i<test_num; i++)
		work(i);
	return 0;
}
