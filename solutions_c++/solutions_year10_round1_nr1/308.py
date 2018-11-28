#include <string>
#include <vector>
#include <fstream>
#include <iostream>

using namespace std;

int n, k;
vector<string> board;
vector<string> nextB;


bool CheckV(char p)
{
	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++)
			if(nextB[i][j] == p)
			{
				int cnt = 0;
				for(int d = 0; i + d < n && nextB[i + d][j] == p; d++)
					cnt++;
				if(cnt == k)
					return true;
			}
	return false;
}
bool CheckH(char p)
{
	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++)
			if(nextB[i][j] == p)
			{
				int cnt = 0;
				for(int d = 0; j + d < n && nextB[i][j + d] == p; d++)
					cnt++;
				if(cnt == k)
					return true;
			}
	return false;
}
bool CheckD(char p)
{
	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++)
			if(nextB[i][j] == p)
			{
				int cnt = 0;
				for(int d = 0; i + d < n && j + d < n && nextB[i + d][j + d] == p; d++)
					cnt++;
				if(cnt == k)
					return true;
				cnt = 0;
				for(int d = 0; i + d < n && j - d >= 0 && nextB[i + d][j - d] == p; d++)
					cnt++;
				if(cnt == k)
					return true;
			}
	return false;
}


void MakeGra()
{
	for(int i = n - 2; i >= 0; i--)
	{
		for(int j = 0; j < n; j++)
		{
			if(nextB[i + 1][j] == '.')
			{
				int k = i + 1;
				while(k < n && nextB[k][j] == '.')
					k++;
				swap(nextB[i][j], nextB[k - 1][j]);
			}
		}
	}
}

string Check()
{
	nextB = vector<string>(n, string(n, ' '));
	for(int i = 0; i < n; i++)
	{		
		for(int j = 0; j < n; j++)
			nextB[i][n - j - 1] = board[j][i];
	}
	MakeGra();
	int red = CheckV('R') || CheckH('R') || CheckD('R');
	int blue = CheckV('B') || CheckH('B') || CheckD('B');

	if(red && !blue)
		return "Red";
	if(!red && blue)
		return "Blue";
	if(red && blue)
		return "Both";
	return "Neither";

}

int main()
{
	int tests;
	ifstream in("in.txt");
	in >> tests;
	for(int test = 1; test <= tests; test++)
	{
		in >> n >> k;
		board.resize(n);
		for(int i = 0; i < n; i++)
			in >> board[i];
		cout << "Case #" << test << ": " << Check() << endl;
	}
	return 0;
}
