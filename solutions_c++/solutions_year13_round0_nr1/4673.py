#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
bool IsWon(string x[ ],char ch)
{
	vector <int> a(10);
	for(int i=0;i<4;++i)
	{
		for(int j=0;j<4;++j)
		{
			if(x[i][j]==ch)
			{
				++a[i];
				++a[4+j];
				if(i==j)
					++a[8];
				if(i==3-j)
					++a[9];
			}
		}
	}
	if( *max_element(a.begin(),a.end()) !=4)
		return false;
	return true;
}

int main()
{
	int T;
	cin>>T;
	for(int c=0;c<T;++c)
	{
		string x[4],t[4];
		int dotCount=0;
		for(int i=0;i<4;++i)
		{
			cin>>x[i];
			t[i]=x[i];
			if(x[i].find('.')!=string::npos)
				++dotCount;
			size_t pos=x[i].find('T');
			if(pos!=string::npos)
			{
				t[i][pos]='O';
				x[i][pos]='X';
			}
		}
		if(IsWon(x,'X'))
		{
			cout<<"Case #"<<c+1<<": X won\n";
		}
		else if(IsWon(t,'O'))
		{
			cout<<"Case #"<<c+1<<": O won\n";
		}
		else if(dotCount)
		{
			cout<<"Case #"<<c+1<<": Game has not completed\n";
		}
		else
		{
			cout<<"Case #"<<c+1<<": Draw\n";
		}
	}
	return 0;
}