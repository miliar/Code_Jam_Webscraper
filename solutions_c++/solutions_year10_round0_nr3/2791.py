#include"iostream"
#include"fstream"
#include"stdio.h"
#include"cmath"
#include"queue"
using namespace std;
int main() 
{
	ifstream cin("C-small-attempt0.in");
	ofstream cout("sqh.txt");
	queue<int>a;
	int count,i,j;
	cin>>count;
	for(i=0;i<count;i++)
	{
		int r,k,n,temp,sum=0,result=0;
		cin>>r>>k>>n;
		for(j=0;j<n;j++)
		{
			cin>>temp;
			sum+=temp;
			a.push(temp);
		}	
		if(sum<=k) cout<<"Case #"<<i+1<<": "<<sum*r<<endl;
		else
		{
			for(j=0;j<r;j++)
			{
				int t=k;
				while(t-a.front()>=0)
				{
					result+=a.front();
					t-=a.front();
					a.push(a.front());
					a.pop();
				}
			}
			cout<<"Case #"<<i+1<<": "<<result<<endl;
		}
		while(!a.empty()) a.pop();
	}	
	return 0;
}




  
















