#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
	int nt;
	cin>>nt;
	for(int i=0;i<nt;i++)
	{
		
		int N,L,H;
		cin>>N>>L>>H;
		vector<int> hold;
		for(int m=0;m<N;m++)
		{
			int temp;
			cin>>temp;
			hold.push_back(temp);
		}
		int printed=0;
		for(int j=L;j<=H;j++)
		{
			int flag=1;
			for(int k=0;k<N&&flag;k++)
			{
				if(hold[k]<j)
				{
					if(j%hold[k]!=0)
					flag=0;
				}
				else
				{
					if(hold[k]%j!=0)
					flag=0;
				}
			}
			if(flag)
			{
			cout<<"Case #"<<i+1<<": "<<j<<endl;
			printed=1;
			break;
			}
			
		}
		if(printed!=1)
		cout<<"Case #"<<i+1<<": NO"<<endl;
		hold.clear();
	}
	
	return 0;
}
