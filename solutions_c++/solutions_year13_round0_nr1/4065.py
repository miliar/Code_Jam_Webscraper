#include <iostream>
using namespace std;
int main()
{
	int t,t2,i,j;
	bool won,draw;
	char arr[4][4],temp;
	cin>>t;
	t2=t;
	while(t2--)
	{
		won=false;
		draw=false;
		//input
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>arr[i][j];
				if(arr[i][j]=='.')
					draw=true;
			}
		}
		//input end
		
		
		
		
		//row check		
		for(i=0;i<4;i++)
		{
			temp=arr[i][0];
			if(temp=='T') {
				temp=arr[i][1];
				j=2;
			}
			else {
			j=1;
			}
			
			if(temp=='.')
				continue;
			for(;j<4;j++)
			{
				if(!(arr[i][j]=='T'||arr[i][j]==temp))
					break;
			}
			if(j==4)
			{
				won=true;
				break;
			}
		}		
		if(won==true)
		{
			cout<<"Case #"<<t-t2<<": "<<temp<<" won"<<endl;
			continue;
		}
		
		//column check
		for(i=0;i<4;i++)
		{
			temp=arr[0][i];
			if(temp=='T') {
				temp=arr[1][i];
				j=2;
			}
			else {
			j=1;
			}
			if(temp=='.')
				continue;
			
			for(;j<4;j++)
			{
				if(!(arr[j][i]=='T'||arr[j][i]==temp))
					break;
			}
			if(j==4)
			{
				won=true;
				break;
			}
		}
		
		if(won==true)
		{
			cout<<"Case #"<<t-t2<<": "<<temp<<" won"<<endl;
			continue;
		}
		
		//diagonal1 check
		temp=arr[0][0];
		if(temp=='T') {
			temp=arr[1][1];
			j=2;
		}
		else {
			j=1;
		}
		if(temp!='.')
		{
			for(;j<4;j++)
			{
				if(!(arr[j][j]=='T'||arr[j][j]==temp))
					break;
			}
			if(j==4)
			{
				won=true;
			}
		}
		if(won==true)
		{
			cout<<"Case #"<<t-t2<<": "<<temp<<" won"<<endl;
			continue;
		}
		
		//diagonal2 check
		temp=arr[0][3];
		if(temp=='T') {
			temp=arr[1][2];
			j=2;
		}
		else {
			j=1;
		}
		if(temp!='.')
		{
			for(;j<4;j++)
			{
				if(!(arr[j][3-j]=='T'||arr[j][3-j]==temp))
					break;
			}
			if(j==4)
			{
				won=true;
			}
		}
		if(won==true)
		{
			cout<<"Case #"<<t-t2<<": "<<temp<<" won"<<endl;
			continue;
		}	
		
		
		//draw condition
		if(draw)
			cout<<"Case #"<<t-t2<<": Game has not completed"<<endl;
		else
			cout<<"Case #"<<t-t2<<": Draw"<<endl;
			
		
	}
}
		
		
		
