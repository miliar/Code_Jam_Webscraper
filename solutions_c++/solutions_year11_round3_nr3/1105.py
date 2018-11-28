#include<iostream>
#include<cmath>
using namespace std;
long long gcd(long long x, long long y)
{
	if (y==0) return x;
	else
		return gcd(y, x%y);
}

int work(int test_now)
{
	cout<<"Case #"<<test_now+1<<": ";
	int n,l,r;
	cin>>n>>l>>r;
	int x[n];
	for (int i=0; i<n; i++)
		cin>>x[i];
	int ans=-1;
	for (int i=l; i<=r; i++)
        {
         int flag=1;
         for (int j=0; j<n; j++)
             if (x[j]%i!=0&&i%x[j]!=0)
                flag=0;
         if (flag)
            {
                  ans=i;
                  break;
                  }
        } 
	if (ans==-1)
		cout<<"NO"<<endl;
	else
		cout<<ans<<endl;
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
