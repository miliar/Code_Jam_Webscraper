#include<cstdio>
//#include<conio.h>
int main()
{
    freopen("C:\\Users\\dell\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\dell\\Desktop\\output.txt","w",stdout);
    char a[4][4];
    int x=0,o=0,xf=0,of=0,g,i,j,t,no=1;

    scanf("%d",&t);
    while(t--)
    {
    x=0; o=0;          
    for(i=0;i<4;i++)          
    scanf("%s",a[i]);
    
    for(i=0;i<4;i++)
    {
       if(a[i][0]=='X')
       {
          x=1;
          o=0;             
         for(j=1;j<4;j++)
         {
            if(a[i][j]!='X' && a[i][j]!='T')
            {
              x=0;
              break;
            }
         }
       }
       else if(a[i][0]=='O')
       {
          x=0;
          o=1;             
         for(j=1;j<4;j++)
         {
            if(a[i][j]!='O' && a[i][j]!='T')
            {
              o=0;
              break;
            }
         }
       }
       else if(a[i][0]=='T')
       {
        if(a[i][1]=='X')
        {
          x=1;
          o=0;              
         for(j=2;j<4;j++)
         {
            if(a[i][j]!='X')
            {
              x=0;
              break;
            }
         }               
                        
        } 
        else if(a[i][1]=='O')
        {
          x=0;
          o=1;              
         for(j=2;j<4;j++)
         {
            if(a[i][j]!='O')
            {
              o=0;
              break;
            }
         }               
                        
        }    
               
       }
       xf=0; of=0;
       if(x==1)
       {
         xf=1;
         break;
       }
       else if(o==1)
       {
          of=1;
          break;
       }
       //columns
       
       if(a[0][i]=='X')
       {
          x=1;
          o=0;             
         for(j=1;j<4;j++)
         {
            if(a[j][i]!='X' && a[j][i]!='T')
            {
              x=0;
              break;
            }
         }
       }
       else if(a[0][i]=='O')
       {
          x=0;
          o=1;             
         for(j=1;j<4;j++)
         {
            if(a[j][i]!='O' && a[j][i]!='T')
            {
              o=0;
              break;
            }
         }
       }
       else if(a[0][i]=='T')
       {
        if(a[1][i]=='X')
        {
          x=1;
          o=0;              
         for(j=2;j<4;j++)
         {
            if(a[j][i]!='X')
            {
              x=0;
              break;
            }
         }               
                        
        } 
        else if(a[1][i]=='O')
        {
          x=0;
          o=1;              
         for(j=2;j<4;j++)
         {
            if(a[j][i]!='O')
            {
              o=0;
              break;
            }
         }               
                        
        }    
               
       }
       xf=0; of=0;
       if(x==1)
       {
         xf=1;
         break;
       }
       else if(o==1)
       {
          of=1;
          break;
       }
       
    }  
    
    if(xf!=1 && of!=1)
    {
        if(a[0][0]=='X')
        {
           x=1; o=0;             
           for(i=1;i<4;i++)
           {
            if(a[i][i]!='X' && a[i][i]!='T')
            {
              x=0;
              break;
            }
         }
       }
       else if(a[0][0]=='O')
        {
           x=0; o=1;             
           for(i=1;i<4;i++)
           {
            if(a[i][i]!='O' && a[i][i]!='T')
            {
              o=0;
              break;
            }
           }
       }
       else if(a[0][0]=='T')
       {
         if(a[1][1]=='X')
         {
          x=1; o=0;               
          for(i=2;i<4;i++)
           {
            if(a[i][i]!='X')
            {
              x=0;
              break;
            }
           }
         } 
         
         else if(a[1][1]=='O')
         {
          x=0; o=1;               
          for(i=2;i<4;i++)
           {
            if(a[i][i]!='O')
            {
              o=0;
              break;
            }
           }                                
         }
       }
            
       if(x==1)
       {
         xf=1;
       }
       else if(o==1)
       {
          of=1;
       }    
                 
    }       
    //right diagonal
    
    if(xf!=1 && of!=1)
    {
             //printf("ghusa\n"); 
        if(a[0][3]=='X')
        {
           x=1; o=0;             
           for(i=1;i<4;i++)
           {
            if(a[i][3-i]!='X' && a[i][3-i]!='T')
            {
              x=0;
              break;
            }
           }
       }
       else if(a[0][3]=='O')
        {
           x=0; o=1;  
           //printf("ghusa\n");           
           for(i=1;i<4;i++)
           {
            if(a[i][3-i]!='O' && a[i][3-i]!='T')
            {
              o=0;
              break;
            }
           }
       }
       else if(a[0][3]=='T')
       {
         if(a[1][2]=='X')
         {
          x=1; o=0;               
          for(i=2;i<4;i++)
           {
            if(a[i][3-i]!='X')
            {
              x=0;
              break;
            }
           }
         } 
         
         else if(a[1][2]=='O')
         {
          x=0; o=1;               
          for(i=2;i<4;i++)
           {
            if(a[i][3-i]!='O')
            {
              o=0;
              break;
            }
           }                                
         }
       }
            
       if(x==1)
       {
         xf=1;
       }
       else if(o==1)
       {
          of=1;
       }    
                 
    }  
    
    if(xf==1)
    printf("Case #%d: X won\n",no);
    else if(of==1)
    printf("Case #%d: O won\n",no);
    else
    {
        g=0;
        for(i=0;i<4;i++)
        {
          for(j=0;j<4;j++)
          {
             if(a[i][j]=='.')
             {
               g=1;
               break;
             }
          }
        }
        if(g==1)
        printf("Case #%d: Game has not completed\n",no);
        else
        printf("Case #%d: Draw\n",no);
    }
    printf("\n");
    no++; 
   } 
   
   
    
    //getch();
    return 0;
}                                             
           
                                                       
                      
       
                                                     
                                                            
