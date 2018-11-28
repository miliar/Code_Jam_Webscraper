#include <iostream>

using namespace std;

int main()
{
	std::cout.precision(12);
	int T, cs = 1;
	cin>>T;

	while(T--)
	{
		int R, C;
		char design[50][50];
		int flag = 1;
		cin>>R>>C;

		for(int i = 0; i < R; i ++)
		{
			for(int j = 0; j < C; j ++)
			{
				cin>>design[i][j];
			}
		}

		for(int i = 0; i < R - 1; i ++)
		{
			for(int j = 0; j < C - 1; j ++)
			{
				if((design[i][j] == '#') && (design[i][j+1] == '#') && (design[i+1][j] == '#') && (design[i+1][j+1] == '#'))
				{
					design[i][j] = '/';
					design[i+1][j+1] = '/';
					design[i+1][j] = '\\';
					design[i][j+1] = '\\';
				}
			}
		}

		for(int i = 0; i < R; i ++)
		{
			for(int j = 0; j < C; j ++)
			{
				if(design[i][j] == '#')
				{
					flag = 0;
					break;
				}
			}
		}
 
		
		cout<<"Case #"<<cs++<<": "<<endl;
		if(flag)
		{
			for(int i = 0; i < R; i ++)
			{
				for(int j = 0; j < C; j ++)
				{
					cout<<design[i][j];
				}
				cout<<endl;
			}
		}
		else
			cout<<"Impossible"<<endl;
				
	}

	return 0;
}
