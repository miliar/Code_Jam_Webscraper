#include<iostream>
using namespace std;
int main()
{
	int x,o,t;
	int flag=0;
	bool uc=false;
	//bool w=false;
	char array[4][4];
	//input
	int test;
	cin>>test;
	int c=0;
	while(test--)
	{
		flag=0;
		uc=false;
		//w=false;
		
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>array[i][j];
			}
		}	
		//cout<<array[3][3]<<endl;
	
		//row
		for(int i=0;i<4;i++)
		{
			x=0;
			o=0;
			t=0;
			for(int j=0;j<4;j++)
			{
				x+=(array[i][j]=='X')?1:0;
				o+=(array[i][j]=='O')?1:0;
				t+=(array[i][j]=='T')?1:0;
				if(array[i][j]=='.')
					uc=true;
			}
			if(x+t==4)
			{
				cout<<"Case #"<<(c+1)<<": X won"<<endl;
				//w=true;
				flag=1;
				break;
			}
			if(o+t==4)
			{
				cout<<"Case #"<<(c+1)<<": O won"<<endl;
				//w=true;
				flag=1;
				break;
			}
			
		}
			
	
		//column
		for(int i=0; i<4 && flag!=1 ;i++)
		{
			x=0;
			o=0;
			t=0;
			for(int j=0;j<4;j++)
			{
				x+=(array[j][i]=='X')?1:0;
				o+=(array[j][i]=='O')?1:0;
				t+=(array[j][i]=='T')?1:0;
			}
			if(x+t==4)
			{
				cout<<"Case #"<<(c+1)<<": X won"<<endl;
				//w=true;
				flag=1;
				break;
			}
			if(o+t==4)
			{
				cout<<"Case #"<<(c+1)<<": O won"<<endl;
				//w=true;
				flag=1;
				break;
			}
			
		}
			
			
		//first diagonal
			x=0;
			o=0;
			t=0;
			for(int j=0;j<4 && flag!=1;j++)
			{
				x+=(array[j][j]=='X')?1:0;
				o+=(array[j][j]=='O')?1:0;
				t+=(array[j][j]=='T')?1:0;
			}
			if(x+t==4)
			{
				cout<<"Case #"<<(c+1)<<": X won"<<endl;
				//w=true;
				flag=1;
				//break;
			}
			if(o+t==4)
			{
				cout<<"Case #"<<(c+1)<<": O won"<<endl;
				//w=true;
				flag=1;
				//break;
			}
			
		//second diagonal
			x=0;
			o=0;
			t=0;
			for(int j=0;j<4 && flag!=1;j++)
			{
				x+=(array[j][3-j]=='X')?1:0;
				o+=(array[j][3-j]=='O')?1:0;
				t+=(array[j][3-j]=='T')?1:0;
			}
			if(x+t==4)
			{
				cout<<"Case #"<<(c+1)<<": X won"<<endl;
				//w=true;
				flag=1;
				//break;
			}
			if(o+t==4)
			{
				cout<<"Case #"<<(c+1)<<": O won"<<endl;
				//w=true;
				flag=1;
				//break;
			}
			
			//no one won
			if(uc && flag!=1)
			{
				cout<<"Case #"<<(c+1)<<": Game has not completed"<<endl;
				flag=1;
			}
			
			if(flag!=1)
				cout<<"Case #"<<(c+1)<<": Draw"<<endl;
	
	c++;
	
	}	  //end of while loop of test cases
	return 0;
}
