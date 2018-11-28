#include<iostream>
#include<fstream>
using namespace std;

typedef struct 
{
	char ch;
	int t;
}b;

b botton[110];

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	int T;
	cin>>T;
	int k;
	for(k=1; k<=T; k++)
	{
		int n;
		int i;
		cin>>n;
		for(i=0; i<n; i++)
		{
			cin>>botton[i].ch;
			cin>>botton[i].t;
		}
		int time,nowo,nowb,ido,idb;
		time=nowo=nowb=ido=idb=0;
		for(i=0; i<n; i++)
		{
			if(botton[i].ch=='O')
			{
				time=abs(botton[i].t-ido);
				ido=botton[i].t;
				if(time+nowo<=nowb)
				{
					nowo=nowb+1;
				}
				else
					nowo=time+nowo+1;
			}
			if(botton[i].ch=='B')
			{
				time=abs(botton[i].t-idb);
				idb=botton[i].t;
				if(time+nowb<=nowo)
				{
					nowb=nowo+1;
				}
				else
					nowb=time+nowb+1;
			}
		}
		if(botton[n-1].ch=='O')
			cout<<"Case #"<<k<<": "<<nowo-1<<endl;
		else
			cout<<"Case #"<<k<<": "<<nowb-1<<endl;
	}

	return 0;
}