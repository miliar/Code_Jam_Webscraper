#include <iostream>
using namespace std;
int map[5][5];

int main()
{
     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);
 	int n;
 	int T;
 	scanf("%d",&T);
 	for(int cas=1;cas<=T;cas++)
 	{
      char  in[5];
      int flagT=0;
      int sx,sy;
      int n=4;
      for(int i=0;i<4;i++)
      {
        scanf("%s",in);
        int len=strlen(in);
        for(int j=0;j<len;j++)
        {
		  if(in[j]=='X')
		   map[i][j]=1;
          else if(in[j]=='O')
            map[i][j]=2;
          else if(in[j]=='.')
            map[i][j]=3;
          else 
           {
		   	   map[i][j]=4;
		   	   flagT=1;
		   	   sx=i;
		   	   sy=j; 
		   }
      }
   }
   int flagX=0;
   if(flagT==1)
   {
    map[sx][sy]=1;
   }
   //row
   for(int i=0;i<n;i++)
   {
     int ans=0;
     for(int j=0;j<n;j++)
     {
	   if(map[i][j]==1)
	     ans++;
	  }
	  if(ans==4)
	   flagX=1;
   }
   if(flagX)
   {
      printf("Case #%d: X won\n",cas);
      continue;
    }
    //col
    for(int i=0;i<n;i++)
    {
       int ans=0;
       for(int j=0;j<n;j++)
       {
	   if(map[j][i]==1)
	      ans++;
       }
       if(ans==4)
        flagX=1;
     }
     if(flagX)
   {
      printf("Case #%d: X won\n",cas);
      continue;
    }
    //diagonal
    int ans=0;
   for(int i=0;i<n;i++)
    if(map[i][i]==1)
      ans++;
   if(ans==4)
   {
	 printf("Case #%d: X won\n",cas);
      continue;
   }
   if(map[0][3]==1&&map[1][2]==1&&map[2][1]==1&&map[3][0]==1)
   {
   	printf("Case #%d: X won\n",cas);
      continue;
    }														 
   //***********************//
     int flagO=0;
   if(flagT==1)
   {
    map[sx][sy]=2;
   }
   //row
   for(int i=0;i<n;i++)
   {
     int ans=0;
     for(int j=0;j<n;j++)
     {
	   if(map[i][j]==2)
	     ans++;
	  }
	  if(ans==4)
	   flagO=1;
   }
   if(flagO)
   {
      printf("Case #%d: O won\n",cas);
      continue;
    }
    //col
    for(int i=0;i<n;i++)
    {
       int ans=0;
       for(int j=0;j<n;j++)
       {
	   if(map[j][i]==2)
	      ans++;
       }
       if(ans==4)
        flagO=1;
     }
     if(flagO)
   {
      printf("Case #%d: O won\n",cas);
      continue;
    }
    //diagonal
     ans=0;
   for(int i=0;i<n;i++)
    if(map[i][i]==2)
      ans++;
   if(ans==4)
   {
	 printf("Case #%d: O won\n",cas);
      continue;
   }
   if(map[0][3]==2&&map[1][2]==2&&map[2][1]==2&&map[3][0]==2)
   {
   	printf("Case #%d: O won\n",cas);
      continue;
    }			 
 //****************//
  //draw
  int flagD=0;
  for(int i=0;i<n;i++)
   for(int j=0;j<n;j++)
   {
   	 if(map[i][j]==3)
	  {
	   	flagD=1;
		break;
	  } 
   }  
  if(flagD==1)
  {
    printf("Case #%d: Game has not completed\n",cas);
    continue;
   }
  else
  {
    printf("Case #%d: Draw\n",cas);
    continue;
   }
}
return 0;
}
     
   
  
     
   
