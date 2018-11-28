#include <iostream>

using namespace std;

int main()
{
	int te,i,j,x,k,n,s,sum,p,t[100];
	cin>>te;
	for(x=1;x<=te;x++)
	{
		int S=0,N=0,diff;
		cin>>n;
		cin>>s;
		cin>>p;
		sum=0;
		for(i=0;i<n;i++)
		{
			cin>>t[i];
			switch(t[i]%3)
			{
				case 0:
					if(t[i]/3-p>=0)
						N++;
					else if(t[i]>=3 && t[i]/3-p>=-1)
						S++;
					break;
				case 1:
					if((t[i]/3+1)-p>=0)
						N++;
					break;
				case 2:
					if((t[i]/3+1)-p>=0)
						N++;
					else if((t[i]/3+2)-p==0)
						S++;
					break;
			}		
		}
		
		diff=s-S;
		if(diff>=0)
			N=N-diff;
		sum+=N;
		sum+=s;
		cout<<"Case #"<<x<<": "<<sum<<endl;	
	}
	return 0;
}
