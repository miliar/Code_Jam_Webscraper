#include<stdio.h>
#include<iostream>
#include<stdlib.h>
using namespace std;
char a[4][4];
int check(int,char);
int checkdot(void);
main()
{ 
    freopen ("A-large.in", "r", stdin);
    freopen ("Q1large.in", "w", stdout);   
 int t,cases;
    cases=1;
    scanf("%d",&t);getchar();
 while(t--)
  {
    
	for(int i=1;i<=4;i++)   //for input of values
	 {  int j;
	 	for( j=1;j<=4;j++)
	     cin>>a[i][j];
	 }
	 int k,l;
	 cout<<"Case #"<<cases<<": ";
	 int gt=0; 
  for(l=1;l<=4;l++)
    {  if(gt==1)
        break;
	 for(k=1;k<=4;k++)
	 {   if(gt==1)
	      break;    
	     char tmp;
	     if(a[l][k]=='X')       tmp='X';
	     else if(a[l][k]=='O')  tmp='O';
	 	 if(check(k,tmp)==1)
	 	 {cout<<tmp<<" won\n";gt=1;break;}
	 	 else if(checkdot()==1&&k==4&&l==4)
	 	 {cout<<"Game has not completed\n";gt=1; break;}
	 	 else if(check(k,tmp)==0&&k==4&&l==4&&checkdot()==0)
	 	 {cout<<"Draw\n";gt=1; break;}
		 else
		 continue;    	 	 
     }
   }
     cases++;
 }
}
int check(int g,char tp)
{   
    int flag=0;
    if((a[g][1]==tp||a[g][1]=='T')&&
	   (a[g][2]==tp||a[g][2]=='T')&&
	   (a[g][3]==tp||a[g][3]=='T')&&
	   (a[g][4]==tp||a[g][4]=='T')) 
	{  
		flag=1;
		return flag;
	}
	else if((a[1][g]==tp||a[1][g]=='T')&&
	        (a[2][g]==tp||a[2][g]=='T')&&
	        (a[3][g]==tp||a[3][g]=='T')&&
	        (a[4][g]==tp||a[4][g]=='T')) 
                	{
		                flag=1;
		                return flag;
	                }
	else if((g==1)&&
	        (a[1][1]==tp||a[1][1]=='T')&&
	        (a[2][2]==tp||a[2][2]=='T')&&
	        (a[3][3]==tp||a[3][3]=='T')&&
	        (a[4][4]==tp||a[4][4]=='T'))
	          {
	   	          flag=1;
	   	          return flag;
	          }
	else if((g==4)&&
	        (a[1][4]==tp||a[1][4]=='T')&&
	        (a[2][3]==tp||a[2][3]=='T')&&
	        (a[3][2]==tp||a[3][2]=='T')&&
	        (a[4][1]==tp||a[4][1]=='T'))
               {
	   	          flag=1;
	   	          return flag;
	          }
	else return flag;
}
int checkdot(void)
{
	int s;
	for(int s=1;s<=4;s++)   //for input of values
	 {  int r;
	 	for( r=1;r<=4;r++)
	 	{  
	 	  if(a[s][r]=='.')
	 	  return 1;
	 	}
     } 			 	
}
