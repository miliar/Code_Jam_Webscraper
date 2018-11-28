#include<cstdio>
#include<queue>
#include<algorithm>
using namespace std;
int groups[1000];
int main()
{
    FILE *in,*out;
    in=fopen("C-small-attempt0.in","r");
    out=fopen("out.txt","w");
    int T;
    fscanf(in,"%d",&T);
    int caseno=1;
    while(T--)
    {
        queue<int>Q;
        int R,K,N;
        fscanf(in,"%d %d %d",&R,&K,&N);
        //take the groups
        for(int i=0;i<N;i++)
        fscanf(in,"%d",&groups[i]);
        //now push onto queue
        for(int i=0;i<N;i++)
        Q.push(groups[i]);
        int cost=0;
        while(R--)
        {
            //calc ride cost
            int tempwt=0,curr=0,tcntr=0;
            while(1)
            {
                int top=Q.front();
                tempwt+=top;
                if(tempwt>K)
                break;
                tcntr++;
                curr+=top;
                Q.pop();
                Q.push(top);
                if(tcntr==N)
                break;
            }
            cost+=curr;
        }
        fprintf(out,"Case #%d: %d\n",caseno++,cost);
    }
    return 0;
}
