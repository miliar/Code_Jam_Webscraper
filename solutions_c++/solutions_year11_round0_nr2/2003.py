#include<iostream>

using namespace std;

char combine[26][26];

char opposed[26][26];

char list[105];

char newlist[105];
int f(int N)
{
    int p=0;

    for(int i=0;i<N;i++)
    {
        if(p>0 && combine[newlist[p-1]-'A'][list[i]-'A']!=0)
        {
            newlist[p-1]=combine[newlist[p-1]-'A'][list[i]-'A'];
        }
        else
            newlist[p++]=list[i];

        for(int j=0;j<p-1;j++)
        {
            if( opposed[newlist[p-1]-'A'][newlist[j]-'A']!=0 )
                p=0;  
        }
    }
    return p;
}


int main()
{
    int T;
    int N;
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        memset(combine,0,sizeof(combine));
        memset(opposed,0,sizeof(opposed));

        scanf("%d",&N);
        for(int j=0;j<N;j++)
        {
            scanf("%s",list);
            combine[list[0]-'A'][list[1]-'A']=list[2];
            combine[list[1]-'A'][list[0]-'A']=list[2];
        }
        scanf("%d",&N);
        for(int j=0;j<N;j++)
        {
            scanf("%s",list);
            opposed[list[0]-'A'][list[1]-'A']=1;
            opposed[list[1]-'A'][list[0]-'A']=1;
        }
        scanf("%d",&N);             
        scanf("%s",list);
        
        N = f(N);
        printf("Case #%d: [",i+1);
        for(int j=0;j<N-1;j++)
        {
            printf("%c, ",newlist[j]);
        }
        if( N!=0 )
            printf("%c]\n",newlist[N-1]);
        else
            printf("]\n");
    }
    return 0;
}
