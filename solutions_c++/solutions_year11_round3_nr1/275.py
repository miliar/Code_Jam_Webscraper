#include <iostream>
using namespace std;
const int maxn = 51;
char mas[maxn][maxn];
void init()
{
	for (int i = 0 ; i < 51; i++)
		for (int j = 0 ; j < 51; j++)
			mas[i][j] = 0;
}
void func(int test)
{
	init();
	int a, b;
	cin >> a >> b;	
	int count = 0;
	for (int i = 0 ; i < a ; i++)
		for (int j = 0 ; j < b; j++)
		{
			cin >> mas[i][j];
			if (mas[i][j] == '#')
				count++;
		}

	bool flag = true;
	while (count && flag && count % 4 == 0)
	{
		flag = false;
		for (int i = 0 ; i < a - 1 && flag == false; i++)
			for (int j = 0; j < b - 1 && flag == false; j++)
			{
				bool check = true;
				for (int j1 = 0; j1 < 2 && check; j1++)
					for (int i1 = 0 ; i1 < 2 && check; i1++)
						if (mas[i + i1][j + j1] != '#')
							check = false;
				if (check == true)
				{
					mas[i][j] = '/';
					mas[i][j + 1] = '\\';
					mas[i+1][j] = '\\';
					mas[i+1][j+1] ='/';
					flag = true;
					count -= 4;
				}
			}		
	}
	cout <<"Case #" << test <<":\n";
	if (flag == false || count % 4 != 0)
	{
		cout << "Impossible\n";
		return;
	}
	for (int i = 0 ; i < a; i++)
		for (int j = 0; j < b; j++)
			if (j != b-1)
				cout << mas[i][j];
			else
				cout <<mas[i][j] << endl;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	for (int i = 0 ; i < t ; i++)
		func(i +  1);
}