#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main()
{
	int T=0;
	cin>>T;

	for (int t=0;t<T;t++)
	{
		int r,c;
		cin>>r>>c;

		string frame[r];

		for (int i=0;i<r;i++)
		{
			cin>>frame[i];
		}
		
		bool failed = false;
		
		for (int i=0;i<r;i++)
		{
			for (int j=0;j<c;j++)
			{
				if (frame[i][j]=='#')
				{
					frame[i][j]='/';
					if (j<c-1 && frame[i][j+1]=='#') frame[i][j+1]='\\';
					else 
					{
						failed = true;
						break;
					}

					if (i<r-1 && frame[i+1][j]=='#') frame[i+1][j]='\\';
					else 
					{
						failed = true;
						break;
					}	
					
					if (frame[i+1][j+1]=='#')frame[i+1][j+1]='/';
					else 
					{
						failed = true;
						break;
					}
				}
			}
			if (failed) break;
		}
		
		cout<<"Case #"<<t+1<<":"<<endl;
		if (failed)
		{
			cout<<"Impossible"<<endl;
		}
		else
		{
			for (int i=0;i<r;i++)
			{
				cout<<frame[i].c_str()<<endl;
			}
		}
		
	}//t for ends
}

