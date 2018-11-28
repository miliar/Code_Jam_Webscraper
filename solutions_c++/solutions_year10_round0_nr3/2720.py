#include <cstdio>

using namespace std;

int main()
{

    FILE*fin;
    FILE*fout;
    fin=fopen("C-small-attempt3.in","r");
    fout=fopen("output.in","w");
    int t;
    fscanf(fin,"%d\n",&t);
    long r,k,n;
    long cost;
    long *arr,*costa,*ridesa,*prev;
    bool *check;
    int j,start,group;
    int rides,rleft;
    for(int i=0;i<t;i++)
    {
        fscanf(fin,"%ld %ld %ld\n",&r,&k,&n);
        arr=new long[n];
        check=new bool[n];
        costa=new long[n];
        ridesa=new long[n];
        prev=new long[n];
        for( j=0;j<n;j++)
        {
            fscanf(fin,"%ld ",&arr[j]);
            check[j]=false;
        }
        fscanf(fin,"\n");
        j=0;
        cost=0;
        rides=0;
        while(check[j]==false&&rides!=r)
        {

            group=0;
            bool flag=false;
            for(start=j;group<=k;start=(start+1)%n)
            {
                if(flag)
                {
                    if(start==j)
                    {
                        break;
                    }
                }
                flag=true;
                if(group+arr[start]<=k)
                {
                    group+=arr[start];
                    cost+=arr[start];

                }
                else
                {
                    break;
                }
            }

            rides++;
            costa[j]=cost;
            ridesa[j]=rides;
            if(check[start]==false)
            {
            prev[start]=j;
            }
            check[j]=true;
            j=start;

        }
        if(r!=rides)
        {


        if(j>0)
        {
             costa[j]=cost-costa[prev[j]];
        ridesa[j]=rides-ridesa[prev[j]];
        //int a=costa[prev[j]];
        //int b=costa[j];
        //int c=ridesa[prev[j]];
        //int d=ridesa[j];

        cost=costa[prev[j]]+costa[j]*(long)((r-ridesa[prev[j]])/ridesa[j]);
        rleft=(r-ridesa[prev[j]])%ridesa[j];
        }
        else
        {
            cost=cost*(long)(r/rides);
            rleft=r%rides;
        }
        rides=0;
        while(rleft!=rides)
        {
            group=0;
            for(start=j;group<=k;start=(start+1)%n)
            {
                if(group+arr[start]<=k)
                {
                    group+=arr[start];
                    cost+=arr[start];
                }
                else
                {
                    break;
                }

            }
            rides++;
            j=start;
        }
        }
        fprintf(fout,"Case #%d: %ld\n",i+1,cost);
        delete[] arr;
        delete[] check;
        delete[] ridesa;
        delete[] prev;
    }
    return 0;
}
