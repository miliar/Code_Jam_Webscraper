#include<iostream>
#include<string>
#include<vector>
using namespace std;
int main()
{
	int T;cin >> T;
	cin.clear();cin.ignore(1,'\n');
	vector<string>S;
	int c;string temp;
	for(c=1;c<=T;c++)
	{
		getline(cin,temp);
		S.push_back(temp);cin.clear();cin.ignore(0,'\n');
		getline(cin,temp);
		S.push_back(temp);cin.clear();cin.ignore(0,'\n');
		getline(cin,temp);
		S.push_back(temp);cin.clear();cin.ignore(0,'\n');
		getline(cin,temp);
		S.push_back(temp);cin.clear();cin.ignore(0,'\n');
		getline(cin,temp);
		cin.clear();cin.ignore(0,'\n');
		bool X=false; bool O=false;
		int dot=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(S[i].at(j)=='.')
					dot++;
			}
			//cout<<endl;
			if( (S[i].at(0)=='X'||S[i].at(0)=='T')&&(S[i].at(1)=='X'||S[i].at(1)=='T')&&(S[i].at(2)=='X'||S[i].at(2)=='T')&&(S[i].at(3)=='X'||S[i].at(3)=='T'))
			{	X=true; break; }
			if( (S[i].at(0)=='O'||S[i].at(0)=='T')&&(S[i].at(1)=='O'||S[i].at(1)=='T')&&(S[i].at(2)=='O'||S[i].at(2)=='T')&&(S[i].at(3)=='O'||S[i].at(3)=='T'))
			{	O=true; break; }
		}
		if(X==false && O==false)
		{
			for(int i=0; i<4;i++)
			{
				if((S[0].at(i)=='X'||S[0].at(i)=='T')&&(S[1].at(i)=='X'||S[1].at(i)=='T')&&(S[2].at(i)=='X'||S[2].at(i)=='T')&&(S[3].at(i)=='X'||S[3].at(i)=='T'))
				{ X=true;break; }
				if((S[0].at(i)=='O'||S[0].at(i)=='T')&&(S[1].at(i)=='O'||S[1].at(i)=='T')&&(S[2].at(i)=='O'||S[2].at(i)=='T')&&(S[3].at(i)=='O'||S[3].at(i)=='T'))
				{ O=true;break;}
			}
		}
		if(X==false && O==false)
		{
			if((S[0].at(0)=='X'||S[0].at(0)=='T')&&(S[1].at(1)=='X'||S[1].at(1)=='T')&&(S[2].at(2)=='X'||S[2].at(2)=='T')&&(S[3].at(3)=='X'||S[3].at(3)=='T'))
			{ X=true; }
			else if((S[0].at(0)=='O'||S[0].at(0)=='T')&&(S[1].at(1)=='O'||S[1].at(1)=='T')&&(S[2].at(2)=='O'||S[2].at(2)=='T')&&(S[3].at(3)=='O'||S[3].at(3)=='T'))
			{ O=true; }
		}
		if(X==false && O==false)
		{
			//if( (S[0].at(3)=='X'||S[0].at(3)=='T')&&(S[1].at(2)=='X'||S[1].at(2)=='T')(S[2].at(1)=='X'||S[2].at(1)=='T')(S[3].at(0)=='X'||S[3].at(0)=='T') )
			if((S[0].at(3)=='X' || S[0].at(3)=='T')&&(S[1].at(2)=='X' ||S[1].at(2)=='T')&&(S[2].at(1)=='X'||S[2].at(1)=='T')&&(S[3].at(0)=='X' || S[3].at(0)=='T'))
			{ X=true;}
			else if((S[0].at(3)=='O'||S[0].at(3)=='T')&&(S[1].at(2)=='O'||S[1].at(2)=='T')&&(S[2].at(1)=='O'||S[2].at(1)=='T')&&(S[3].at(0)=='O'||S[3].at(0)=='T'))
			{O=true;}
		}
		if(X==true)
			cout<<"Case #"<<c<<": "<<"X won"<<endl;
		else if(O==true)
			cout<<"Case #"<<c<<": "<<"O won"<<endl;
		else
		{
			if(dot>=2)
				cout<<"Case #"<<c<<": "<<"Game has not completed"<<endl;
			else
				cout<<"Case #"<<c<<": "<<"Draw"<<endl;
		}
		S.clear();
	}
	return 0;
}