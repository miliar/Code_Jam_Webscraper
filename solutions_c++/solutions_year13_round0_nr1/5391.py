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

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A.out", "w", stdout);

	  int t;scanf("%d",&t);
	  char n[5][5];
	  int chos;
	  int coun;
	  
	for (int cas=1;cas<=t;cas++)
{
	   for (int i=0;i<=3;i++)
	  {
	      scanf("%s",&n[i]);
	  }
	  chos=0;
	  
	  for (int j=0;j<=3;j++)
	  { 
		  
		  
		  coun=0;
		  for (int j1=0;j1<=3;j1++)
		  {
			  if ((n[j][j1]=='O')||(n[j][j1]=='T'))
				  coun++;
			  
		  }
		  if (coun==4)
		  {
			  chos=1;break;
		  }
		  else
			  coun=0;
		  for (j1=0;j1<=3;j1++)
		  {
			  if ((n[j][j1]=='X')||(n[j][j1]=='T'))
				  coun++;
			  
		  }
		   if (coun==4)
		  {
			  chos=2;break;
		  }
		  else
			  coun=0;
		     for (j1=0;j1<=3;j1++)
		  {
			  if ((n[j1][j]=='X')||(n[j1][j]=='T'))
				  coun++;
			  
		  }
			   if (coun==4)
		  {
			  chos=2;break;
		  }
		  else
			  coun=0;

		     for (j1=0;j1<=3;j1++)
		  {
			  if ((n[j1][j]=='O')||(n[j1][j]=='T'))
				  coun++;
		  }
		  if (coun==4)
		  {
			  chos=1;break;
		  }
		  else
			  coun=0;
	  }

		   
	  if (chos==0)
	  {
		  if( (n[0][0]=='X')||(n[0][0]=='T'))
		  {
			  if( (n[1][1]=='X')||(n[1][1]=='T'))
			  {
				  if( (n[2][2]=='X')||(n[2][2]=='T'))
					{  
						if( (n[3][3]=='X')||(n[3][3]=='T'))
						  chos=2;
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
						  chos=1;
				     }

			  }
		  }
	  }
	  if(chos==0)
	  {
		  for (int ct=0;ct<=3;ct++)
		  {
			  for(int dt=0;dt<=3;dt++)
			  { 
				  if(n[ct][dt]=='.')
				  {
					  chos=4;
					  break;
				  }
			  }
		  }
	  }
	  if (chos==0)
		  cout<<"Case #"<<cas<<": Draw"<<endl;
	  else if(chos==1)
		  cout<<"Case #"<<cas<<": O won"<<endl;
	  else if (chos==2)
		  cout<<"Case #"<<cas<<": X won"<<endl;
	  else if (chos==4)
		  cout<<"Case #"<<cas<<": Game has not completed"<<endl;
}



	  





		  


	
	  
	

	  
	  
	  return 0;
  }

	  
		
