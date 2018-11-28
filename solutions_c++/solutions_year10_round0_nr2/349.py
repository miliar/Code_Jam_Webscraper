#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

long long gcd(long long a,long long b)
{
	if(b==0) return(a);
	if(a%b==0) return(b);
	else return(gcd(b,a%b));
}
 
int main()
{
	long long test,numtest,i,j,n,a[100],ans,k;
	string st;
	ifstream cin ("a.in");
	ofstream cout ("a.out");
	cin >> numtest;
	for(test=1;test<=numtest;test++)
	{
		cin >> n;
		for(i=1;i<=n;i++) cin >> a[i];
		if(a[1]>a[2]) ans=a[1]-a[2];else ans=a[2]-a[1];
		for(i=2;i<n;i++)
		{
			if(a[i]>a[i+1]) k=a[i]-a[i+1];else k=a[i+1]-a[i];			
			if(k>ans){a[0]=ans;ans=k;k=a[0];}
			//cout << ans << ' ' << k << endl;
			ans=gcd(ans,k);
		}
		
		cout << "Case #" << test << ": " << (ans-a[1]%ans)%ans << endl;
	}
}
