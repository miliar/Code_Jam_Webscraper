#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main()
{
	int nt;
	cin>>nt;
	for(int i=0;i<nt;i++)
	{
			int R,C;
			cin>>R>>C;
			vector<string> hold;
			for(int j=0;j<R;j++)
			{
				string temp;
				cin>>temp;
				hold.push_back(temp);

			}
			
			//check for square
			int count=0;
			for(int m=0;m<R;m++)
			{
				for(int k=0;k<C;k++)
				{
					if(hold[m][k]=='#')
					count++;		
				}
			}
			if(count%4!=0)
			cout<<"Case #"<<i+1<<":\nImpossible\n";
			else
			{
				int flag=1;
				for(int m=0;m<R&&flag;m++)
				{
					
					for(int k=0;k<C&&flag;k++)
					{
						if(hold[m][k]=='#')
						{
							if(k+1<C&&hold[m][k+1]=='#'&&m+1<R&&hold[m+1][k]=='#'&&hold[m+1][k+1]=='#')
							{
								hold[m].replace(k,1,'/');
								hold[m+1].replace(k+1,1,'/');
								hold[m].replace(k+1,1,'\\');
								hold[m+1].replace(k,1,'\\');
							}
							else
							flag=0;
						}
					}
				}
				if(flag==0)
				cout<<"Case #"<<i+1<<":\nImpossible\n";
				else
				{
					cout<<"Case #"<<i+1<<":\n";
					for(int m=0;m<R;m++)
					{
						cout<<hold[m]<<endl;
					}
				}
				
				
			}
			hold.clear();
	}
	
	return 0;
}
