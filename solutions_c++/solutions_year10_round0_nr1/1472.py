#include<stdio.h>
#include<algorithm>
#include<math.h>
using namespace std;

FILE * in = fopen("in.in","r");
FILE * out = fopen("out.out","w");

int n , k , vis[31] , arr[31];

bool check()
{
    for(int i=0;i<n;i++) if(!vis[i]) return 1;
    return 0;
}

void make()
{
    for(int i=0;i<n;i++)
    {
        if(!vis[i])
        {
            vis[i] = 1;
            break;
        }
        else vis[i] = 0;
    }
    return;
}

int main()
{
    int i , a , r , caseID = 0 , sum = 0;
    fscanf(in,"%d",&r);
    while(r--)
    {
        memset(vis,0,sizeof vis);
        fprintf(out,"Case #%d: ",++caseID);
        fscanf(in,"%d %d",&n,&k);
        i = (int) pow(2 , n) - 1;
        k -= i;
        i++;
        if(k % i == 0) fprintf(out,"ON\n");
        else fprintf(out,"OFF\n");
    }
    return 0;
}
