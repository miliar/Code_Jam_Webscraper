#include <iostream>
#include<sstream>

#include <cmath>
using namespace std;

int cand[1100];
int main ()
{

	int t,n;
	int re=0;
	int sum=0;
	int temp=0;

	freopen("C:\\Users\\NAZI\\Desktop\\C-large.in", "rt", stdin);
	freopen("C:\\Users\\NAZI\\Desktop\\C-large.out", "wt", stdout);
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n;

		for(int j=0;j<n;j++)
		{
			cin>>cand[j];
			re=re^cand[j];
			sum+=cand[j];
		}
		if(re==0)
		{
			temp=cand[0];
			for(int p=1;p<n;p++)
			{
				if(temp>cand[p])
				{
					temp=cand[p];
				}
			}
			cout<<"Case #"<<i+1<<": "<<sum-temp<<endl;
		}
		else
		{
			cout<<"Case #"<<i+1<<": NO"<<endl;
		}
		sum=0;re=0;
	}
	

	return 0;
}

