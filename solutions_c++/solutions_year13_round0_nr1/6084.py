#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;


bool isX(char cc)
{
  if(cc == 'X' || cc == 'T')
    return true;
  return false;
}

bool isO(char cc)
{
  if(cc == 'O' || cc == 'T')
    return true;
  return false;
}


bool Xwon(char map[][4])
{
  // Diagonal
  if((isX(map[0][0]) && isX(map[1][1]) && isX(map[2][2]) && isX(map[3][3])) || (isX(map[0][3]) && isX(map[1][2]) && isX(map[2][1]) && isX(map[3][0])))
  {
    return true;
  }

  // Each row
  for(int i=0; i < 4; i++)
  {
    if(isX(map[i][0]) && isX(map[i][1]) && isX(map[i][2]) && isX(map[i][3]))
      return true;
  }

  // Each column
  for(int i=0; i < 4; i++)
  {
    if(isX(map[0][i]) && isX(map[1][i]) && isX(map[2][i]) && isX(map[3][i]))
      return true;
  }




  return false;
}

bool Owon(char map[][4])
{
  // Diagonal
  if((isO(map[0][0]) && isO(map[1][1]) && isO(map[2][2]) && isO(map[3][3])) || (isO(map[0][3]) && isO(map[1][2]) && isO(map[2][1]) && isO(map[3][0])))
  {
    return true;
  }
  // Each row
  for(int i=0; i < 4; i++)
  {
    if(isO(map[i][0]) && isO(map[i][1]) && isO(map[i][2]) && isO(map[i][3]))
      return true;
  }

  // Each column
  for(int i=0; i < 4; i++)
  {
    if(isO(map[0][i]) && isO(map[1][i]) && isO(map[2][i]) && isO(map[3][i]))
      return true;
  }
  return false;
}

bool isEmpty(char map[][4])
{
  for(int i =0; i < 4; i++)
    for(int j = 0; j < 4; j++)
    {
      if(map[i][j] == '.')
        return true;
    }

  return false;
}

int main()
{
  int nCase;
  string inputFileName = "input.txt";
  string outputFileName = "output.txt";
  ifstream infile;
  ofstream ofile;

  //Loading information
  infile.open(inputFileName.c_str());
  ofile.open(outputFileName.c_str());
  if (!infile.is_open())
  {
    cout <<"Unable to open file \""<< inputFileName.c_str() << "\"."<<endl;
    exit(1);
  }

  infile >> nCase;
  //char sstring[100];
  //infile.getline(sstring, 100);

  for(int numCase = 0; numCase < nCase; numCase++)
  {
    cout<<"Case #"<<numCase + 1<<""<<": ";
    ofile << "Case #"<<numCase + 1<<""<<": ";
    char map[4][4];
    for(int i=0; i < 4; i++)
      for(int j = 0; j < 4; j++)
        infile >> map[i][j];

    if(Xwon(map))
    {
      cout<<"X won"<<endl;
      ofile<<"X won"<<endl;
      continue;

    }

    else if(Owon(map))
    {
      cout<<"O won"<<endl;
      ofile<<"O won"<<endl;
      continue;
    }

    else if(isEmpty(map))
    {
      cout<<"Game has not completed"<<endl;
      ofile<<"Game has not completed"<<endl;
      continue;
    }

    else
    {
      cout<<"Draw"<<endl;
      ofile<<"Draw"<<endl;
      continue;
    }


    
    
    




    

  }
  infile.close();
  ofile.close();
  return 0;
}