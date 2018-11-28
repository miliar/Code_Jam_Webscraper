#include<iostream>
#include<string>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int test=1;test<=T;test++)
	{
		int X=0,O=0,D=0,C=0;
		string S[4];
		for(int i=0;i<4;i++)
		{
			cin>>S[i];
		}
		//checking rows
		int x,o,dot,t;
		//cout<<S[0]<<endl;
		for(int i=0;i<4;i++)
		{
			x=0;o=0;dot=0;t=0;
			for(int j=0;j<4;j++)
			{
				if(S[i][j]=='X')x++;
				else if (S[i][j]=='O')o++;
				else if (S[i][j]=='T')t++;
				else dot++;
			}
			if(x+t==4){X=1;break;}
			if(o+t==4){O=1;break;}
			if(dot>0)C=1;//incomplete game- cannot be a draw
			
		}

		//checking columns
		for(int j=0;j<4;j++)
		{
			x=0;o=0;dot=0;t=0;
			for(int i=0;i<4;i++)
			{
				if(S[i][j]=='X')x++;
				else if (S[i][j]=='O')o++;
				else if (S[i][j]=='T')t++;
				else dot++;
			}
			if(x+t==4){X=1;break;}
			if(o+t==4){O=1;break;}
			if(dot>0)C=1;//incomplete game- cannot be a draw
		}
		x=0;o=0;dot=0;t=0;
		//checking diagnal
		for(int i=0;i<4;i++)
		{
			
			if(S[i][i]=='X')x++;
			else if (S[i][i]=='O')o++;
			else if (S[i][i]=='T')t++;
			else dot++;
			
			if(x+t==4){X=1;break;}
			if(o+t==4){O=1;break;}
			if(dot>0)C=1;//incomplete game- cannot be a draw
		}
		x=0;o=0;dot=0;t=0;
		for(int i=0;i<4;i++)
		{
			if(S[i][3-i]=='X')x++;
			else if (S[i][3-i]=='O')o++;
			else if (S[i][3-i]=='T')t++;
			else dot++;
			
			if(x+t==4){X=1;break;}
			if(o+t==4){O=1;break;}
			if(dot>0)C=1;//incomplete game- cannot be a draw
		}

		if(X==1){cout<<"Case #"<<test<<": X won"<<endl;continue;}
		if(O==1){cout<<"Case #"<<test<<": O won"<<endl;continue;}
		if(C==1){cout<<"Case #"<<test<<": Game has not completed"<<endl;continue;}
		cout<<"Case #"<<test<<": Draw"<<endl;
		//char ch;cin>>ch;
		
	}
	return 0;
}

