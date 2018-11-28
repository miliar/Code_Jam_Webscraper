#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>

#include <map>
#define LL long long
#define ff first
#define ss second
#define PB push_back
#define MP make_pair
using namespace std;

int P,K;
int t;
char s[5][5];
int xt,yt;

int main()
{
  scanf("%d",&t);  
int n=4;
  for(int z=1;z<=t;z++)
  {
    int xt=-5;
    int yt=-16;
    int kr=0;
    int won=0;
    for(int i=1;i<=n;i++)
    {
      scanf("%s",&s[i][1]);
      for(int j=1;j<=n;j++)if(s[i][j]=='T')
      {
	xt=i;
	yt=j;
      }
    }
      
      for(int i=1;i<=n;i++)
      {
	P=0;
	K=0;
	for(int j=1;j<=n;j++)
	{
	  if(s[i][j]=='O')
	    P++;
	  if(s[i][j]=='X')
	    K++;
	  if(s[i][j]=='.')kr++;
	}
	
	if(P==4||P==3&&xt==i)
	  won=1;
	if(K==4||K==3&&xt==i)
	  won=2;
	
      }
      
      for(int j=1;j<=n;j++)
      {
	P=K=0;
	for(int i=1;i<=n;i++)
	{
	  if(s[i][j]=='O')
	    P++;
	  if(s[i][j]=='X')
	    K++;
	  if(s[i][j]=='.')kr++;
	}
	
	if(P==4||P==3&&yt==j)
	  won=1;
	if(K==4||K==3&&yt==j)
	  won=2;
	
      }
      
      P=K=0;
      for(int i=1;i<=n;i++)
      {
	  if(s[i][i]=='O')
	    P++;
	  if(s[i][i]=='X')
	    K++;
	  if(s[i][i]=='.')kr++;
	
	
	if(P==4||P==3&&yt==xt)
	  won=1;
	if(K==4||K==3&&yt==xt)
	  won=2;
      }
      P=K=0;
	  if(s[1][4]=='O')
	    P++;
	  if(s[1][4]=='X')
	    K++;
	  if(s[2][3]=='O')
	    P++;
	  if(s[2][3]=='X')
	    K++;
	  if(s[3][2]=='O')
	    P++;
	  if(s[3][2]=='X')
	    K++;
	  if(s[4][1]=='O')
	    P++;
	  if(s[4][1]=='X')
	    K++;
      if(P==4||P==3&&yt+xt==5)
	  won=1;
	if(K==4||K==3&&yt+xt==5)
	  won=2;
    
	printf("Case #%d: ",z);
	
    if(won==1)printf("O won");
    if(won==2)printf("X won");
    if(won==0)
    {
      if(kr>0)printf("Game has not completed");
      else printf("Draw");
      
    }
    printf("\n");
    

  }
  return 0;
}