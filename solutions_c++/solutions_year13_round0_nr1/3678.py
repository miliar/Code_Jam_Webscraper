#include <iostream>
using namespace std;

int a[5][5];
int b[5][5];
char ch[5][5];

void set_game(int b)
{
	int i,j;
	for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
			if(ch[i][j]=='.')
				a[i][j]= not b;
			else if(ch[i][j]=='T')
				a[i][j]= b;
}

bool check0()
{
	int i,j;
	bool flag1,flag2,flag3,flag4;
	for(i=1;i<=4;i++)
	{
		flag1=flag2=0;
		for(j=1;j<=4;j++)
		{
			flag1=flag1 or a[i][j];
			flag2=flag2 or a[j][i];
		}
		if((!(flag1)) || (!(flag2)))
			return true;
	}
	flag3 = a[1][1] or a[2][2] or a[3][3] or a[4][4];
	flag4 = a[1][4] or a[2][3] or a[3][2] or a[4][1];
	if((!(flag3)) || (!(flag4)))
			return true;
	return false;
}

bool check1()
{
	int i,j;
	bool flag1,flag2,flag3,flag4;
	for(i=1;i<=4;i++)
	{
		flag1=flag2=1;
		for(j=1;j<=4;j++)
		{
			flag1=flag1 and a[i][j];
			flag2=flag2 and a[j][i];
		}
		if((flag1) || (flag2))
			return true;
	}
	flag3 = a[1][1] and a[2][2] and a[3][3] and a[4][4];
	flag4 = a[1][4] and a[2][3] and a[3][2] and a[4][1];
	if((flag3) || (flag4))
			return true;
	return false;
}

int main()
{
	int z,t,i,j,ti,tj;
	cin >> t;
	for(z=1;z<=t;z++)
	{
		bool flag = 0;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
			{
				cin >> ch[i][j];
				if(ch[i][j]=='X')
					a[i][j]=1;
				else if(ch[i][j]=='O')
					a[i][j]=0;
				else if(ch[i][j]=='.')
					flag=1;
			}
		set_game(0);
		if(check0())
		{
			cout << "Case #" << z << ": O won" << endl;
			continue;
		}
		set_game(1);
		if(check1())
		{
			cout << "Case #" << z << ": X won" << endl;
			continue;
		}
		if(flag)
			cout << "Case #" << z << ": Game has not completed" << endl;
		else
			cout << "Case #" << z << ": Draw" << endl;
	}
	return 0;
}
