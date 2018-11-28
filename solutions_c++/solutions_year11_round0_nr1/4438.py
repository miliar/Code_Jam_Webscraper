#include <iostream>

using namespace std;

int main()
{
	long t,n;  //test cases and number of operations
	long po,pb; //current position
	long to,tb,lasto,lastb; //time taken to move and last time operation was performed
	long time;   //total time
	char color;
	long testCase=1;
	long pos;

	cin>>t;
	while(t--)
	{
		lasto=lastb=time=0;
		po=pb=1;

		cin>>n;
		while(n--)
		{
			cin>>color>>pos;
			
			if(color=='O')
			{
				long temp=pos-po;
				if(temp>0) to=temp;
				else to=(-1*temp);

				if(time-lasto>to)
					time=time+1;					
				else
					time=time+(to-(time-lasto))+1;
				po=pos;
				lasto=time;
			}	
			
			else
			{
				long temp=pos-pb;
				if(temp>0) tb=temp;
				else tb=(-1*temp);


				if(time-lastb>tb)
					time=time+1;					
				else
					time=time+(tb-(time-lastb))+1;
				pb=pos;
				lastb=time;
			}	

		}
		cout<<"Case #"<<testCase<<": "<<time<<endl;
		testCase+=1;
	}
	return 0;
}
