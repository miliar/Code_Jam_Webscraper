#include<stdio.h>
#include<conio.h>

char ch, tic[4][4];

int check(int i, int j, int inci, int incj)
{
              ch=tic[i][j];
     while(i<4&&j<4)
     {
               if(tic[i][j]=='.')
               return 0;
               
               
               if(tic[i][j]=='T')
               {
                          i=i+inci;
                          j=j+incj;
                          continue;
               }
               
               if(ch=='T')
               ch=tic[i][j];
               
               else if(tic[i][j]!=ch)
               return 0;
               
               i+=inci;
               j+=incj;
     }
     
     return 1;
     
}
               

               
               
               
               
               

int main()
{
    int i,j,t,k=1, is_empty=0,flag;
    FILE *file, *out;
    file=fopen("inputSA.txt", "r");
    out=fopen("outputSA.txt", "w");
    fscanf(file,"%d", &t);
    while(k<=t)
    {
               is_empty=0;
               for(i=0;i<4;i++)
               {
                               for(j=0;j<4;j++)
                               {
                               fscanf(file,"%c",&tic[i][j]);
                               if(tic[i][j]=='\n')
                               j--;
                               if(tic[i][j]=='.')
                                is_empty=1;
                               }
               }

               
               
               ///1st element
               if(check(0,0,1,0))
               fprintf(out,"Case #%d: %c won\n",k,ch);
               
               else if(check(0,0,1,1))
               fprintf(out,"Case #%d: %c won\n",k,ch);
               
                else if(check(0,0,0,1))
               fprintf(out,"Case #%d: %c won\n",k,ch);
               
                else if(check(0,1,1,0))
               fprintf(out,"Case #%d: %c won\n",k,ch);
               
                else if(check(0,2,1,0))
               fprintf(out,"Case #%d: %c won\n",k,ch);
               
                else if(check(0,3,1,-1))
               fprintf(out,"Case #%d: %c won\n",k,ch);
               
                else if(check(0,3,1,0))
               fprintf(out,"Case #%d: %c won\n",k,ch);
               
               else if(check(1,0,0,1))
               fprintf(out,"Case #%d: %c won\n",k,ch);
               
               else if(check(2,0,0,1))
               fprintf(out,"Case #%d: %c won\n",k,ch);
               
               else if(check(3,0,0,1))
               fprintf(out,"Case #%d: %c won\n",k,ch);
               
               
               else if(is_empty==1)
               fprintf(out,"Case #%d: Game has not completed\n",k);
               
               else
               fprintf(out,"Case #%d: Draw\n",k);
              

                         k++;
    }
    fclose(file);
    fclose(out);
    printf("done");
    getch();
    return 0;
}
