#include <iostream>
using namespace std;
int T;
int TO;
int TB;
int posO,posB;
int dT;
int main()
{
	int N,cnt,i,num,TT;
	char str[10];
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","a+",stdout);
	cin>>TT;
	cnt=1;
	while(TT--)
	{
		cin>>N;
		
		TO=TB=T=0;
		posO=posB=1;
		for(i=0;i<N;++i)
		{
			cin>>str>>num;
			if(str[0]=='O')
			{
				dT=abs(num-posO);
				if(dT<=T-TO)
				{
					T=TO=T+1;
				}
				else
				{
					TO=T=TO+dT+1;
				}
				posO=num;
			}
			else if(str[0]=='B')
			{
				dT=abs(num-posB);
				if(dT<=T-TB)
				{
					T=TB=T+1;
				}
				else
				{
					TB=T=TB+dT+1;
				}
				posB=num;
			}
		}
		cout<<"Case #"<<cnt<<": "<<T<<endl;
		cnt++;
	}
	return 0;
}