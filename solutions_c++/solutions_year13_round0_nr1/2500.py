#include<iostream>

using namespace std;

int main()
{
 int i,j,t,k,z,b;
 char ch,a[4][4],c;
 
 freopen("A-small-attempt2.in", "r", stdin);
 freopen("output.txt", "w", stdout);
 
 scanf("%d",&t);
 
 for(z=0;z<t;z++)
 {
  for(i=0;i<4;i++)
  {
   scanf("%s",&a[i]);
   
  } 
  scanf("%c",&ch);
  
  k=0;
  
  for(i=0;i<4;i++)
  {
   b=0;
   if(a[i][0]=='T')
   {c=a[i][1]; b++;} 
                   
   else
   c=a[i][0];                
       
   for(j=b+1;j<4;j++)                
   if((a[i][j-1]!=a[i][j])&&(a[i][j-1]!='T')&&(a[i][j]!='T'))
   break;
   
   if((j==4)&&(c!='.'))
   { k=1; break; }               
  }
  
  if(k==1)
  {
   printf("Case #%d: %c won\n",z+1,c);        
   continue;       
  }
  
  for(j=0;j<4;j++)
  {
   b=0;
   if(a[0][j]=='T')
   {c=a[1][j]; b++;} 
                   
   else
   c=a[0][j];                
                   
   for(i=b+1;i<4;i++)                
   if((c!=a[i][j])&&(a[i][j]!='T'))
   break;
   
   if((i==4)&&(c!='.'))
   { k=1; break; }               
  }
  
  if(k==1)
  {
   printf("Case #%d: %c won\n",z+1,c);        
   continue;       
  }
     
  if(a[0][0]=='T')
  {
   c=a[1][1];
   if((c==a[2][2])&&(c==a[3][3])&&(c!='.'))
   printf("Case #%d: %c won\n",z+1,c);
  } 
                   
  else
  {
   c=a[0][0];
   for(i=1;i<4;i++)
   if((c!=a[i][i])&&(a[i][i]!='T'))
   break;
   
   if((i==4)&&(c!='.'))
   {
    printf("Case #%d: %c won\n",z+1,c);        
    continue;       
   }
  }
  
  if(a[0][3]=='T')
  {
   c=a[1][2];
   if((c==a[2][1])&&(c==a[3][0])&&(c!='.'))
   printf("Case #%d: %c won\n",z+1,c);
  } 
                   
  else
  {
   c=a[0][3];
   for(i=1;i<4;i++)
   if((c!=a[i][3-i])&&(a[i][3-i]!='T'))
   break;
   
   if((i==4)&&(c!='.'))
   {
    printf("Case #%d: %c won\n",z+1,c);        
    continue;       
   }
  }
  
  k=0;
  
  for(i=0;i<4;i++)
  {
   for(j=0;j<4;j++)
   if(a[i][j]=='.')
   { k=1; break;}   
   
   if(k==1)
   break;
  } 
  
  if(k==1)
  printf("Case #%d: Game has not completed\n",z+1);
  
  else
  printf("Case #%d: Draw\n",z+1);
 }
   
 return 0;   
}
