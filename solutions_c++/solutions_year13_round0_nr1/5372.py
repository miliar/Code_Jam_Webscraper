#include<iostream>
using namespace std;
int main()
{
	int t,i,j,num=1,n=4;
	char checkWith;
	bool fwd_diagonalCheck, bck_diagonalCheck,outcome,dotsExist;
	char board[5][5];
	cin>>t;
	while(num<=t)
	{
		dotsExist = false;
		fwd_diagonalCheck = true;
		bck_diagonalCheck = true;
		outcome = false;
		i=0;
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				cin>>board[i][j];
				if(board[i][j] == '.')
					dotsExist = true;
				if(i == j)
				{
					if(board[i][j] == '.')
					fwd_diagonalCheck = false;
				}
				if(i+j == 3)
				{
					if(board[i][j] == '.')
					bck_diagonalCheck = false;
				}
			}
		}
		//check the diagonals.
		if(fwd_diagonalCheck == true)
		{
			i=j=0;
			outcome = true;
			checkWith = board[i][j];
			while(i<=3)
			{
				if(checkWith != board[i][j] && board[i][j]!='T')
				{
					outcome = false;
					break;
				}
				else
				{
					i++;
					j++;
				}
			}
			if(outcome == true && checkWith!='.')
			{
				//cout<<"fwd\n";
				cout<<"Case #"<<num<<": "<<checkWith<<" won"<<endl;
				num++;
				continue;
			}
		}
		if(bck_diagonalCheck == true)			// check back diagonal.
		{
				i=0;
				j=3;
				outcome = true;
				checkWith = board[i][j];
				while(i<=3)
				{
					if(checkWith != board[i][j] && board[i][j]!='T')
					{
						outcome = false;
						break;
					}
					else
					{
						i++;
						j--;
					}
				}
				if(outcome == true && checkWith!='.')
				{
					//cout<<"bck\n";
					cout<<"Case #"<<num<<": "<<checkWith<<" won"<<endl;
					num++;
					continue;
				}
		}
			//check the rows
			i=0;
			while(i<n)
			{
				while(board[i][0] == '.' && i<n)
					i++;
				outcome= true;
				checkWith = board[i][0];
				for(j=0;j<n;j++)
				{
					if(checkWith != board[i][j] && board[i][j]!='T')
					{
						outcome = false;
						break;
					}
				}
				if(outcome == true)
				break;
				i++;
			}
			if(outcome == true)
			{
				//cout<<"Row i ::\n ";
				cout<<"Case #"<<num<<": "<<checkWith<<" won"<<endl;
				num++;
				continue;
			}
			//check columns.
			i=0;
			while(i<n)
			{
				while(board[0][i] == '.' && i<n)
					i++;
				outcome = true;
				checkWith = board[0][i];
				for(j=0;j<n;j++)
				{
					if(checkWith != board[j][i] && board[j][i]!='T')
					{
						outcome = false;
						break;
					}
				}
				if(outcome == true)
				break;
				i++;
			}
			if(outcome == true)
			{
				//cout<<"Column i \n";
				cout<<"Case #"<<num<<": "<<checkWith<<" won"<<endl;
				num++;
				continue;
			}
			if(outcome == false && dotsExist == true)
			{
				cout<<"Case #"<<num<<": Game has not completed"<<endl;
			}
			else if(dotsExist == false)
			{
				cout<<"Case #"<<num<<": Draw"<<endl;
			}
			num++;
	}
	return 0;
}
