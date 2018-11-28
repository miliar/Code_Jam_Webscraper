#include <iostream>
using namespace std;
int a[50], n;
void work()
{
	int ans;
	for(int i=0; i<n; i++)
	{
		int j;
		for(j=i; j<n; j++)
		{
			if(a[j] <= i+1) break;
		}
		ans += (j-i);
		for(;j>i; j--) a[j] = a[j-1];
	}
	cout << /*"greed1 " <<*/ ans << endl;
}
/*void work2()
{
	int ans;
	int x[50];
	for(int i=0; i<50; i++)x[i]=0;
	for(int i=0; i<n; i++)
	{
		for(int j=a[i]; j<n; j++) x[j]++;
	}
	for(int i=n-1; i>0; i--)
	{
		int t;
		for(t=1;t<=n;t++) if(x[t] > t) break;
		int j;
		for(j=i; j>=0; j--) if(a[j] > t) break;
	}
}*/
void init()
{
	cin >> n;
	string t;
	for(int i=0; i<n; i++)
	{
		cin >> t;
		for(a[i]=n-1;t.c_str()[a[i]]=='0';a[i]--);
		a[i]++;
		//cout << a[i] << endl;
	}
}
int main()
{
	int t,ct;
	cin >> t;
	for(ct=1; ct<=t; ct++)
	{
		init();
		cout << "Case #" << ct << ": ";
		work();
	}
	return 0;
}
