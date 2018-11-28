#include <iostream>
#include <string>
#include <Cmath>
#include <algorithm>
#include <sstream>
#include <fstream>

using namespace std;

int main()
{
	ofstream output;
	output.open ("output.in");
	int i, n;
	string baris[4]={};
	char out;
	cin >> n;
	
	for (i = 0; i < n;i++)
	{
		int T[10]={0}, X[10]={0},O[10]={0};
		bool isWin=false, isDot=false;
		for ( int j=0; j<4; j++)
		{
			cin >> baris[j];
		}
	
		for ( int j=0; j<4; j++)
		{
			for (int k=0; k< 4; k++)
			{
				if (baris[j][k] == 'X') X[j]++;
				if (baris[k][j] == 'X') X[j+4]++;
				if (baris[j][k] == 'O') O[j]++;
				if (baris[k][j] == 'O') O[j+4]++;
				if (baris[j][k] == 'T') T[j]++;
				if (baris[k][j] == 'T') T[j+4]++;
				if (baris[j][k] == '.') isDot = true;
			}
						
			if (baris[j][j] == 'X') X[8]++;
			if (baris[j][j] == 'O') O[8]++;
			if (baris[j][j] == 'T') T[8]++;
			if (baris[3-j][j] == 'X') X[9]++;
			if (baris[3-j][j] == 'O') O[9]++;
			if (baris[3-j][j] == 'T') T[9]++;
		}
		
		for (int j=0; j< 10; j++)
		{
			if (X[j] ==4 || (X[j]==3&&T[j]==1)) 
			{
				out = 'X';
				isWin = true;
				break;
			}
			if (O[j] ==4 || (O[j]==3&&T[j]==1)) 
			{
				out = 'O';
				isWin = true;
				break;
			}
			//cout << X[j] <<" " << O[j]<< " "<< T[j]<< endl;
		}
		
		if (isWin) output << "Case #"<<i+1<<": "<<out<<" won"<< endl;
		else if (isDot) output << "Case #"<<i+1<<": "<<"Game has not completed"<< endl;
		else output << "Case #"<<i+1<<": "<<"Draw"<< endl;
	}
	output.close();
	return 0;
}