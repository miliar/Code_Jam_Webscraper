#include<iostream>
using namespace std;

bool light[32];

int main()
{
	//freopen("A-small-attempt1.in","r",stdin);
	//freopen("A-small-attempt0.out","w",stdout);
		
	long int T,i,N,K,j,kase;
	int state;

	cin>>T;

	for(kase=1;kase<=T;kase++)
	{
		cin>>N>>K;
	
		for(i=1;i<=N;i++)
			light[i]=0;

		for(i=1;i<=K;i++)
		{
			for(j=1;j<=N;j++)
			{
				if (j==1)	
				{
					if (light[j]==0) {light[j]=1;break;}
					else if (light[j]==1) light[j]=0;
				}
				else if (j>1)
				{
					if (light[j]==0) {light[j]=1;break;}
					else if (light[j]==1) light[j]=0; 
				}
			}

			/*
			cout <<i<<" : ";

			for(j=1;j<=N;j++)
				cout<<light[j]<<" ";

			cout<<"\n";
			*/

		}


		state=1;

		for(i=1;i<=N;i++)
		{
			if (light[i]==0) {state=0;break;}
		}

		if (state==1) cout << "Case #" << kase << ": ON\n";	
		else if (state==0) cout << "Case #" << kase << ": OFF\n";	
		
	}

	return 0;
}