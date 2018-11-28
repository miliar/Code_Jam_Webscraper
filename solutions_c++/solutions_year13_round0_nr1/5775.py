#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"





#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include<iostream>
using namespace std;





  int main()

  {

    freopen("A-small-attempt4.in", "r", stdin);
    freopen("A4.out", "w", stdout);

	  int t;scanf("%d",&t);
	  char n[5][5];
	  int cho;
	  int con;
	  
	for (int cas=1;cas<=t;cas++)
{
	  
	 
	 
	  for (int i=0;i<=3;i++)
	  {
	      scanf("%s",&n[i]);
	  }
	  cho=0;
	  
	  for (int j=0;j<=3;j++)
	  { 
		  
		  
		  con=0;
		  for (int j1=0;j1<=3;j1++)
		  {
			  if ((n[j][j1]=='O')||(n[j][j1]=='T'))
				  con++;
			  
		  }
		  if (con==4)
		  {
			  cho=1;break;
		  }
		  else
			  con=0;
		  for (int j2=0;j2<=3;j2++)
		  {
			  if ((n[j][j2]=='X')||(n[j][j2]=='T'))
				  con++;
			  
		  }
		   if (con==4)
		  {
			  cho=2;break;
		  }
		  else
			  con=0;
		     for (int j3=0;j3<=3;j3++)
		  {
			  if ((n[j3][j]=='X')||(n[j3][j]=='T'))
				  con++;
			  
		  }
			   if (con==4)
		  {
			  cho=2;break;
		  }
		  else
			  con=0;

		     for (int j4=0;j4<=3;j4++)
		  {
			  if ((n[j4][j]=='O')||(n[j4][j]=='T'))
				  con++;
		  }
		  if (con==4)
		  {
			  cho=1;break;
		  }
		  else
			  con=0;
	  }

		   
	  if (cho==0)
	  {
		  if( (n[0][0]=='X')||(n[0][0]=='T'))
		  {
			  if( (n[1][1]=='X')||(n[1][1]=='T'))
			  {
				  if( (n[2][2]=='X')||(n[2][2]=='T'))
					{  
						if( (n[3][3]=='X')||(n[3][3]=='T'))
						  cho=2;
				     }

			  }
		  }
		  else if( (n[0][0]=='O')||(n[0][0]=='T'))
		  {
			  if( (n[1][1]=='O')||(n[1][1]=='T'))
			  {
				  if( (n[2][2]=='O')||(n[2][2]=='T'))
					{  
						if( (n[3][3]=='O')||(n[3][3]=='T'))
						  cho=1;
				     }

			  }
		  }
	  }
	  if(cho==0)
	  {
		  for (int ct=0;ct<=3;ct++)
		  {
			  for(int dt=0;dt<=3;dt++)
			  { 
				  if(n[ct][dt]=='.')
				  {
					  cho=4;
					  break;
				  }
			  }
		  }
	  }
	  if (cho==0)
		  cout<<"Case #"<<cas<<": Draw"<<endl;
	  else if(cho==1)
		  cout<<"Case #"<<cas<<": O won"<<endl;
	  else if (cho==2)
		  cout<<"Case #"<<cas<<": X won"<<endl;
	  else if (cho==4)
		  cout<<"Case #"<<cas<<": Game has not completed"<<endl;
}



	  





		  


	
	  
	

	  
	  
	  return 0;
  }
				
