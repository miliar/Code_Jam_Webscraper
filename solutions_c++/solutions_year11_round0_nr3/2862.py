#include<iostream>
#include<algorithm>
#include<cmath>
#include<fstream>
using namespace std;
ifstream fin("D:\\acm\\C-small-attempt2.in");
ofstream fout("D:\\acm\\C-small-attempt2.out");
#define cin fin
#define cout fout
int a[1001];
int main()
{
	int t;
	int n,i;
	cin>>t;
	int j=0;
	while(t--)
	{
	  cin>>n;
	  int sum1=0;
	  for(i=0;i<n;i++)
	  {
		cin>>a[i];
		sum1+=a[i];
	  }	  
	  sort(a,a+n);
	  
	  int sum=0;
	  for(i=0;i<n;i++)
	  {
		  sum=sum^a[i];
	  }
	  cout<<"Case #"<<++j<<": ";
	  if(sum==0) cout<<sum1-a[0]<<endl;
	     else cout<<"NO"<<endl;
			
	}
	return 0;
}