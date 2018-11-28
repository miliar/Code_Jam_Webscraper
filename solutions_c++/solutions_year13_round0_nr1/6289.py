#include <vector>
#include <iostream>
using namespace std;
char f[17][17] = {0};
bool isClmn(char ch,int j)
{
	for (int i = 0; i < 4; i++)
	{
		if (ch != f[i][j])
			return false;
	}
	return true;
}
bool isRow(char ch,int i)
{
	for (int j = 0; j < 4; j++)
	{
		if (ch != f[i][j])
			return false;
	}
	return true;
}
bool isDig(char ch,int t)
{
	if (t == 1)
	{
		for (int i = 0; i < 4; i++)
			if (ch != f[i][i])
				return false;
	}
	if (t == 2)
	{
		for (int i = 0; i < 4; i++)
			if (ch != f[3 - i][i])
				return false;
	}
	return true;
}
bool isWin(char ch)
{
	int x = -1,y = -1;
	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++)
		{
			if (f[i][j] == 'T'){
				x = i,y = j;
				f[i][j] = ch;
				break;
			}
		}
	}
	bool ans = false;
	for (int i = 0; i < 4; i++)
	{
		if (isRow(ch,i) || isClmn(ch,i)){
			ans = true;
			break;
		}
	}
	if (isDig(ch,1) || isDig(ch,2))
		ans = true;
	if (x != -1)
		f[x][y] = 'T';
	return ans;
}
bool isThereEmptyCell()
{
	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++)
		{
			if (f[i][j] == '.'){
				return true;
			}
		}
	}
	return false;
}
int main()
{
	freopen ("A-large.in","r",stdin);
	freopen ("output1.txt","w",stdout);
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < 4; j++)
			scanf ("%s\n",f[j]);
		if (isWin('X'))
		{
			printf ("Case #%d: X won\n",i + 1);
		}
		else if(isWin('O'))
		{
			printf ("Case #%d: O won\n",i + 1);
		}
		else if(isThereEmptyCell())
		{
			printf ("Case #%d: Game has not completed\n",i + 1);
		}
		else
		{
			printf ("Case #%d: Draw\n",i + 1);
		}
	}

	return 0;
}