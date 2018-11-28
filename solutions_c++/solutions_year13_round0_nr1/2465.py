#include<stdio.h>
#include<stdlib.h>
FILE *fin  = fopen ("A-small-practice.in", "r");
FILE *fout = fopen ("A-small-practice.out", "w");
char a[4][4];
void solve(int);
int judge(int,int);



int judge(int x,int y)
{
    char ch = a[x][y];
    int i;
    int total = 0;
    for(i=0;i<4;i++) if(a[x][i]==ch || a[x][i] == 'T') total++;
    if (total == 4) return 1;
   // fprintf(fout,"%d\n",total);
    
    total = 0;
    for(i=0;i<4;i++) if(a[i][y]==ch || a[i][y] == 'T') total++;
    if (total == 4) return 1;
  //  fprintf(fout,"%d\n",total);
    
    total = 0;
    if(x==y){
             for(i=0;i<4;i++)if(a[i][i]==ch || a[x][i] == 'T') total++;
             if (total == 4) return 1;
             }
   // fprintf(fout,"%d\n",total);
              
    total = 0; 
    if(x+y==3){
               for(i=0;i<4;i++) if(a[i][3-i]==ch || a[i][3-i] == 'T') total++;
               if(total==4) return 1;
               }
   // fprintf(fout,"%d\n",total);
    
    return 0;
}

void solve(int n)
{
    
    int total = 0;
    int i,j;
    for(i=0;i<4;i++)
     for(j=0;j<4;j++)
     {
       if(a[i][j]=='O' || a[i][j] == 'X')             
       if (judge(i,j)==1) {
                          fprintf(fout,"Case #%d: %c won\n",n+1,a[i][j]);
                          return;
                        }
       
        if(a[i][j]=='O' || a[i][j] == 'X' || a[i][j]=='T') total++;
         
     }
     
     //fprintf(fout,"%d\n",total);
     if(total == 16){
                 fprintf(fout,"Case #%d: Draw\n",n+1);
                 
              }else{
                 fprintf(fout,"Case #%d: Game has not completed\n",n+1);   
              } 
}


int main()
{
    int i,j,T,k;
    fscanf(fin,"%d\n",&T);
    for(int i=0;i<T;i++)
    {
         for(j=0;j<4;j++)
              {
              fscanf(fin,"%s\n",a[j]);
              //fprintf(fout,"%s\n",a[j]);
              }
    
              
         solve(i); 
        // fscanf(fin,"\n");
    }
    return 0;
}
