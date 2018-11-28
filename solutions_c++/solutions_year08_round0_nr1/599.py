#include<stdio.h>
#include<string.h>
#include<algorithm>
#define MAXSIZE 101
#define MAXS    100

struct String
{
       char str[MAXSIZE];
       bool operator<(const String& s) const
       {
            return strcmp(str,s.str)<0;
       }
}engine[MAXS];

char word[MAXSIZE];
int bi_search(char word[]);

bool appeared[MAXS];
int cnt,N,Q,change;

int main()
{
    int T,i,j,k,index;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for (i=1;i<=T;i++)
    {
        scanf("%d",&N);
        getchar();
        for (j=0;j<N;j++)
        {
            gets(engine[j].str);
            //printf("%s\n",engine[j].str);
        }
        std::sort(engine,engine+N);
        scanf("%d",&Q);
        getchar();
        for (j=0;j<N;j++)
            appeared[j]=false;
        change=0;
        cnt=N;
        while (Q--)
        {
              gets(word);
              index=bi_search(word);
              if (index>=0 && !appeared[index])
              {
                  appeared[index]=true;
                  cnt--;
                  if (!cnt)
                  {
                      change++;
                      for (k=0;k<N;k++)
                          appeared[k]=false;
                      appeared[index]=true;
                      cnt=N-1;
                  }
              }
        }
        printf("Case #%d: %d\n",i,change);
        
    }
    return 0;
}
int bi_search(char word[])
{
     int left,right,mid,cmp;
     left=0;
     right=N-1;
     while (left<=right)
     {
           mid=(left+right)>>1;
           cmp=strcmp(engine[mid].str,word);
           if (cmp==0)
              return mid;
           else if (cmp<0)
              left=mid+1;
           else
               right=mid-1;
     }
     return -1;
}
