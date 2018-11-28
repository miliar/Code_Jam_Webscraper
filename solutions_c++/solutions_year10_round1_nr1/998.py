#include<stdio.h>
#include<conio.h>
int main()
{
    int T,K,N,i,j,output=0,test=0,k,m,n;
    char a[51][51],b[51][51];
    FILE *fp1, *fp2;
    fp1 = fopen ( "A-large(2).in", "r" ) ;
    if ( fp1 == NULL )
    {
    puts ( "Cannot open file" ) ;
    }
    else
    {
        fp2 = fopen("A_Ans.txt", "w");
        fscanf(fp1,"%d",&T);
    for(n=0;n<T;n++)
    {fscanf(fp1,"%d",&N);
    fscanf(fp1,"%d",&K);
    output=0;
    for(i=0;i<N;i++)
    {                for(j=0;j<N;j++)
                                    if(j==0)
                                            fscanf(fp1," %c",&b[i][j]);
                                    else
                                        fscanf(fp1,"%c",&b[i][j]);
    }
    for(i=0;i<N;i++)
    {                for(j=0;j<N;j++)
                                    a[i][j]=b[N-j-1][i];
    }
    for(k=0;k<N;k++)
    {
    for(i=N-1;i>0;i--)
                      for(j=0;j<N;j++)
                                      if(a[i-1][j]!='.'&&a[i][j]=='.')
                                      {
                                                       a[i][j]=a[i-1][j];
                                                       a[i-1][j]='.';
                                      }
    for(i=0;i<N-1;i++)
                      for(j=0;j<N;j++)
                                      if(a[i+1][j]=='.'&&a[i][j]!='.')
                                      {
                                                       a[i+1][j]=a[i][j];
                                                       a[i][j]='.';
                                      }
    }
    for(i=0;i<N;i++)
                    for(j=0;j<N;j++)
                                    if(a[i][j]!='.')
                                    {
                                                    k=j;
                                                    test=1;
                                                    while(a[i][k+1]==a[i][k])
                                                    {
                                                                             test++;
                                                                             
                                                                             if(test==K)
                                                                              {if(a[i][j]=='R')
                                                                                               output=output+1;
                                                                               else if(a[i][j]=='B')
                                                                                    output=output+10;
                                                                                              break;}
                                                                              k++;
                                                                             if(k>=N)
                                                                                     break;
                                                    }
                                                    test=1;
                                                    k=i;
                                                    while(a[k+1][j]==a[k][j])
                                                    {
                                                                             test++;
                                                                             k++;
                                                                             if(k>=N)
                                                                                     break;
                                                                             if(test==K)
                                                                              {if(a[i][j]=='R')
                                                                                               output=output+1;
                                                                               else if(a[i][j]=='B')
                                                                                    output=output+10;          break;}
                                                    }
                                                    test=1;
                                                    k=i;
                                                    m=j;
                                                    while(a[k+1][m-1]==a[k][m])
                                                    {
                                                                             test++;
                                                                             k++;
                                                                             m--;
                                                                             if(k>=N)
                                                                                     break;
                                                                             if(m<0)
                                                                                    break;
                                                                             if(test==K)
                                                                              {if(a[i][j]=='R')
                                                                                               output=output+1;
                                                                               else if(a[i][j]=='B')
                                                                                    output=output+10;          break;}
                                                    }
                                                    test=1;
                                                    k=i;
                                                    m=j;
                                                    while(a[k+1][m+1]==a[k][m])
                                                    {
                                                                             test++;
                                                                             k++;
                                                                             m++;
                                                                             if(k>=N || m>=N)
                                                                                     break;
                                                                             if(test==K)
                                                                              {if(a[i][j]=='R')
                                                                                               output=output+1;
                                                                               else if(a[i][j]=='B')
                                                                                    output=output+10;          break;}
                                                    }
                                    }
                                    
    if(output>=10)
                  if((output%10)!=0)
                                    fprintf(fp2,"Case #%d: Both\n",n+1);
                  else
                      fprintf(fp2,"Case #%d: Blue\n",n+1);
    else
        if((output%10)!=0)
                                    fprintf(fp2,"Case #%d: Red\n",n+1);
                  else
                      fprintf(fp2,"Case #%d: Neither\n",n+1);
}
fclose(fp2);
fclose(fp1);
}
}
