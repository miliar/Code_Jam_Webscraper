#include <iostream>
#include<cstdio>
//#include<conio.h>

using namespace std;

int main() {
    
    int t,k;
    
    FILE *fp,*fp1;
    fp=fopen("input.txt","r");
     fp1=fopen("output1.txt","w");
     char ch;
    fscanf(fp,"%d",&t);
   // printf("%d\n",t);
    fscanf(fp,"%c",&ch);
   // printf("%d",t);
    for(k=1;k<=t;k++)
    {
        
         int flag=0,i,j,countx,counto,countt,countdot;
         
        char a[5][5]={'.'};
      /*   for(i=0;i<4;i++)
        {   scanf("%s",a[i]);
            // scanf("%c",&ch);
        } */
        
        for(i=0;i<4;i++)
         {
             for(j=0;j<4;j++)
              fscanf(fp,"%c",&a[i][j]);
              
              fscanf(fp,"%c",&ch);
         }
          
                
                
           for(i=0;i<4;i++)                         //summing the rows
            {
                 countx=counto=countdot=countt=0;
                for(j=0;j<4;j++)
                {
                    if(a[i][j]=='T')
                      countt++;
                      
                      else if(a[i][j]=='X')
                       countx++;
                       
                       else if(a[i][j]=='O')
                        counto++;
                        
                        else if(a[i][j]=='.')
                           countdot++;
                }
                
                if(countx==4||countx+countt==4)
                 {
                     fprintf(fp1,"Case #%d: X won\n",k);
                    /* flag=1;
                     break; */
                     goto abc;
                 }
                 
                 else if(counto==4||counto+countt==4)
                 {
                     fprintf(fp1,"Case #%d: O won\n",k);
                    /* flag=1;
                     break; */
                     goto abc;
                 }
                 
            }
            
            
         //   if(flag==0)
          //  {
                 for(j=0;j<4;j++)                         //summing the columns
            {
                 countx=counto=countdot=countt=0;
                for(i=0;i<4;i++)
                {
                    if(a[i][j]=='T')
                      countt++;
                      
                      else if(a[i][j]=='X')
                       countx++;
                       
                       else if(a[i][j]=='O')
                        counto++;
                        
                        else if(a[i][j]=='.')
                           countdot++;
                }
                
                if(countx==4||countx+countt==4)
                 {
                     fprintf(fp1,"Case #%d: X won\n",k);
                    /* flag=1;
                     break; */
                     goto abc;
                 }
                 
                 else if(counto==4||counto+countt==4)
                 {
                     fprintf(fp1,"Case #%d: O won\n",k);
                   /*  flag=1; 
                     
                     break; */
                     goto abc;
                 }
                 
            }
            //}
            
           // if(flag==0)
          //  {
                 countx=counto=countdot=countt=0;
                for(i=0;i<4;i++)
                 for(j=0;j<4;j++)
                  {
                      if(i==j)
                       {
                          if(a[i][j]=='T')
                      countt++;
                      
                      else if(a[i][j]=='X')
                       countx++;
                       
                       else if(a[i][j]=='O')
                        counto++;
                        
                        else if(a[i][j]=='.')
                           countdot++; 
                       }
                  }
                  
                  if(countx==4||countx+countt==4)
                  {
                       fprintf(fp1,"Case #%d: X won\n",k);
                    /* flag=1;
                     break; */
                     goto abc;
                  } 
                  
                  else if(counto==4||counto+countt==4)
                 {
                     fprintf(fp1,"Case #%d: O won\n",k);
                    /* flag=1;
                     break; */
                     goto abc;
                 }
                  
                  
          //  }
            
        //    if(flag==0)
           // {
                 countx=counto=countdot=countt=0;
                for(i=0;i<4;i++)
                 for(j=0;j<4;j++)
                  {
                      if(i+j==3)
                       {
                          if(a[i][j]=='T')
                      countt++;
                      
                      else if(a[i][j]=='X')
                       countx++;
                       
                       else if(a[i][j]=='O')
                        counto++;
                        
                        else if(a[i][j]=='.')
                           countdot++; 
                       }
                  }
                  
                  if(countx==4||countx+countt==4)
                  {
                       fprintf(fp1,"Case #%d: X won\n",k);
                     /* flag=1;
                     break; */
                     goto abc;
                  }
                  
                  else if(counto==4||counto+countt==4)
                 {
                     fprintf(fp1,"Case #%d: O won\n",k);
                    /* flag=1;
                     break; */
                     goto abc;
                 } 
       //     }
            
           // if(flag==0)
            //{
                 countdot=0;
                for(i=0;i<4;i++)
                 for(j=0;j<4;j++)
                  if(a[i][j]=='.')
                   countdot++;
                   
                   if(countdot==0)
                  {  fprintf(fp1,"Case #%d: Draw\n",k);
                      goto abc; }
                    
                    else
                   { fprintf(fp1,"Case #%d: Game has not completed\n",k);
                    goto abc; }
                    
                    abc:
            //}
        fscanf(fp,"%c",&ch); //to get the new line char
    }
    
      fclose(fp);
      fclose(fp1);
  //  getch();
	return 0;
}
