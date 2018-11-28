#include<iostream>
#include<cstdio>
using namespace std;

char mat[51][51];

  int checkredtiles(int row,int col)
    {
     if((mat[row][col]=='#')&&(mat[(row+1)][col]=='#')&&(mat[row][(col+1)]=='#')&&(mat[(row+1)][(col+1)]=='#'))
       {
           mat[row][col]='/';
          mat[row][col+1]='\\';
          mat[row+1][col]='\\';
           mat[row+1][col+1]='/';
           
           return 1;
           
       }    
       return 0;    
    }
      
  int main()
    {
         freopen("input.txt","r",stdin);
         freopen("output.txt","w",stdout);
         
         int t,tc=1,r,c;

         for(scanf("%d",&t);tc<=t;tc++)
          {
              printf("Case #%d:\n",tc);
            scanf("%d %d\n",&r,&c);
               for(int row=1;row<=r;row++)
                {
                    for(int col=1;col<=c;col++)
                    {
                        scanf("%c",&mat[row][col]);
                    }    
                    scanf("\n");
                }    
             int flag=0;   
              for(int row=1;row<=r;row++)
                {
                    for(int col=1;col<=c;col++)
                    {
                        if(mat[row][col]=='#')
                        {

                        if(!checkredtiles(row,col))
                           {
                           printf("Impossible\n");
                           flag=1;
                           break;
                           }    
                         }             
                    }
                    if(flag==1)
                       break; 
                   }        
                    
                    if(flag==0)
                     {
                          for(int row=1;row<=r;row++)
                          {
                             for(int col=1;col<=c;col++)
                             {
                              printf("%c",mat[row][col]);
                              }    
                                      printf("\n");
                 
                          }    
                     }    
                
          }        
                
                //system("PAUSE");
                return 0;
    }    

    
