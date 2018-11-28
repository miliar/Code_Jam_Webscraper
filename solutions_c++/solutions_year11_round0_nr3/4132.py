#include <iostream>
using namespace std;

int main()
{
    int t, n , m;
    int min;
    int sum;
    int ans;
    int i,j,k;
    cin>>t;
    for (i = 0; i < t; i++)
    {
	cin>>n;
	sum = 0; 
	ans = 0;
	for (j = 0;j<n;j++)
	{
	    cin>>k;
	    if (j==0) min = k;
	    else if (k<min){
		min = k;
	    }
	    sum ^= k;
	    ans += k;
	}
	cout<<"Case #"<<i+1<<": ";
	if (sum==0) cout<<ans-min<<endl;
	else cout<<"NO"<<endl;
    }
    return 0;
}