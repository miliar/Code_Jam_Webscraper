#include <iostream>
#include <vector>

using namespace std;

bool isIn(char* ar, char a)
{
	for(int i=0;i<4;i++)
	{
		if(ar[i] == a)
			return true;
	}
	return false;
}

int getStatus(char* m)
{
	bool t = isIn(m, 'T');
	bool x = isIn(m, 'X');
	bool o = isIn(m, 'O');
	bool dot = isIn(m, '.');

	if((t || x) && (!dot && !o))
		return 1;
	if((t || o) && (!dot && !x))
		return 2;
	if(dot)
		return 3;
	return 4;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n = 0;
	cin >> n;

	char (*fields)[4][4];
	fields = new char[n][4][4];
	bool* hasDot = new bool[n];

	for(int i=0;i<n;i++)
	{
		hasDot[i] = false;
		for(int j=0;j<4;j++)
		{
			for (int k=0;k<4;k++)
			{
				cin >> fields[i][j][k];
				if(!hasDot[i] && fields[i][j][k] == '.')
					hasDot[i] = true;
			}
		}
	}

	for(int i=0;i<n;i++)
	{
		bool done = false;
		for (int j=0;j<4;j++)
		{
			int tmp;
			tmp = getStatus(fields[i][j]);
			if (tmp == 1)
			{
				cout << "Case #" << i+1 << ": X won" << endl;
				done = true;
				break;
			}
			if (tmp == 2)
			{
				cout << "Case #" << i+1 << ": O won" << endl;
				done = true;
				break;
			}
		}
		if(done) continue;
		for (int j=0;j<4;j++)
		{
			char temp[4] = {fields[i][0][j], fields[i][1][j], fields[i][2][j], fields[i][3][j]};
			int tmp;
			tmp = getStatus(temp);
			if (tmp == 1)
			{
				cout << "Case #" << i+1 << ": X won" << endl;
				done = true;
				break;
			}
			if (tmp == 2)
			{
				cout << "Case #" << i+1 << ": O won" << endl;
				done = true;
				break;
			}
		}
		if(done) continue;
		char diag1[4] = {fields[i][0][0], fields[i][1][1], fields[i][2][2], fields[i][3][3]};
		int tmp;
		tmp = getStatus(diag1);
		if (tmp == 1)
		{
			cout << "Case #" << i+1 << ": X won" << endl;
			done = true;
		}
		if(done) continue;
		if (tmp == 2)
		{
			cout << "Case #" << i+1 << ": O won" << endl;
			done = true;
		}
		if(done) continue;
		char diag2[4] = {fields[i][0][3], fields[i][1][2], fields[i][2][1], fields[i][3][0]};
		tmp = getStatus(diag2);
		if (tmp == 1)
		{
			cout << "Case #" << i+1 << ": X won" << endl;
			done = true;
		}
		if(done) continue;
		if (tmp == 2)
		{
			cout << "Case #" << i+1 << ": O won" << endl;
			done = true;
		}
		if(done) continue;
		if (hasDot[i])
		{
			cout << "Case #" << i+1 << ": Game has not completed" << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": Draw" << endl;
		}
	}

	delete [] fields;
	delete [] hasDot;
	return 0;
}