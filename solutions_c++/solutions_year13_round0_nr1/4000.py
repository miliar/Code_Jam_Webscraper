#include <iostream>
#include <vector>

using namespace std;

char check(const vector<char>& vec)
{
  if(vec[0] == '.' || vec[1] == '.')
    {return 'U';}
  char sym;
  if(vec[0] != 'T')
    sym = vec[0];
  else
    sym = vec[1];
  int i = 1;
  char stat='T';
  for(;i<vec.size(); ++i)
    {
      if(vec[i]==sym || vec[i]=='T')
	{
	  continue;
	}
      else if(vec[i] == '.')
	{return 'U';}
      else
	{break;}
    }
  if(i==vec.size())
    {
      stat = sym;
    }
  //cout << stat << endl;
  return stat;
}

int main()
{
  int T;
  cin >> T;
  for(int i = 0; i < T; ++i)
    {
      vector<vector<char> > vec;
      for(int j = 0; j < 4; ++j)
	{
	  vector<char> temp;
	  for(int k = 0; k < 4; ++k)
	    {
	      char c;
	      cin >> c;
	      temp.push_back(c);
	    }
	  vec.push_back(temp);
	}
      bool tie = true;
      bool unfinish = false;
      bool OO = false;
      bool XX = false;
      for(int j = 0; !OO && !XX && j < 4; ++j)
	{
	  char sym = check(vec[j]);
	  if(sym == 'U')
	    {
	      tie=false;
	      unfinish = true;
	    }
	  if(sym == 'O')
	    {
	      tie=false;
	      unfinish = false;
	      OO=true;
	    }
	  if(sym == 'X')
	    {
	      tie = false;
	      unfinish = false;
	      XX=true;
	    }
	}
      for(int j = 0; !OO && !XX && j < 4; ++j)
	{
	  vector<char> temp;
	  temp.push_back(vec[0][j]);
	  temp.push_back(vec[1][j]);
	  temp.push_back(vec[2][j]);
	  temp.push_back(vec[3][j]);
	  char sym = check(temp);
	  if(sym == 'U')
	    {
	      tie=false;
	      unfinish = true;
	    }
	  if(sym == 'O')
	    {
	      tie=false;
	      unfinish = false;
	      OO=true;
	    }
	  if(sym == 'X')
	    {
	      tie = false;
	      unfinish = false;
	      XX=true;
	    }
	}
      if(!OO && !XX)
	{
	  vector<char> temp;
	  temp.push_back(vec[0][3]);
	  temp.push_back(vec[1][2]);
	  temp.push_back(vec[2][1]);
	  temp.push_back(vec[3][0]);
	  char sym = check(temp);
	  if(sym == 'U')
	    {
	      tie=false;
	      unfinish = true;
	    }
	  if(sym == 'O')
	    {
	      tie=false;
	      unfinish = false;
	      OO=true;
	    }
	  if(sym == 'X')
	    {
	      tie = false;
	      unfinish = false;
	      XX=true;
	    }
	}
      if(!OO &&!XX)
	{
          vector<char> temp;
          temp.push_back(vec[0][0]);
          temp.push_back(vec[1][1]);
          temp.push_back(vec[2][2]);
          temp.push_back(vec[3][3]);
          char sym = check(temp);
          if(sym == 'U')
            {
              tie=false;
              unfinish = true;
            }
          if(sym == 'O')
            {
              tie=false;
              unfinish = false;
              OO=true;
            }
          if(sym == 'X')
            {
              tie = false;
              unfinish = false;
              XX=true;
            }
        }
      cout << "Case #" << i+1 << ": ";
      if(OO)
	{cout << "O won" << endl;}
      else if(XX)
	{cout << "X won" << endl;}
      else if(unfinish)
	{cout << "Game has not completed" << endl;}
      else if(tie)
	{cout << "Draw" << endl;}
      else
	{cerr <<"ERROR" << endl;}
    }
}
