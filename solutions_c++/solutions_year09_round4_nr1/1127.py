#include<iostream>
using namespace std;

int T,num[50],N;

int sort()
{
     int i,j,k,c=0;
     for (i=0;i<N;i++)
     {
          for (j=i;j<N;j++)
              if (num[j] <= i)
                 break;
          for (k=j;k>i;k--)
          {
              swap(num[k-1],num[k]);
              c++;
          }
     }
     return c;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    char c,str[100];
    int i,j,k=1;
    scanf("%d",&T);
    while (T--)
    {
          scanf("%d\n",&N);
          for (i=0;i<N;i++)
          {
              gets(str);
              num[i]=0;
              for (j=0;j<N;j++)
              {
                  if (str[j]=='1')
                     num[i]=j;
              }
          }
          printf("Case #%d: %d\n",k++,sort());
    }
}
