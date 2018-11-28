#include<iostream>
using namespace std;
int mod(int);
int main()
{
	int t,n,p,blue,orange,time,lo,lb,count;
	char r;
	
	cin>>t;
	count=0;
	while(t--)
	{
		count++;
		cin>>n;
		blue=1;orange=1;time=0,lo=0,lb=0;
		while(n--)
		{
			cin>>r>>p;
			if(r=='O')
			{
				if(time-lo<=mod(orange-p))
					time=time+mod(orange-p)+1-(time-lo);
				else
					time+=1;
				lo=time;
				orange=p;
			}
			else
			{
				if(time-lb<=mod(blue-p))
					time=time+mod(blue-p)+1-(time-lb);
				else
					time+=1;
					lb=time;
				blue=p;
			}
			
		}
		cout<<"Case #"<<count<<": "<<time<<endl;
	}
}

int mod(int a)
{
	if (a<0) return -a;
	else return a;
}
