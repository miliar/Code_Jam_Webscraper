#include<iostream>
#include<string.h>
using namespace std;

int main()
{
	freopen("F:\\download\\1.txt", "r", stdin);
	freopen("F:\\download\\1out.txt", "w", stdout);

	int T;
	cin>>T;
	int arr[4][4];
	char p;
	int id = 1;
	while(T--)
	{
		bool flag = true;
		memset(arr, 0, sizeof(arr));
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
			{
				cin>>p;
				if(p == 'O')
					arr[i][j] = 1;
				else if(p == 'X')
					arr[i][j] = 10;
				else if(p == 'T')
					arr[i][j] = 5;
				else if(p == '.')
					flag = false;
			}

		bool f = false;
		for(int i = 0; i < 4 && (!f); ++i)
		{
			int a1 = 0, a2 = 0, a3 = 0, a4 = 0;
			for(int j = 0; j < 4; ++j)
			{
				a1 += arr[i][j];
				a2 += arr[j][i];
				a3 += arr[j][j];
				a4 += arr[j][3-j];
			}
			if(a1 == 4 || a2 == 4 || a1 == 8 || a2 == 8 || a3 ==4 || a3 == 8 || a4 == 4||a4 ==8)
			{
				f = true;
				p = 'O';
			}
			else if(a1 == 40 || a2 == 40 || a1 == 35 || a2 == 35||a3==40|a3==35||a4==40||a4==35)
			{
				f = true;
				p = 'X';
			}
		
		
		}
		if(f)
		{
			cout<<"Case #"<<id<<": "<<p<<" won"<<endl;	
		}
		else if(flag)
		{
			cout<<"Case #"<<id<<": Draw"<<endl;
		}
		else
		{
			cout<<"Case #"<<id<<": Game has not completed"<<endl;
		}

		id++;	
		
	}
	return 0;
}