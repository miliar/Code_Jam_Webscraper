#include <iostream>

using namespace std;


int main()
{
	int z; cin>>z; 
	for(int ii=1; ii<=z; ii++)
	{
		int t[5][5];
		int lk=0;
		int aa= 4; int b = 4; 
		for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
		{
			char a;
			cin>>a;
			if(a=='T')
				{aa=i; b=j;}
			if(a=='.')
				{t[i][j]=0;
				lk++;}
			if(a=='X')
				t[i][j]=1;
			if(a=='O')
				t[i][j]=2;
		}

		 bool x = false;
		 bool y = false;
		for(int i=0; i<4; i++)
		{
			t[aa][b]=1;
			if(t[i][0] == 1 && t[i][1] ==1 &&  t[i][2] == 1 && t[i][3] == 1)
				x=true;
			if(t[0][i] == 1 && t[1][i] == 1 && t[2][i] == 1 &&t[3][i] == 1)
				x=true;
			if(t[0][0] == 1 && t[1][1] ==1 &&  t[2][2] == 1 && t[3][3] == 1)
				x=true;
			if(t[3][0] == 1 && t[2][1] ==1 &&  t[1][2] == 1 && t[0][3] == 1)
				x=true;
				
			t[aa][b]=2;
			if(t[i][0] == 2 &&  t[i][1] ==  2 && t[i][2] == 2 && t[i][3] == 2)
				y=true;
			if(t[0][i] == 2 && t[1][i] == 2 && t[2][i] == 2 && t[3][i] == 2)
				y=true;
			if(t[0][0] == 2 && t[1][1] == 2 && t[2][2] == 2 && t[3][3] == 2)
				y=true;
			if(t[3][0] == 2 && t[2][1] == 2 && t[1][2] == 2 && t[0][3] == 2)
				y=true;
		}

		cout<<"Case #"<<ii<<": "; 
		 if(x)
		 cout<<"X won";
		 else
		 if(y)
		 cout<<"O won";
		 else
		 if(lk==0)
		 	cout<<"Draw";
		else
		cout<<"Game has not completed";
		 
		 cout<<endl;
	}
	return 0;
}
