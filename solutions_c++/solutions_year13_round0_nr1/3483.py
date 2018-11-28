#include <cstdio>
using namespace std;

int masks[][4]= {
  				{0,1,2,3},
  				{4,5,6,7},
  				{8,9,10,11},
  				{12,13,14,15},
  				{0,4,8,12},
  				{1,5,9,13},
  				{2,6,10,14},
  				{3,7,11,15},
  				{0,5,10,15},
  				{3,6,9,12}
                };

bool found=false;
char m[5][5];
int n,i,j,k,l,cas=1,t;
int main()
{
  scanf("%d",&t);
  n=t;
  while(n--)
  {
    
    if(cas<=t&&cas>1)
      printf("\n");
    
    for(i=0;i<4;i++)
      	scanf("%s",m[i]);
    
      found=false;
   	for(k=0;k<10;k++)
    {
      for(l=0;l<4;l++)
      {
        i=masks[k][l]/4;
        j=masks[k][l]%4;
       // printf("%c",m[i][j]);
        if(m[i][j]!='O'&&m[i][j]!='T')
          break;
      }
      
      if(l==4)
      {found=true; break;}
      
    }
    
    if(found)
    {printf("Case #%d: O won",cas++);continue;}
    
    if(!found)
    {
    found=false;
   	for(k=0;k<10;k++)
    {
      for(l=0;l<4;l++)
      {
        i=masks[k][l]/4;
        j=masks[k][l]%4;
        if(m[i][j]!='X'&&m[i][j]!='T')
          break;
      }
      
      if(l==4)
      {found=true; break;}
      
    }
    
    if(found)
    {printf("Case #%d: X won",cas++);continue;}
    
    }
    
    if(!found)
    {
      for(i=0;i<4&&!found;i++)
        for(j=0;j<4;j++)
          if(m[i][j]=='.')
      	  {
             printf("Case #%d: Game has not completed",cas++);
             found=true;
        
        	break;
          }
      
      if(!found)
        printf("Case #%d: Draw",cas++);
        
    }
  }
  return 0;
}	