#include<iostream>
using namespace std;

int main()
{
  char board[4][4];
  int testcase;
  cin>>testcase;
  for(int i =0;i<testcase;i++)
  {
      bool isDraw = true;
	 
	 
    for(int j=0;j<4;j++)
    {
	 for(int k=0;k<4;k++)
	 {
	   cin>>board[j][k];
	   if(board[j][k]=='.')
		{		
			isDraw = false; 
		} 
	 }
    }
    
    /*cout<<"printing the Output";
    		 cout<<"isDraw"<<isDraw<<"\n";
    for(int j=0;j<4;j++)
    {
	 for(int k=0;k<4;k++)
	 {
	   cout<<board[j][k];
	 }
    }*/
    string output ="";
    
    //checking for the Rows
    for(int j=0;j<4;j++)
    {
	 int counterO = 0;
	 int counterX = 0;
	 int counterT = 0;
	 for(int k=0;k<4;k++)
	 {
	   	 if(board[j][k] == 'O')
		   counterO++;
		 if(board[j][k] == 'X')
		   counterX++;
		 if(board[j][k] == 'T')
		   counterT++;
	 }
	 //cout<<counterO<<":"<<counterT<<":"<<counterX<<"\n";
	 if(counterO + counterT == 4)
	   output = "O won";
	 else if(counterX + counterT ==4)
	   output = "X won";
    }
    
    //Checking for Columns
    for(int j=0;j<4;j++)
    {
	 int counterO = 0;
	 int counterX = 0;
	 int counterT = 0;
	 for(int k=0;k<4;k++)
	 {
	   	 if(board[k][j] == 'O')
		   counterO++;
		 if(board[k][j] == 'X')
		   counterX++;
		 if(board[k][j] == 'T')
		   counterT++;
	 }
	 if(counterO + counterT == 4)
	   output = "O won";
	 else if(counterX + counterT ==4)
	   output = "X won";
    }
    
    	 int counterO = 0;
	 int counterX = 0;
	 int counterT = 0;
    //Checking for Both the Diagonals
    for(int j=0;j<4;j++)
    {
	   	 if(board[j][j] == 'O')
		   counterO++;
		 if(board[j][j] == 'X')
		   counterX++;
		 if(board[j][j] == 'T')
		   counterT++;
	 if(counterO + counterT == 4)
	   output = "O won";
	 else if(counterX + counterT ==4)
	   output = "X won";
    }
    	 //cout<<counterO<<":"<<counterT<<":"<<counterX<<"\n";
	 counterO = 0;
	 counterX = 0;
	 counterT = 0;
    for(int j=0;j<4;j++)
    {
	 int index = 3-j;
	   	 if(board[index][j] == 'O')
		   counterO++;
		 if(board[index][j] == 'X')
		   counterX++;
		 if(board[index][j] == 'T')
		   counterT++;
	 if(counterO + counterT == 4)
	   output = "O won";
	 else if(counterX + counterT == 4)
	   output = "X won";
    }
    		 //cout<<counterO<<":"<<counterT<<":"<<counterX<<"\n";
    if(output==""&&!isDraw)
	 output = "Game has not completed";
    else if(output==""&&isDraw)
	 output = "Draw";
    
    cout<<"Case #"<<i+1<<": "<<output<<"\n";
    //cout<<isDraw<<"\n";
  }
  
}
