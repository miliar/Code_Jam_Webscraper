#include<stdio.h>
#include<string.h>
int main()
{
    int T,i,j,x[4],y[4],d1,d2,p,won;;
    int notf=1;
    char q[5][5];
    scanf("%d",&T);
    
    for(p=1;p<=T;p++)
    {
    notf=0;
        won=0;
    printf("Case #%d: ",p);
    d1=0;d2=0;
    y[0]=0;
    y[1]=0;
    y[2]=0;
    y[3]=0;
            for( i=0;i<4;i++)
            {
                 x[i]=0;
                 scanf("%s",q[i]);
                 for( j=0;j<4;j++)
                 {
                      if(q[i][j]=='.')
                                      notf=1;
                      x[i]+=q[i][j];
                      y[j]+=q[i][j];
                      if(i==j)
                              d1+=q[i][j];
                      if(i+j==3)
                                d2+=q[i][j];
                 }    
            }
            
            if(d1==348 || d1==352 || d2==348 || d2==352)
            {
                          printf("X won\n");
                          continue;
            }
            else if(d1==321 || d1==316 || d2==321 || d2==316)
            {
                                         printf("O won\n");
                                         continue;
            }
            for(i=0;i<4;i++)
            {
                            if(x[i]==348 || x[i]==352 || y[i]==348 || y[i]==352)
                            {
                                         printf("X won\n");
                                         won=1;
                                         break;
                            }
                            else if(x[i]==321 || x[i]==316 || y[i]==321 || y[i]==316)
                            {
                                         printf("O won\n");
                                         won=1;
                                         break;
                            }
            }
            if(won==1)
                      continue;
            if(notf==1)
                       printf("Game has not completed\n");
            else
                printf("Draw\n");
    }
}
