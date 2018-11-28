#include<iostream>
using namespace std;
void main()
{
	char field[50][50];
	char result[50][50];
	int numsR[50];
	int numsC[50];
	int numTests = 0;
	cin>>numTests;
	int R, C;
	bool flag = true;
	for(int t = 0; t < numTests; ++t)
	{
		flag = true;
		cin>>R;
		cin>>C;
		int tmp;
		int s = 0;
		s = 0;
		for(int i = 0; i < R; ++i)
		{
			numsR[i] = 0;
			for(int j = 0; j < C; ++j)
			{
				cin>>field[i][j];
				result[i][j] = ' ';
				if(field[i][j] == '#'){ ++numsR[i]; ++s;}
			}
		}
		for(int j = 0; j < C; ++j)
		{
			numsC[j] = 0;
			for(int i = 0; i <R; ++i)
				if(field[i][j] == '#') ++numsC[j];
		}
		for(int i = 0; i < R; ++i)
		{ 
			if(numsR[i] % 2 != 0 )
			{
				flag = false;
				cout<<"Case #"<<t+1<<":"<<endl;
				cout<<"Impossible"<<endl;
				break;
			}

		}
		if(flag == true)
		for(int j = 0; j < C; ++j)
		{ 
			if(numsC[j] % 2 != 0 )
			{
				flag = false;
				cout<<"Case #"<<t + 1<<":"<<endl;
				cout<<"Impossible"<<endl;
				break;
			}
		}
		if(flag == true)
		{
			int td;
			int tr = 0;
			char last = '.';
			cout<<"Case #"<<t+1<<":"<<endl;
			for(int i = 0; i < (R -1); ++i)
				for(int j = 0; j < (C - 1); ++j)
				if(field[i][j] == '#') 
				{
					if(result[i][j] == ' ')
					{
					if(field[i][j] == '#' && field[i+1][j] == '#' && field[i][j+1] == '#'  && field[i+1][j+1] == '#')
					{
						if((i==0) || ( result[i][j - 1] == '/')||(j%2==0)||(field[i - 1][j] == '.'))
						{
							{
							result[i][j] = '/';
							result[i][j+1] = '\\';
							result[i+1][j] = '\\';
							result[i+1][j+1] = '/';
							}
						}
						else
						{
							if( (j == 0)|| (result[i - 1][j] =='\\') || (i %2 == 0))
							{
							result[i][j] = '/';
							result[i][j+1] = '\\';
							result[i+1][j] = '\\';
							result[i+1][j+1] = '/';
							}
							else
							{
							result[i][j] = '\\';
							result[i][j+1] = '/';
							result[i+1][j] = '/';
							result[i+1][j+1] = '\\';
							}
						}

					}
					}
				}
				else
				{
					result[i][j] = '.';
				}

			for(int j = 0; j < C; ++j)
				if(result[R-1][j] ==' ')
					result[R -1][j] = '.';
			for(int i = 0;i < R; ++i )
				if(result[i][C - 1] ==' ')
					result[i][C-1] = '.';
		for(int i = 0; i < R; ++i)
		{
			for(int j = 0; j < C; ++j)
				cout<<result[i][j];
			if((t == (numTests - 1))&&(i == R - 1))
			{
			}
			else
			{
				cout<<endl;
			}
		}


		}
	}
}