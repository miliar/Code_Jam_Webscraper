#include <stdio.h>
#include <iostream>
#include <conio.h>

using namespace std;

double wp[105],owp[105],oowp[105];
char str[105][105];

int main()
{
    int c = 0,T,N,i,j,count1,count2,count3,k;
    double sum;
    char ch;

    cin>>T;
    while(T--)
    {
        c++;
        cin>>N;
        for(i = 0;i<N;i++)
        {
            for(j = 0;j<N;j++)
             cin>>str[i][j];
        }
        for(i = 0;i<N;i++)
        {
            count1 = 0;
            count2 = 0;
            for(j = 0;j<N;j++)
            {
                if(str[i][j]!='.')
                count1++;
                if(str[i][j]=='1')
                count2++;
            }
            wp[i] =count2/(double)count1;
        }


        for(i= 0;i<N;i++)
        {
            count1 = 0;
            sum = 0;
            for(j = 0;j<N;j++)
              if(str[i][j]!='.')
              {
               count1++;
               ch = str[j][i];
               str[j][i] = '.';
               count2 = 0;count3 = 0;
               for(k = 0;k<N;k++)
               {
                   if(str[j][k]!='.')
                   count2++;
                   if(str[j][k]=='1')
                   count3++;
               }
               sum+=count3/(double)count2;
               str[j][i] = ch;
              }
              owp[i] = sum/count1;
        }
        for(i= 0;i<N;i++)
        {
            sum = 0;
            count1= 0;
            for(j= 0;j<N;j++)
             if(str[i][j]!='.')
             {
                 count1++;
                 sum+=owp[j];
             }
             oowp[i] = sum/count1;
        }
        printf("Case #%d:\n",c);
      for(i=0;i<N;i++)
          printf("%0.8lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
    }
    return 0;
}
