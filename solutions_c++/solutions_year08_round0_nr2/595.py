#include<stdio.h>
#include<algorithm>
#define MAXSIZE 101

struct TList
{
       int start;
       int end;
       int isA;
       bool operator<(const TList& l) const
       {
            return start<l.start;
       }
}train[MAXSIZE*2];
int NA,NB,total,T;
int idle_A[MAXSIZE],idle_B[MAXSIZE],len_A,len_B,cnt_A,cnt_B;

int find_item(int array[],int len,int element)
{
    int i;
    for (i=0;i<len;i++)
        if (array[i]<=element)
           return i;
    return len;
}
void delete_item(int array[],int& len,int index)
{
     int i;
     for (i=index+1;i<len;i++)
         array[i-1]=array[i];
     len--;
}
char from[32],to[32];
inline int convert_time(char* str)
{
       return (10*(str[0]-'0')+(str[1]-'0'))*60+10*(str[3]-'0')+(str[4]-'0');
}
int main()
{
    int cas,i,j,index;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&cas);
    for (i=1;i<=cas;i++)
    {
        scanf("%d%d%d",&T,&NA,&NB);
        total=NA+NB;
        for (j=0;j<total;j++)
        {
            scanf("%s %s",from,to);
            train[j].start=convert_time(from);
            train[j].end=convert_time(to);
            if (j<NA)
               train[j].isA=1;
            else
                train[j].isA=0;
        }
        std::sort(train,train+total);
        //for (j=0;j<total;j++)
        //    printf("start=%d end=%d isA=%d\n",train[j].start,train[j].end,train[j].isA);
        cnt_A=cnt_B=0;
        len_A=len_B=0;
        for (j=0;j<total;j++)
        {
            if (train[j].isA)
            {
                index=find_item(idle_A,len_A,train[j].start);
                if (index>=len_A)
                    cnt_A++;
                else
                    delete_item(idle_A,len_A,index);
                idle_B[len_B++]=train[j].end+T;
            }
            else
            {
                index=find_item(idle_B,len_B,train[j].start);
                if (index>=len_B)
                   cnt_B++;
                else
                    delete_item(idle_B,len_B,index);
                idle_A[len_A++]=train[j].end+T;
            }
        }
        printf("Case #%d: %d %d\n",i,cnt_A,cnt_B);
    }
    return 0;
}
