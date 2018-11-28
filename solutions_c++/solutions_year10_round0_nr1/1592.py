#include<iostream>
using namespace std;
int t;
int a[32];
int temp = 1;
int temp_;
int n,k;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin >> t;
	a[1]= 1;
	temp = 1;
	for (int i = 2; i< 31; i++)
	{
		temp *=2;
		a[i] += a[i-1];
		a[i] += temp;
	}
	for (int test = 0 ; test < t; test++)
	{
	  	cin >> n >> k;
	  	temp = 0;
	    while (k>0)
	    {
			temp_ = k % 2;
			if (temp_ == 0)
				break;
			k = k / 2;
			temp++ ;
		}
		if  (temp>=n)	
		cout<<"Case #"<<test+1<<": "<<"ON"<<endl;	  	
		else 
		cout<<"Case #"<<test+1<<": "<<"OFF"<<endl;
	}
	return 0;
}
