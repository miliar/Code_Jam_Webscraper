#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	int T;
	cin>>T;
	char square[4][4]={0};
	//int caseno = 1;
	for(int caseno=1;caseno<=T;++caseno)
	{
		for(int i=0;i<4;++i)
		{
			for(int j=0;j<4;++j)
			{
				cin>>square[i][j];
			}
		}
		cout<<"Case #"<<caseno<<": ";
		int xrowresult[4] = {0};
		int xcolresult[4] = {0};
		int xdiaresult[2] = {0};
		int orowresult[4] = {0};
		int ocolresult[4] = {0};
		int odiaresult[2] = {0};
		int count = 0;
		for(int i=0;i<4;++i)
		{
			for(int j=0;j<4;++j)
			{
				if(square[i][j]=='X')
				{
					++xrowresult[i];
					++xcolresult[j];
				}
				else if(square[i][j]=='O')
				{
					++orowresult[i];
					++ocolresult[j];
				}
				else if(square[i][j]=='T')
				{
					++xrowresult[i];
					++xcolresult[j];
					++orowresult[i];
					++ocolresult[j];
				}
				else
				{
					++count;
				}
			}
		}
		for(int i=0,j=0;i<4,j<4;++i,++j)
		{
			if(square[i][j]=='X')
			{
				++xdiaresult[0];	
			}
			else if(square[i][j]=='O')
			{
				++odiaresult[0];	
			}
			else if(square[i][j]=='T')
			{
				++xdiaresult[0];
				++odiaresult[0];
			}
		}
		for(int i=0,j=3;i<4,j>=0;++i,--j)
		{
			if(square[i][j]=='X')
			{
				++xdiaresult[1];	
			}
			else if(square[i][j]=='O')
			{
				++odiaresult[1];	
			}
			else if(square[i][j]=='T')
			{
				++xdiaresult[1];
				++odiaresult[1];
			}
		}
		bool anyonewon = false;
		for(int i=0;i<4;++i)
		{
			if(xrowresult[i]==4||xcolresult[i]==4||(xdiaresult[i]==4&&i<2))
			{
				cout<<"X won"<<endl;
				anyonewon = true;
				break;
			}
			if(orowresult[i]==4||ocolresult[i]==4||(odiaresult[i]==4&&i<2))
			{			
				cout<<"O won"<<endl;
				anyonewon = true;
				break;
			}
		}
		if((anyonewon==false)&&count>0)
		{
			cout<<"Game has not completed"<<endl;
		}
		if((anyonewon==false)&&count==0)
		{
			cout<<"Draw"<<endl;
		}
	}
	return 0;
}
