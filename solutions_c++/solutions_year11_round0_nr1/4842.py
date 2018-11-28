#include <iostream>
#include <conio.h>
#include <vector>
#include <stdlib.h>
#include <stdio.h>
#include <sstream>
#include <cstring>
#include <string.h>
#include <iomanip>
#include <cmath>
#include <algorithm>

using namespace std;

int number, amt, i, j, k, k1=0, l, l1=0, ch=0, waste, blue[10000][1000], orange[10000][10000];
int counto, countb;
char color[10000][10000];
int line;

int main()
{
     //freopen("A-small.in","rt",stdin);
     //freopen("A-small.txt","wt",stdout);
     freopen("A-large.in","rt",stdin);
     freopen("A-large.txt","wt",stdout);
     scanf("%d", &line);
     for(i=1;i<=line;i++)
     {
          counto=countb=number=0;
          k=l=0;
          blue[0][l1]=0;
          orange[0][k1]=0;
          scanf("%d", &amt);
          for (j=0;j<amt;j++)
          {
               scanf("%c", &waste);
               scanf("%c", &color[j][ch]);
               scanf("%c", &waste);
               if (color[j][ch]=='O')
               {
                    k++;
                    scanf("%d", &orange[k][k1]);
                    if (j==0)
                    {
                         number = number + orange[k][k1];
                         counto = orange[k][k1];
                    }
                    else if (color[j-1][ch]=='B')
                    {
                         if (j==1)
                         {
                            if ((orange[k][k1]-blue[l][l1])>=1)
                            {
                                number = number + orange[k][k1] - blue[l][l1];
                                counto = orange[k][k1] - blue[l][l1];
                            }
                            else
                            {
                                number++;
                                counto++;
                            }
                         }
                         else
                         {
                             if (orange[k][k1] >= orange[k-1][k1])
                             {
                                if ((orange[k][k1] - orange[k-1][k1])<=countb)
                                {
                                    number++;
                                    countb = 0;
                                    counto = 1;
                                }
                                else if (orange[k][k1]>countb && k==1)
                                {
                                    number = number + orange[k][k1] - countb;
                                    counto = orange[k][k1] - countb;
                                    countb = 0;
                                }
                                else
                                {
                                    number = number + 1 + orange[k][k1] - orange[k-1][k1] - countb;
                                    counto = 1 + orange[k][k1] - orange[k-1][k1] - countb;
                                    countb = 0;
                                }
                             }
                             else
                             {
                                if ((orange[k-1][k1] - orange[k][k1])<=countb)
                                {
                                    number++;
                                    countb = 0;
                                    counto = 1;
                                }
                                else if (orange[k-1][k1]>countb && k==1)
                                {
                                    number = number + orange[k-1][k1] - countb;
                                    counto = orange[k-1][k1] - countb;
                                    countb = 0;
                                }
                                else
                                {
                                    number = number + 1 + orange[k-1][k1] - orange[k][k1] - countb;
                                    counto = 1 + orange[k-1][k1] - orange[k][k1] - countb;
                                    countb = 0;
                                }
                             }
                         }
                    }
                    else
                    {
                         if (orange[k][k1]>=orange[k-1][k1])
                         {
                              number = number + 1 + orange[k][k1] - orange[k-1][k1];
                              counto = counto + 1 + orange[k][k1] - orange[k-1][k1];
                         }
                         else
                         {
                              number = number + 1 + orange[k-1][k1] - orange[k][k1];
                              counto = counto + 1 + orange[k-1][k1] - orange[k][k1];
                         }
                    }
               }
               else
               {
                    l++;
                    scanf("%d", &blue[l][l1]);
                    if (j==0)
                    {
                         number = number + blue[l][l1];
                         countb = blue[l][l1];
                    }
                    else if (color[j-1][ch]=='O')
                    {
                         if (j==1)
                         {
                            if ((blue[l][l1]-orange[k][k1])>=1)
                            {
                                number = number + blue[l][l1] - orange[k][k1];
                                countb = blue[l][l1] - orange[k][k1];
                            }
                            else
                            {
                                number++;
                                countb++;
                            }

                         }
                         else
                         {
                            if (blue[l][l1] >= blue[l-1][l1])
                            {
                                 if ((blue[l][l1] - blue[l-1][l1])<=counto)
                                 {
                                     number++;
                                     counto = 0;
                                     countb = 1;
                                 }
                                 else if (blue[l][l1]>counto && l==1)
                                 {
                                     number = number + blue[l][l1] - counto;
                                     countb = blue[l][l1] - counto;
                                     counto = 0;
                                 }
                                 else
                                 {
                                     number = number + 1 + blue[l][l1] - blue[l-1][l1] - counto;
                                     countb = 1 + blue[l][l1] - blue[l-1][l1] - counto;
                                     counto = 0;
                                 }
                            }
                            else
                            {
                                 if ((blue[l-1][l1] - blue[l][l1])<=counto)
                                 {
                                     number++;
                                     counto=0;
                                     countb=1;
                                 }
                                 else if (blue[l-1][l1]>counto && l==1)
                                 {
                                     number = number + blue[l-1][l1] - counto;
                                     countb = blue[l-1][l1] - counto;
                                     counto = 0;
                                 }
                                 else
                                 {
                                     number = number + 1 + blue[l-1][l1] - blue[l][l1] - counto;
                                     countb = 1 + blue[l-1][l1] - blue[l][l1] - counto;
                                     counto = 0;
                                 }
                            }
                         }
                    }
                    else
                    {
                         if (blue[l][l1]>=blue[l-1][l1])
                         {
                              number = number + 1 + blue[l][l1] - blue[l-1][l1];
                              countb = countb + 1 + blue[l][l1] - blue[l-1][l1];
                         }
                         else
                         {
                              number = number + 1 + blue[l-1][l1] - blue[l][l1];
                              countb = countb + 1 + blue[l-1][l1] - blue[l][l1];
                         }
                    }
               }
          }
          printf("Case #%d: %d\n", i, number);
          k1++;
          l1++;
          ch++;
     }
     fclose(stdin);
     fclose(stdout);
     return 0;
}
