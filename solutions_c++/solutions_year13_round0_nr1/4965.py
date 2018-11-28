#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

#define FOR(i,v,n) for(int i=v;i<=n;i++)

char s[6][6];

int check(char c)
{
  int d1=1,d2=1;
  FOR(i,1,4)
    {
      int h=1,v=1;
      FOR(j,1,4)
	{
	  if(s[i][j]!=c)
	    h=0;
	  if(s[j][i]!=c)
	    v=0;
	}
      if(h || v)
	return 1;
      
      if(s[i][i]!=c)
	d1=0;
      if(s[5-i][i]!=c)
	d2=0;
    }  
  return (d1||d2);
}

int main()
{
  int T;
  cin>>T;
  string res;
  FOR(t,1,T)
    {
      int tx=0,ty=0;
      bool dot=false;
      FOR(i,1,4)
	{
	  scanf("%s",s[i]+1);
	 
	  FOR(j,1,4)
	    {
	      if(s[i][j]=='T')
		tx=j,ty=i;
	      else if(s[i][j]=='.')
		dot=true;
	    }
	}
      
      if((s[ty][tx]='X') && check('X'))
	res="X won";
      else if((s[ty][tx]='O') && check('O'))
	res="O won";
      else
	{
	  if(dot)
	    res="Game has not completed";
	  else
	    res="Draw";
	}

      printf("Case #%d: %s\n",t,res.c_str());
	    
    }
}
