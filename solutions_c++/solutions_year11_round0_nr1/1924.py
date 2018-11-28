#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <cstdio>
#include <cmath>
#include <cstdio>






using namespace std;

typedef pair<char,int> pii;

pii array[1000];
int record[1000];
int T,N;

int work()
{
    array[0]=make_pair('O',1);
    array[1]=make_pair('B',1);

    int p;
    for(int i=2;i<N+2;i++)
    {
        if(array[i].first==array[i-1].first)
        {
            record[i]=record[i-1]+abs(array[i].second-array[i-1].second)+1;
        }
        else
        {
            p=-1;
            for(int j=i-2;j>=0;j--)
            {
                if(array[j].first==array[i].first)
                {
                    p=record[j]+abs(array[i].second-array[j].second)+1;
                    break;
                }
            }
            p=max(p,record[i-1]+1);
            record[i]=p;
        }
    }
    //for(int i=2;i<N+2;i++)
    //printf("%d %d\n",i,record[i]);

    return record[N+1];


}





int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("output.out","w",stdout);

    scanf("%d",&T);
    char c;
    int pos;
    for(int loop=1;loop<=T;loop++)
    {
        scanf("%d",&N);
        for(int i=2;i<N+2;i++)
        {
            scanf(" %c %d",&c,&pos);
            array[i]=make_pair(c,pos);
        }
        /*
        for(int i=0;i<N;i++)
        {
            printf("%c %d\n",array[i].first,array[i].second);
        }
        */

        int res=work();
        printf("Case #%d: %d\n",loop,res);


    }















    return 0;
}
