#include<iostream>
#include<cmath>
using namespace std;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int test;
	cin>>test;
	for(int t = 0;t<test;t++)
	{
		int n;
		cin>>n;
		int k;
		double mass[6] = {0};
		
		for(int i =0;i<n;i++)
		{
			for(int j = 0;j<6;j++)
			{
				cin>>k;
				mass[j]+=k;
			}
		}
		//for(int i = 0;i<6;i++)
		//	mass[i]/=(double) n;
		double a = mass[3]*mass[3] + mass[4]*mass[4] + mass[5]*mass[5];
		double b = mass[3]*mass[0] + mass[4]*mass[1] + mass[5]*mass[2];
		double c = mass[0]*mass[0] + mass[1]*mass[1] + mass[2]*mass[2];
		
		double x = 0;
		//cout<<a<<" "<<b<<" "<<c<<endl;
		if(a>0.0001) 
			x= -b/a;
		if(x<=0)
			x = 0;
		double ans = (mass[0] + x*mass[3])*(mass[0] + x*mass[3]) + (mass[1] + x*mass[4])*(mass[1] + x*mass[4]) + (mass[2] + x*mass[5])*(mass[2] + x*mass[5]);
		//cout<<ans<<endl;
			cout<<"Case #"<<t+1<<": "<<(double)sqrt(ans)/(double)n<<" "<<x<<endl;
		
		
		
		
	}
	return 0;
}
