#include<iostream>
#include<vector>
#include<string>
using namespace std;

int winner(string s)
{
  int flag=1;
  for(int i=0;i<4;i++)
  {
    if(s[i]=='T')
    {
      s[i]=s[1];
      break;
    }
  }
  for(int i=0;i<3;i++)
  {
    if((s[i]!=s[i+1]) || (s[i]=='.'))
    {
      return -1;
    }
    if(s[i]=='X')
    {
      flag=0;
    }
    
  }
  return flag;//0 for 'X',1 for 'O' 
    
}

int scan(vector<string>& tictac)
{
  string s;
  for(int i=0;i<4;i++)
  {
    if(!s.empty())
    {
      s.clear();
    }
    for(int j=0;j<4;j++)
    {
      s.append(1,tictac[j][i]);
    }
    int temp=winner(s);
    if(temp>-1)
    {
      return temp;
    }
  }
  return -1;
}

int diascan(vector<string>& tictac)
{
  string s;
  for(int i=0;i<4;i++)
  {
    s.append(1,tictac[i][i]);
  }
  int temp=winner(s);
  if(temp>-1)
  {
    return temp;
  }
  s.clear();
  for(int i=0;i<4;i++)
  {
    s.append(1,tictac[i][3-i]);
  }
  return winner(s);
}

int ifdraw(vector<string>& tictac)
{
  for(int i=0;i<4;i++)
  {
    for(int j=0;j<4;j++)
    {
      if(tictac[i][j]=='.')
      {
	return -1;
      }
    }
  }
  return 2;
}
int findwinner(vector<string>& tictac)
{
  int colsc=scan(tictac);
  if(colsc>=0)
  {
    return colsc;
  }
  int diasc= diascan(tictac);
  if(diasc>=0)
  {
    return diasc;
  }
  return ifdraw(tictac);
}
  


int main()
{
  int T; //test cases
  cin>>T;
  vector<int> results(T,-1);
  vector<string> tictac;
  string s;
  for(int i=0;i<T;i++)
  {
    bool flagfound=false;
    if(!tictac.empty())
    {
      tictac.clear();
    }
    for(int j=0;j<4;j++)
    {
      if(!s.empty())
      {
	s.clear();
      }
      cin>>s;
      if(!flagfound)
      {
	int temp=winner(s);
	if(temp==-1)
	{
	  tictac.push_back(s);
	}
	else
	{
	  flagfound=true;
	  results[i]=temp;
	}
       }
     }
     if(!flagfound)
     {
       results[i]=findwinner(tictac);
     }
  }
  for(int i=0;i<T;i++)
  {
    switch(results[i])
    {
      case -1: cout<<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;
	       break;
      case 0:  cout<<"Case #"<<i+1<<": "<<"X won"<<endl;
	       break;
      case 1:  cout<<"Case #"<<i+1<<": "<<"O won"<<endl;
	       break;
      case 2:  cout<<"Case #"<<i+1<<": "<<"Draw"<<endl;
	       break;
     }
  }
    
}
      
