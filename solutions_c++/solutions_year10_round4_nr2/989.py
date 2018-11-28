#include<iostream>
#include<cmath>
#include<vector>
using namespace std;

main()
{
	int cases,P,keka;

	cin >> cases;

	for(int l=0;l<cases;l++)
	{
		cin >> P;
		int noteams=pow(2.0,P);
		vector<int> M(noteams,0);
		
		for(int i=0;i<noteams;i++)cin >> M[i];
		int size=noteams,count=0,waste;
		for(int i=0;i<P;i++)
		{
			size=size/2;
			for(int j=0;j<size;j++)cin >> waste;
		}
			

		vector<int> temp=M;
		size=noteams;
		for(int i=0;i<P;i++)
		{
			size=size/2;
			if(i==0)keka=0;
			else keka=1;
			for(int j=0;j<size;j++)
			{
				if(temp[2*j]==0 || temp[2*j+1]==0)temp[j]=0;
				else if(temp[2*j]<=temp[2*j+1])temp[j]=temp[2*j]-keka;
				else temp[j]=temp[2*j+1]-keka;
				
				if(temp[j]==0)count++;
			}
		}
		cout<<"Case #"<<l+1<<": "<<count<<'\n';
	}
}
			
			
		
