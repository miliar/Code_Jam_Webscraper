#include<iostream>
#include<algorithm>
using namespace std;
char str[60][60];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,n,k;
    int x,y,i,j;
    scanf("%d",&t);
    for(x=0;x<t;x++)
    {
                    scanf("%d%d",&n,&k);
                    for(i=0;i<n;i++)
                    {
                                    scanf("%s",str[i]);
                                    int r=n-1;
                                    for(j=n-1;j>=0;j--)
                                    {
                                                       if(str[i][j]!='.')
                                                       {
                                                                         swap(str[i][j],str[i][r]);
                                                                         r--;
                                                                         }
                                                       }
                                    }
                    
                    /*for(i=0;i<n;i++)
                    {
                                    for(j=0;j<n;j++)
                                    printf("%c",str[i][j]);
                                    printf("\n");
                                    }*/
                    
                    int rr=0,bb=0;
                    for(i=0;i<n;i++)
                    {
                                    for(j=0;j<=n-k;j++)
                                    {
                                                       int checkr=1,checkb=1;
                                                       for(y=0;y<k;y++)
                                                       {
                                                                       if(str[i][j+y]!='R')
                                                                       checkr=0;
                                                                       if(str[i][j+y]!='B')
                                                                       checkb=0;
                                                                       }
                                                       if(checkr)
                                                       rr=1;
                                                       if(checkb)
                                                       bb=1;
                                                       }
                                    }
                    for(i=0;i<=n-k;i++)
                    {
                                       for(j=0;j<n;j++)
                                       {
                                                       int checkr=1,checkb=1;
                                                       for(y=0;y<k;y++)
                                                       {
                                                                       if(str[i+y][j]!='R')
                                                                       checkr=0;
                                                                       if(str[i+y][j]!='B')
                                                                       checkb=0;
                                                                       }
                                                       if(checkr)
                                                       rr=1;
                                                       if(checkb)
                                                       bb=1;
                                                       }
                                       }
                    for(i=0;i<=n-k;i++)
                    {
                                    for(j=0;j<=n-k;j++)
                                    {
                                                       int checkr=1,checkb=1;
                                                       for(y=0;y<k;y++)
                                                       {
                                                                       if(str[i+y][j+y]!='R')
                                                                       checkr=0;
                                                                       if(str[i+y][j+y]!='B')
                                                                       checkb=0;
                                                                       }
                                                       if(checkr)
                                                       rr=1;
                                                       if(checkb)
                                                       bb=1;
                                                       }
                                    }
                    for(i=0;i<=n-k;i++)
                    {
                                    for(j=k-1;j<n;j++)
                                    {
                                                       int checkr=1,checkb=1;
                                                       for(y=0;y<k;y++)
                                                       {
                                                                       if(str[i+y][j-y]!='R')
                                                                       checkr=0;
                                                                       if(str[i+y][j-y]!='B')
                                                                       checkb=0;
                                                                       }
                                                       if(checkr)
                                                       rr=1;
                                                       if(checkb)
                                                       bb=1;
                                                       }
                                    }
                    
                    printf("Case #%d: ",x+1);
                    if(rr&&bb)
                    printf("Both\n");
                    else
                    {
                        if(rr)
                        printf("Red\n");
                        else if(bb)
                        printf("Blue\n");
                        else
                        printf("Neither\n");
                        }
                    }
    //scanf(" ");
    return 0;
    }
