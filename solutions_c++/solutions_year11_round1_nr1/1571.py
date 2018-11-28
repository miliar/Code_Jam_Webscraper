#include<iostream>
#include<math.h>
#include<stdlib.h>
#include<string.h>

using namespace std;

int main()
{
	int T,N,pD,pG;
	float wD,wG;
	int x,y,flag=0;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		cin>>N>>pD>>pG;
		cout<<"Case #"<<t+1<<": ";
		flag=0;
		for(int i=N;i>0;i--)
		{
			wD=(float)(i*pD)/100;
			x=(int)wD;
			if(!((pG==100 && pD!=100)||(pG==0 && pD!=0)))
			if((float)wD-x==0.0)
			{
				cout<<"Possible"<<endl;
				flag=1;
				break;
			}
		}
		if(!flag) cout<<"Broken"<<endl;
	}
	return 0;
}