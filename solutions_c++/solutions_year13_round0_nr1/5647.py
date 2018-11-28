#include<iostream>
#include<string>
using namespace std;
struct node
{
	node* right;
	node* left;
	node* ancestor;
	int date;
};

int size;

bool os(char arr[][4])
{
	for (int i = 0; i < 4; i++)
	{
		if(arr[0][i] == 'O')
			if((arr[1][i] == 'O' || arr[1][i] ==  'T') &&
				(arr[2][i] == 'O' || arr[2][i] == 'T') &&
				(arr[3][i] == 'O' || arr[3][i] == 'T'))
				return true;

	}

	for (int i = 0; i < 4; i++)
	{
		if(arr[i][0] == 'O')
			if((arr[i][1] == 'O' || arr[i][1] ==  'T') &&
				(arr[i][2] == 'O' || arr[i][2] == 'T') &&
				(arr[i][3] == 'O' || arr[i][3] == 'T'))
				return true;

	}


	if(arr[0][0] == 'O')
		if((arr[1][1] == 'O' || arr[1][1] ==  'T') &&
			(arr[2][2] == 'O' || arr[2][2] == 'T') &&
			(arr[3][3] == 'O' || arr[3][3] == 'T'))
			return true;

	if(arr[0][3] == 'O')
		if((arr[1][2] == 'O' || arr[1][2] == 'T') &&
			(arr[2][1] == 'O' || arr[2][1] == 'T') &&
			(arr[3][0] == 'O' || arr[3][0] == 'T'))
			return true;


	return false;
}

bool xs(char arr[][4])
{
	for (int i = 0; i < 4; i++)
	{
		if(arr[0][i] == 'X')
			if((arr[1][i] == 'X' || arr[1][i] ==  'T') &&
				(arr[2][i] == 'X' || arr[2][i] == 'T') &&
				(arr[3][i] == 'X' || arr[3][i] == 'T'))
				return true;

	}

	for (int i = 0; i < 4; i++)
	{
		if(arr[i][0] == 'X')
			if((arr[i][1] == 'X' || arr[i][1] ==  'T') &&
				(arr[i][2] == 'X' || arr[i][2] == 'T') &&
				(arr[i][3] == 'X' || arr[i][3] == 'T'))
				return true;

	}


	if(arr[0][0] == 'X')
		if((arr[1][1] == 'X' || arr[1][1] ==  'T') &&
			(arr[2][2] == 'X' || arr[2][2] == 'T') &&
			(arr[3][3] == 'X' || arr[3][3] == 'T'))
			return true;

	if(arr[0][3] == 'X')
		if((arr[1][2] == 'X' || arr[1][2] == 'T') &&
			(arr[2][1] == 'X' || arr[2][1] == 'T') &&
			(arr[3][0] == 'X' || arr[3][0] == 'T'))
			return true;


	return false;
}


bool completed(char arr[][4])
{
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if(arr[i][j] == '.')
				return false;
		}
	}
	return true;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	char arr[4][4];
	string str;
	int t;
	cin >> t;
	cin.ignore();
	for (int i = 0; i < t; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			getline(cin, str);
			for (int k = 0; k < 4; k++)
			{
				arr[j][k] = str[k];
			}
		}
		cout << "Case #" << i+1 << ": ";
		if(os(arr))
			cout << "O won" << endl;
		else if(xs(arr))
		{
			cout << "X won" << endl;
		}
		else
		{
			if(!completed(arr))
				cout << "Game has not completed" << endl;
			else
				cout << "Draw" << endl;
		}
		getline(cin, str);
	}
}
