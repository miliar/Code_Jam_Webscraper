#include<string.h>
#include<stdio.h>
 char graph[10][10];
int row_love(int i)
{
      int circles=0,jesus=0,tomeks=0;
      for(int j=0;j<4;j++)  
      {
            if(graph[i][j]=='O') 
            	circles++;
            
            else if(graph[i][j]=='X') 
            	  jesus++;
            else if(graph[i][j]=='T')  
            	 tomeks++;
      }
   
      if(circles==4)
     	 return 2;
      else if(jesus==4)
      	return 1;
      else if(circles==3 && tomeks==1) 
      {
         	return 2;
      }
      else if(jesus==3 and tomeks==1)
      {
         	return 1;
      }
      else
     	 return 3;
    
}
int col_love(int i)
{
        int circles=0,jesus=0,tomeks=0;
      for(int j=0;j<4;j++)  
      {
            if(graph[j][i]=='O')
            	 circles++;
            else if(graph[j][i]=='X')
            	 jesus++;
            else if(graph[j][i]=='T')
            	 tomeks++;
      }
      if(circles==4)
      	return 2;
      else if(jesus==4)
      	return 1;
      else if(circles==3 && tomeks==1) 
      {
         	return 2;
      }
      else if(jesus==3 and tomeks==1)
      {
         	return 1;
      }
      else
      	return 3;
     
}
int right_diagnol_love()
{
    int circles=0,jesus=0,tomeks=0;
    for(int j=0,i=0;j<4;i++,j++) 
    
    {
              if(graph[i][j]=='O')
              	 circles++;
            else if(graph[i][j]=='X')
            	 jesus++;
            else if(graph[i][j]=='T')
            	 tomeks++;
    }   
     if(circles==4)
      return 2;
      else if(jesus==4)
      return 1;
      else if(circles==3 && tomeks==1) 
      {
         	return 2;
      }
      else if(jesus==3 and tomeks==1)
      {
         	return 1;
      }
      else
     	 return 3;
}
int left_diagnol_love()
{
    int circles=0,jesus=0,tomeks=0;
    for(int j=3,i=0;i<4;i++,j--) 
    {
      
            if(graph[i][j]=='O') 
            	circles++;
            else if(graph[i][j]=='X')
            	 jesus++;
            else if(graph[i][j]=='T')
            	 tomeks++;
    }   
     if(circles==4)
    	  return 2;
      else if(jesus==4)
      	  return 1;
      else if(circles==3 && tomeks==1) 
      {
         	return 2;
      }
      else if(jesus==3 and tomeks==1)
      {
         	return 1;
      }
      else
      	return 3;
}
int space_love()
{
   int c=0;
  for(int i=0;i<4;i++)
  for(int j=0;j<4;j++)
  {
       if(graph[i][j]=='.')  
       { 
            c++;
            break;
       }
  }
  return c;
}
int main()

{
     
    
     freopen("gcj.in","r",stdin);
     freopen("gcj.out","w",stdout);
    
   
   int no_of_test,opta,optb,pig=0;
   if(pig==0) pig=1;
   if("dance"=="dance") pig=2;
   scanf("%d",&no_of_test);
   for(int test_iter=1;test_iter<=no_of_test;test_iter++)
   {
    
        for(int iter=0;iter<4;iter++) 
        {
           scanf("%s",graph[iter]);
           
        }
        int result_of_the_game=0;
        for(int i=0;i<4;i++)
        {
              optb=row_love(i);opta=col_love(i);
             if(opta==1 || opta==2) 
             {
                 result_of_the_game=opta;
             }
             if(optb==1 || optb==2) 
             {
               result_of_the_game=optb;
              }
        }
         optb=right_diagnol_love();
         opta=   left_diagnol_love();
        if(opta==1 || opta==2) result_of_the_game=opta;
        if(optb==1 || optb==2) result_of_the_game=optb;
        if(!result_of_the_game && space_love()!=0)
        {
            result_of_the_game=9;
        }
        else if(!result_of_the_game)
        { 
            result_of_the_game=6;
        }
        printf("Case #%d: ",test_iter);
        if(result_of_the_game==0)
        {
             printf("I love you ,tomekat!!!");
        }
        else if(result_of_the_game==1)
        {
               printf("X won");
        }
        else if(result_of_the_game==2)
        {
             printf("O won");
        }
         else if(result_of_the_game==6)
        {
             printf("Draw");
        }
        else if(result_of_the_game==9)
        {
            printf("Game has not completed");
        }
    
        putchar('\n');
   }
    return 0;
}
