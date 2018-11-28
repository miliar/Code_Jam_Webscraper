
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main()
{
    FILE * fin, * fout;
    int t,i,j,k,p,r1,r2,n,m,flag,fl,sum,max,ord,len[10010],stan[10010],check[20];
    char c,s[10010][11],dic[30];
    fin=fopen("B-small-attempt2.in","r");
    fout=fopen("2.out","w");
    fscanf(fin,"%d",&t);
    for (i=1;i<=t;i++)
    {
        fscanf(fin,"%d %d",&n,&m);
        fprintf(fout,"Case #%d:",i);
        for (j=1;j<=n;j++)
        {
            fscanf(fin,"%s",s[j]);
            len[j]=strlen(s[j]);
            }
        for (j=1;j<=m;j++)
        {
            max=ord=0;
            for (k=1;k<=26;k++) fscanf(fin,"%c",&dic[k]);
            fscanf(fin,"%c",&c);
            for (k=1;k<=n;k++)
            {
                for (p=0;p<=15;p++) check[p]=1;
                sum=0;
                for (p=1;p<=n;p++)
                {
                    if (len[p]==len[k]) stan[p]=1;
                    else stan[p]=0;
                    }
                for (p=1;p<=26;p++)
                {
                    for (flag=0,fl=0,r1=1;r1<=n;r1++)
                          if (stan[r1])
                          {
                                       fl=1;
                                       for (r2=0;r2<len[r1];r2++)
                                           if ((s[r1][r2]==dic[p])&&(check[r2]))
                                           {
                                                            flag=1;
                                                            break;
                                                            }
                                       }
                    if (fl==0) break;
                    if (flag)
                    {
                             for (fl=0,r1=0;r1<len[k];r1++)
                                 if (s[k][r1]==dic[p])
                                 {
                                                      check[r1]=0;
                                                      fl=1;
                                                      }
                             if (fl==0) sum++;
                             for (fl=1,r1=0;r1<len[k];r1++)
                                 if (check[r1]==1)
                                 {
                                                  fl=0;
                                                  break;
                                                  }
                             if (fl) break;
                             for (r1=1;r1<=n;r1++)
                                   if (stan[r1])
                                   {
                                                for (r2=0;r2<len[k];r2++)
                                                      if ((check[r2]==0)&&(s[r1][r2]!=s[k][r2]))
                                                      {
                                                                                                stan[r1]=0;
                                                                                                break;
                                                                                                }
                                                }
                             }
                    }
                if ((max<sum)||(max==0))
                {
                                        max=sum;
                                        ord=k;
                                        }
                }
            fprintf(fout," %s",s[ord]);
            }
        fprintf(fout,"\n");
        }
    fclose(fin);
    fclose(fout);
    return 0;
    }





