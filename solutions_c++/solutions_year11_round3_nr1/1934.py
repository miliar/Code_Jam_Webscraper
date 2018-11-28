#include<iostream>
#include<string>
#include<iomanip>
using namespace std;

#define MAX 100


int main(int argc, char *argv[])
{
  char s;
  char board[MAX][MAX];
  int testcase;
  int rows;
  int columns;
  cin >> testcase;
  for(int i=0;i<testcase;i++)
  {
    cin >> rows;
    cin >> columns;
    for(int j=0;j<rows;j++)
    {
      for(int k=0;k<columns;k++)
      {
	cin >> board[j][k];
      }
    }
    int failure = 0;
  
    for(int j=0;j<rows && 0==failure;j++)
    {
      for(int k=0;k<columns && 0==failure;k++)
      {
	if('#' == board[j][k])
	{
	  if(j+1 == rows)
	  {
	    failure = 1;
	    //cout << "rows problem";
	  }
	  else if(k+1 == columns)
	  {
	    failure = 1;
	    //cout << "columns problem";
	  }
	  else if('#' == board[j][k+1] && '#' == board[j+1][k] && '#' == board[j+1][k+1])
	  {
	    board[j][k] = '/';
	    board[j+1][k+1] = '/';
	    board[j][k+1] = '\\';
	    board[j+1][k] = '\\';
	  }
	  else
	  failure = 1;
	}
      }
    }
    
    cout <<"Case #"<<i+1<<":"<<endl;
    if(1==failure)
    {
      cout<<"Impossible"<<endl;
    }
    else
    {
      for(int j=0;j<rows;j++)
      {
	for(int k=0;k<columns;k++)
	{
	  cout <<board[j][k];
	}
	cout << endl;
      }
    }
  }
  return 0;
}