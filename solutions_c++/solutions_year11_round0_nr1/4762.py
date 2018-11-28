#include<iostream>
#include<math.h>
using namespace std;


int T,N;

int main()
{

	freopen("e:\\A-large.in","r",stdin);

	int i,m,poso,posb,timeo,timeb;
	int k=1;
	char ch,chmark;
	cin>>T;
	while(T--)
	{
		poso=1;
		posb=1;
		timeo=0;
		timeb=0;
		cin>>N;
		cin>>chmark>>m;
		if(chmark=='B')
		{
			posb=m;
			timeb=m;
		}
		else
		{
			poso=m;
			timeo=m;
		}

		for(i=0;i<N-1;i++)
		{
			cin>>ch>>m;
			if(ch=='O')
			{
				if(ch==chmark)
				{
					timeo+=abs(m-poso)+1;
					poso=m;
				}
				else
				{
					chmark=ch;
					if(timeb-timeo>=abs(m-poso))
					{
						timeo=timeb+1;
						poso=m;
					}
					else
					{
						timeo+=abs(m-poso)+1;
						poso=m;
					}
				}
			}
			else
			{
				
				if(ch==chmark)
				{
					timeb+=abs(m-posb)+1;
					posb=m;
				}
				else
				{
					chmark=ch;
					if(timeo-timeb>=abs(m-posb))
					{
						timeb=timeo+1;
						posb=m;
					}
					else
					{
						timeb+=abs(m-posb)+1;
						posb=m;
					}
				}
			}
		}
		
		cout<<"Case #"<<k++<<": ";
		if(timeo>timeb)
			cout<<timeo<<endl;
		else
			cout<<timeb<<endl;
	}

	return 0;
}



	