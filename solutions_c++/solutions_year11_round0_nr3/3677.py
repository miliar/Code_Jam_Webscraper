#include <iostream>
using namespace std;
int a[1000];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("1.out","w",stdout);
    int t,i=1;
    cin>>t;
    while(t--)
    {
    	int n,j,temp=0,min=10000000;
    	cin>>n;
    	for(j=0;j<n;j++)
    	cin>>a[j];
    	for(j=0;j<n;j++)
    	temp=temp^a[j];
    	cout<<"Case #"<<i++<<": ";
    	if(temp)
    	{
    		cout<<"NO\n";
    		continue;
    	}
    	for(j=0;j<n;j++)
    	{
    		min=min<a[j]?min:a[j];
    		temp+=a[j];
    	}
    	cout<<temp-min<<endl;
    }
    return 0;
}