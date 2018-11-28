#include <iostream>
#include <string>
using std::string;
using std::cin;
using std::cout;
 
char gameBoard[4][4];
bool full;
 
bool determineWinner (char inChar, int inInt, int inInt2)
{
        int numOfDupes = 0;
        for(int col = 0 ; col < 4 ; col++)
        {
                if(gameBoard[inInt][col] == 'T' || gameBoard[inInt][col] == inChar) 
				{
						numOfDupes++;
						if(numOfDupes == 4) 
						{
							return true;
						}
				}
        }
        numOfDupes = 0;
        for(int row = 0 ; row < 4 ; row++)
        {
                if(gameBoard[row][inInt2] == 'T' || gameBoard[row][inInt2] == inChar) 
				{
					numOfDupes++;
					if(numOfDupes == 4) 
					{
						return true;
					}
				}
        }
        numOfDupes = 0;
        if(inInt+inInt2 == 3)
        {
                for(int i = 0 ; i < 4 ; i++)
                {
                        for(int j = 0 ; j < 4 ; j++)
                        {
                                if(i+j == 3)
                                {
                                        if(gameBoard[i][j] == 'T' || gameBoard[i][j] == inChar) 
										{
											numOfDupes++;
											if(numOfDupes == 4) 
											{
												return true;
											}
										}
                                }
                        }
						
                }
                numOfDupes = 0;
        }
        if(inInt == inInt2)
        {
                for(int i = 0 ; i < 4 ; i++)
                {
                        for(int j = 0 ; j < 4 ; j++)
                        {
                                if(!(i-j))
                                {
                                        if(gameBoard[i][j] == 'T' || gameBoard[i][j] == inChar) 
										{
											numOfDupes++;
											if(numOfDupes == 4) 
											{
													return true;
											}
										}
                                }
                        }
                }
        }
        return false;
}
 
int main()
{
        int test; 
		int count = 1;
        cin >> test;
        while(test--)
        {
				string winner = "Draw";
                for(int i = 0 ; i < 4 ; i++)
                {
                        cin >> gameBoard[i];
                }
                full = true;
                for(int i = 0 ; i < 4 ; i++)
                {
                        for(int j = 0 ; j < 4 ; j++)
                        {
                                if(gameBoard[i][j] == '.') full = false;
                                else if(gameBoard[i][j] == 'X' || gameBoard[i][j] == 'O')
                                {
                                        bool iswin = determineWinner(gameBoard[i][j], i, j);
                                        if(iswin)
                                        {
                                                winner = "";
                                                winner += gameBoard[i][j];
                                                break;
                                        }
                                }
                        }
                }
				cout << "Case #" << count++ << ": ";
                if(winner == "X" || winner == "O") 
				{
					cout << winner << " won\n";
				}
                else if(winner == "Draw")
                {
                        if(full)
						{
							cout << "Draw\n";
						}
                        else 
						{
							cout << "Game has not completed\n";
						}
                }
        }
        return 0;
}