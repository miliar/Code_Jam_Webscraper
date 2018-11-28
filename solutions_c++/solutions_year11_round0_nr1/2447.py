#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	int T,M, b, t;
	int wb,wo,lb,lo;
	char c;
	cin>>T;
	for(int i = 0; i < T; i++)
	{
		cin>>M;
		wb=0;
		wo=0;
		lb=1;
		lo=1;
		t=0;
		for(int j = 0; j < M; j++)
		{
			cin >> c >> b;
			if(c=='O')
			{
				if(abs(b-lo)<=wo)
				{
					t+=1;
					wb+=1;
				}	
				else
				{
					t+=abs(b-lo)+1-wo;
					wb+=abs(b-lo)+1-wo;
				}	
				wo=0;
				lo=b;
			}
			
			else {
				if(abs(b-lb)<=wb)
				{
					t+=1;
					wo+=1;
				}	
				else
				{
					t+=abs(b-lb)+1-wb;
					wo+=abs(b-lb)+1-wb;
				}	
				wb=0;
				lb=b;
			}
			
		}
		cout<<"Case #"<<(i+1)<<": "<<t<<endl;
	}
}
