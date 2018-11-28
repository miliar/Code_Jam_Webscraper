#include <cstdio>
#include<iostream>
#include <string>
using namespace std;

int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
  freopen("ouput.out", "w", stdout);
	
 int test;
 char pvt;
 bool temp_test=true;
 bool abs_test=false;
 bool dot_fnd=false;
 cin>>test;
 for (int b = 0; b < test; b++)
 {
   string * arr =new string [4]; 
   temp_test=true;
   abs_test=false;
   dot_fnd=false;
   
   //inter board
   for (int i = 0; i < 4; i++)
   {
	   cin>>arr[i];
   }

   //test ofkyyyyyyyyy
   for (int i = 0; i < 4; i++)
   {
	   	   temp_test=true;

	   pvt=arr[i][0];
	   if(pvt=='.')
	   {
		   dot_fnd=true;
	    continue;
	   }
	   else if(pvt=='T')
	   {
	    pvt=arr[i][1];
		 if(pvt=='.')
	      {
		   dot_fnd=true;
	        continue;
	      }
	  
	   }

	   for (int j = 1; j < 4; j++)
	   {
		
		   if(arr[i][j]=='.')
			dot_fnd=true;

		   if(arr[i][j]==pvt || arr[i][j]=='T')
		    continue;
		   else
		   {
			   temp_test=false;
			   break;
		   }
	   }
	   
	   if(temp_test)
	   {
		   abs_test=true;
		   printf("Case #%d: %c won\n",b+1,pvt);
	       break;
	   }
   }

   //test ra2syyyyyyyyyyyyyyyyyyyyyyyyy
   if(!abs_test)
   {
	   temp_test=true;
	   for (int col = 0; col < 4; col++)
	   {
		   	   temp_test=true;

		   pvt=arr[0][col];
		  
		   if(pvt=='.')
	       {
		      dot_fnd=true;
	          continue;
	       }
		   else if(pvt=='T')
		   {
			pvt=arr[1][col];
			 if(pvt=='.')
		     {
			   dot_fnd=true;
			   continue;
		     }
		   }
		   for (int row = 1; row < 4; row++)
		   {
				   if(arr[row][col]==pvt || arr[row][col]=='T')
				continue;
			   else
			   {
				   temp_test=false;
				   break;
			   }
		   }
		    if(temp_test)
			{
				abs_test=true;
				printf("Case #%d: %c won\n",b+1,pvt);
				break;
			}
	   }
   
   
   
   }

   //test main diagonal
   if(!abs_test)
   {
	   	   temp_test=true;

     //main diagonal
	   pvt=arr[0][0];

	   
	   for (int i = 1; i < 4; i++)
	   {
		   if(pvt=='.')
	     {
	      dot_fnd=true;
		  temp_test=false;
		  break;
         }
		   else if(pvt=='T')
		   {
			pvt=arr[1][1];
			 if(pvt=='.')
			  {
			   dot_fnd=true;
			   temp_test=false;
			   break;
			  }	  
		   }
	   

		   if(arr[i][i]==pvt || arr[i][i]=='T')
				continue;
			   else
			   {
				   temp_test=false;
				   break;
			   }
	   }
       if(temp_test)
			{
				abs_test=true;
				printf("Case #%d: %c won\n",b+1,pvt);
			}
   }
	   //second diagonal
   if (!abs_test)
   {
	   	   temp_test=true;

	   pvt=arr[0][3];
	   for (int i = 2; i >= 0; i--)
	   {
		   if(pvt=='.')
	       {
		      dot_fnd=true;
			  temp_test=false;
			  break;
	       }
		   else if(pvt=='T')
		   {
			pvt=arr[1][2];
			 if(pvt=='.')
			  {
			   dot_fnd=true;
			   temp_test=false;
			   break;
			  }	  
		   }

		   if(arr[3-i][i]==pvt || arr[3-i][i]=='T')
				continue;
			   else
			   {
				   temp_test=false;
				   break;
			   }
	   }
       if(temp_test)
		{
			abs_test=true;
			printf("Case #%d: %c won\n",b+1,pvt);
	   }

   }
   
   if(!abs_test)
   {
	   if(dot_fnd)
		   printf("Case #%d: Game has not completed\n",b+1);
	   else
	   printf("Case #%d: Draw\n",b+1);  
   }


   delete []arr;
 }



}