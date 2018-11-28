#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;
int main()
{
	ifstream cin;
	ofstream cout;
	cin.open("A-large.in");
	cout.open("outputprob1.txt");
	int t;
	cin>>t;
	string temp;
	for(int i=0;i<t;i++)
	{
		vector<string> s;
		for(int j=0;j<4;j++)
		{
			cin>>temp;
			s.push_back(temp);
			//cout<<temp<<endl;
		}
		//if(i!=t-1) cin>>temp;
		string result;
		char c;
		bool finished = 0;
		for(int j=0;j<4 && !finished;j++) //checking rows
		{
			c = s[j][0];
			if(c=='T') c=s[j][1];
			if(c == 'O') result = "O won";
			else if (c== 'X') result = "X won";
			else continue;
			finished = 1;
			for(int k=1;k<4;k++)
			{
				if(!(s[j][k] == c || s[j][k] == 'T'))
				{
					finished = 0;
					break;
				}
			}
		}
		if(!finished)
		{
			for(int j=0;j<4 && !finished;j++) //checking columns
				{
					c = s[0][j];
					if(c=='T') c=s[1][j];
					if(c == 'O') result = "O won";
					else if (c== 'X') result = "X won";
					else continue;
					finished = 1;
					for(int k=1;k<4;k++)
					{
						if(!(s[k][j] == c || s[k][j] == 'T'))
						{
							finished = 0;
							break;
						}
					}
				}
		}
		if(!finished)
		{
			c = s[0][0];
			bool exec = true;
			if(c == 'T') c = s[1][1];
			if(c == 'O') result = "O won";
			else if (c== 'X') result = "X won";
			else exec = false;
			if(exec){
			finished = 1;
			for(int j=1;j<4;j++)
			{
				if(!(s[j][j] == c || s[j][j] == 'T'))
				{
					finished = 0;
					break;
				}
			}
			}
		}
		if(!finished)
		{
			c = s[0][3];
			bool exec = true;
			if(c == 'T') c = s[1][2];
			if(c == 'O') result = "O won";
			else if (c== 'X') result = "X won";
			else exec = false;
			if(exec){
			finished = 1;
			for(int j=0;j<4;j++)
			{
				if(!(s[j][3-j] == c || s[j][3-j] == 'T'))
				{
					finished = 0;
					break;
				}
			}
			}
		}
		if(!finished)
		{
			finished = 1;
			result = "Draw";
			for(int j=0;j<4;j++)
				for(int k=0;k<4;k++)
					if(s[j][k]=='.')
						{
							finished = 0;
							break;
						}
		}
		if(!finished) result = "Game has not completed";
		cout<<"Case #"<<i+1<<": "<<result<<endl;
	}
}
