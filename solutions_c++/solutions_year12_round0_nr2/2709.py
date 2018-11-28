#include <cstdio>

using namespace std;

int main()
{
    FILE* be = fopen("be.in","r");
    FILE* ki = fopen("ki.out","w");
    int t;
    fscanf(be,"%d", &t);
    for(int c=0; c<t; c++)
    {
        int n,s,p;
        fscanf(be,"%d %d %d", &n,&s,&p);
        int l1,l2;
        if(p==0)
        {
            l1=0;
            l2=0;
        }
        else if(p==1)
        {
            l1=1;
            int l2=1;
        }
        else
        {
            l1=3*p-2;
            l2=3*p-4;
        }
        int sum=0;
        for(int i=0; i<n; i++)
        {
            int tmp;
            fscanf(be,"%d",&tmp);
            if(tmp>=l1)
            {
                sum++;
            }
            else if((tmp>=l2) && (s>0))
            {
                s--;
                sum++;
            }
        }
        fprintf(ki,"Case #%d: %d\n",c+1,sum);
    }

}
