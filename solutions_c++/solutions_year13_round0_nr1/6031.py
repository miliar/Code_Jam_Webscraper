#include <iostream>
#include <vector>

enum cell {
  EMPTY = 0,
  O_PLAYER,
  X_PLAYER,
  SPECIAL
};

enum problemConstants {
  UPPER_LIMIT = 1000
};

typedef std::pair<int,int> vec2;

using namespace std;

void player_O_won ()
{
  cout<<"O won";
}

void player_X_won ()
{
  cout<<"X won";
}

void draw ()
{
  cout<<"Draw";
}

void notComplete()
{
  cout<<"Game has not completed";
}


// read a board from standard input
void readBoard (unsigned short int board [4][4])
{
  for (unsigned char i=0;i<4;i++)
    {
      for (unsigned char j=0;j<4;j++)
	{
	  char curChar;
	  cin>>curChar;
	  switch(curChar)
	    {
	    case 'O':
	      {
		board[i][j]=O_PLAYER;
	      }
	      break;
	    case 'X':
	      {
		board[i][j]=X_PLAYER;
	      }
	      break;
	    case '.':
	      {
		board[i][j]=EMPTY;
	      }
	      break;
	    case 'T':
	      {
		board[i][j]=SPECIAL;
	      }
	      break;
	    }
	}
    }
}

vec2 hashCell(unsigned char c)
{
  switch(c)
    {
    case EMPTY:
      {
	return vec2(-5,-5);
      }
      break;
    case O_PLAYER:
      {
	return vec2(1,0);
      }
      break;
    case X_PLAYER:
      {
	return vec2(0,1);
      }
      break;
    case SPECIAL:
      {
	return vec2(1,1);
      }
      break;
    default:
      {
	return vec2(0,0);
      }
    }
}

vec2 operator+ (const vec2& lhs, const vec2& rhs)
{
  return vec2(lhs.first+rhs.first,lhs.second+rhs.second);
}


vec2 hashLine(unsigned short int board [4][4],unsigned char i)
{
  vec2 hashedLine(0,0);
  for (unsigned char j=0;j<4;j++)
    {
      hashedLine=hashedLine+hashCell(board[i][j]);
    }
  return hashedLine;
}

vec2 hashColumn(unsigned short int board [4][4],unsigned char j)
{
  vec2 hashedColumn(0,0);
  for (unsigned char i=0;i<4;i++)
    {
      hashedColumn=hashedColumn+hashCell(board[i][j]);
    }
  return hashedColumn;
}

vec2 hashDiagonal1(unsigned short int board [4][4])
{
  vec2 hashedDiag1(0,0);
  for (unsigned char i=0;i<4;i++)
    {
      hashedDiag1=hashedDiag1+hashCell(board[i][i]);
    }
  return hashedDiag1;
}

vec2 hashDiagonal2(unsigned short int board [4][4])
{
  vec2 hashedDiag2(0,0);
  for (unsigned char i=0;i<4;i++)
    {
      hashedDiag2=hashedDiag2+hashCell(board[i][3-i]);
    }
  return hashedDiag2;
}

void printBoard (unsigned short int board[4][4])
{
  for (unsigned char i=0;i<4;i++)
    {
      for (unsigned char j=0;j<4;j++)
	{
	  cout<<board[i][j]<<" ";
	}
      cout<<endl;
    }
}

void printState (unsigned short int board [4][4])
{
  vector<vec2> hashed;
  // we hash the lines
  for (unsigned char i=0;i<4;i++)
    {
      hashed.push_back(hashLine(board,i));
    }
  // we hash the columns
  for (unsigned char j=0;j<4;j++)
    {
      hashed.push_back(hashColumn(board,j));
    }
  // we hash the 2 diagonals
  hashed.push_back(hashDiagonal1(board));
  hashed.push_back(hashDiagonal2(board));

  bool gameIsFull=true;
  for (unsigned char i=0;i<10;i++)
    {
      if (hashed[i].first==4)
	{
	  return player_O_won();

	}
      else if (hashed[i].second==4)
	{
	  return player_X_won();
	}
      else if ((hashed[i].first<0) || (hashed[i].second<0))
	{
	  gameIsFull=false;
	}
    }
  if (gameIsFull)
    return draw();
  else
    return notComplete();
}


int main ()
{
  unsigned int nboards;
  cin>>nboards;

  // boards now have to be stored in memory because of parallal processing
  unsigned short int board [4][4];

  for (unsigned int boardCounter=0;boardCounter<nboards;boardCounter++)
    {
      // read the board
      readBoard(board);
      cout<<"Case #"<<boardCounter+1<<": ";
      printState(board);
      cout<<endl;

     }
    return 0;
}
