# include<iostream>
# include<fstream>
using namespace std;
void check(char a[][4], int k, fstream &f)
{
	char temp;
	for(int i = 0; i < 4; i++)
	{
		temp = a[i][0];
		if(temp =='.')
		{
			continue;
		}
		for(int j = 0; j < 4; j++)
		{
			if(a[i][j] == temp || a[i][j] == 'T')
			{
				if(j == 3)
				{
					f << "Case #" << k << ": " << temp << " " << "won" << endl;
					return;
				}
				continue;
			}
			else
			{
				break;	
			}
		}
	}
	for(int i = 0; i < 4; i++)
	{
		temp = a[0][i];
		if(temp =='.')
		{
			continue;
		}
		for(int j = 0; j < 4; j++)
		{
			if(a[j][i] == temp || a[j][i] == 'T')
			{
				if(j == 3)
				{
					f << "Case #" << k << ": " << temp << " " << "won" << endl;
					return;
				}
				continue;
			}
			else
			{
				break;	
			}
		}
	}
	temp = a[0][0];
	for(int i = 0; i < 4; i++)
	{
		if(temp =='.')
		{
			continue;
		}
		if(a[i][i] == temp || a[i][i] == 'T')
		{
			if(i == 3)
			{
				f << "Case #" << k << ": " << temp << " " << "won" << endl;
				return;
			}
			continue;
		}
		else
		{
			break;	
		}	
	}
	temp = a[0][3];
	for(int i = 0; i < 4; i++)
	{
		if(temp =='.')
		{
			continue;
		}
		if(a[i][3-i] == temp || a[i][3-i] == 'T')
		{
			if(i == 3)
			{
				f << "Case #" << k << ": " << temp << " " << "won" << endl;
				return;
			}
			continue;
		}
		else
		{
			break;	
		}	
	}
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			if(a[i][j] == '.')
			{
				f << "Case #" << k << ": " << "Game has not completed" << endl;
				return;
			}
		}
	}
	f << "Case #" << k << ": " << "Draw" << endl;
};
int main()
{
	int k, zz = 1;
	fstream file1("OUTPUT.TXT",ios::in | ios::out);
	fstream file("A-small-attempt1.in",ios::in | ios::out);
	file >> k;
	while(k > 0)
	{	
		char z[4][4];
		for(int i =0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				file >> z[i][j];
			}
		}
		check(z, zz, file1);
		/*for(int i =0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				cout << z[i][j];
			}
		}*/
		k--;
		zz++;
	}
	file.close();
}
