#include<iostream>
#include<vector>
#include<string>

using namespace std;

vector<vector<int> > M,Mn;

vector<int> temp(100,0);

int empty()
{
	for(int i=0;i<100;i++)
		for(int j=0;j<100;j++)if(M[i][j]==1)return 0;

	return 1;
}
main()
{

	for(int i=0;i<100;i++)
	{
		M.push_back(temp);
		Mn.push_back(temp);
	}

	int C,R,x1,x2,y1,y2;
	cin >> C;
	for(int l=0;l<C;l++)
	{
		cin >> R;
		for(int i=0;i<R;i++)
		{
			cin >> x1>>y1>>x2>>y2;

			for(int k=y1;k<=y2;k++) 
				for(int j=x1;j<=x2;j++)
					M[k-1][j-1]=1;


		}
		int count=0;
		while(!empty())
		{


			for(int i=0;i<100;i++)
			{
				for(int j=0;j<100;j++)
				{
					if(M[i][j]==1)
					{
						if((i==0) && (j==0))
						{
									Mn[i][j]=0;}
						else if((i==0) && (j>0) && (M[i][j-1]==0)){Mn[i][j]=0;}
						else if((j==0) && (i>0) && (M[i-1][j]==0)){Mn[i][j]=0;}
						else if((i>0) && (j>0) && (M[i-1][j] == 0) && (M[i][j-1]==0)){Mn[i][j]=0;}
						else Mn[i][j]=M[i][j];
					}
					else if(M[i][j]==0)
					{
						if(i>0 && j>0 && M[i-1][j]==1 && M[i][j-1]==1)Mn[i][j]=1;
						else Mn[i][j]=M[i][j];
					}
				//	cout<<i<<' '<<j<<'\n';
				}
				
			}
			for(int i=0;i<100;i++)	
				for(int j=0;j<100;j++) 
					M[i][j]=Mn[i][j];
			//M=Mn;
			count++;
		}
		cout<<"Case #"<<l+1<<": "<<count<<'\n';
		for(int i=0;i<100;i++)
			for(int j=0;j<100;j++)
			{M[i][j]=Mn[i][j]=0;}
	
	}
}
						
						
		
		
	
	
