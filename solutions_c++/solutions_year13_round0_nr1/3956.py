#include<stdio.h>
#include<string.h>
int main()
{
    
   int i,j,k,x,o,tc,t,ans;
   FILE *fp1,*fp2;
   fp1=fopen("A-large.in","r");
   fp2=fopen("Goutput.txt","w");
   fscanf(fp1,"%d\n",&t) ;
   k=1;
   while(t--)
   {
       char a[4][4]={'0'};
       
       for(i=0;i<4;i++)
       fscanf(fp1,"%s\n",a[i]);
       fflush(stdin);
      
       x=o=0;
       for(i=0;i<=3;i++)
       {
               if((a[i][0]=='X' ||a[i][0]=='T') && (a[i][1]=='X' ||a[i][1]=='T')&&(a[i][2]=='X' ||a[i][2]=='T')&&(a[i][3]=='X' ||a[i][3]=='T'))
               {
                   x=1;
               }
               else if((a[i][0]=='O' ||a[i][0]=='T') && (a[i][1]=='O' ||a[i][1]=='T')&&(a[i][2]=='O' ||a[i][2]=='T')&&(a[i][3]=='O' ||a[i][3]=='T'))
               {
                   o=1;
               }
               
        }
        for(i=0;i<=3;i++)
        {
               if((a[0][i]=='X' ||a[0][i]=='T') && (a[1][i]=='X' ||a[1][i]=='T')&&(a[2][i]=='X' ||a[2][i]=='T')&&(a[3][i]=='X' ||a[3][i]=='T'))
               {
                   x=1;
               }
               else if((a[0][i]=='O' ||a[0][i]=='T') && (a[1][i]=='O' ||a[1][i]=='T')&&(a[2][i]=='O' ||a[2][i]=='T')&&(a[3][i]=='O' ||a[3][i]=='T'))
               {
                   o=1;
               }
               
        }
           
        if((a[0][0]=='O' ||a[0][0]=='T') && (a[1][1]=='O' ||a[1][1]=='T')&&(a[2][2]=='O' ||a[2][2]=='T')&&(a[3][3]=='O' ||a[3][3]=='T'))
               o=1;
        else if((a[0][0]=='X' ||a[0][0]=='T') && (a[1][1]=='X' ||a[1][1]=='T')&&(a[2][2]=='X' ||a[2][2]=='T')&&(a[3][3]=='X' ||a[3][3]=='T'))
               x=1;
        else if((a[0][3]=='O' ||a[0][3]=='T') && (a[1][2]=='O' ||a[1][2]=='T')&&(a[2][1]=='O' ||a[2][1]=='T')&&(a[3][0]=='O' ||a[3][0]=='T'))
               o=1;
        else if((a[0][3]=='X' ||a[0][3]=='T') && (a[1][2]=='X' ||a[1][2]=='T')&&(a[2][1]=='X' ||a[2][1]=='T')&&(a[3][0]=='X' ||a[3][0]=='T'))
               x=1;
        
        if(x==1)
        fprintf(fp2,"Case #%d: X won\n",k);
        else if(o==1)
        fprintf(fp2,"Case #%d: O won\n",k);
        else if(x==o)
        {
                tc=0;
                for(i=0;i<4;i++)
                {
                    for(j=0;j<4;j++)
                    {
                        if(a[i][j]=='.')
                        tc=1;
                    }
                }
                if(tc==0)
                fprintf(fp2,"Case #%d: Draw\n",k);
                else if(tc==1)
                fprintf(fp2,"Case #%d: Game has not completed\n",k);
        }
            k++;
       }
       return 0;
   }
