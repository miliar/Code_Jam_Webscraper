#include <cstdio>
#include <math.h>

using namespace std;

int t,a,b,z;
int cut(int);
int* q;

int main()
{
    FILE* be = fopen("be.in","r");
    FILE* ki = fopen("ki.out","w");
    fscanf(be,"%d",&t);
    //printf("%d",cut(123456));
    for(int c=0; c<t;c++)
    {
        int sum=0;
        fscanf(be,"%d %d",&a,&b);
        z=floor(log10((double)a));
        q=new int[b+1];
        for(int i=0; i<b+1; i++)
        {
            q[i]=-1;
        }
        for(int i=a; i<b+1; i++)
        {
            int tmp=i;
            do
            {
                if((tmp<=b) && (tmp>=a))
                {
                    q[i]++;
                }
                tmp=cut(tmp);
            } while(tmp!=i);
            sum+=q[i];
            //printf("%d %d\n",i,q[i]);
        }
        fprintf(ki,"Case #%d: %d\n",c+1,sum/2);
    }
}

int cut(int x)
{
    int y=(int)(x%((int)pow(10,z)));
  //  printf("%d %d\n",x,y);
    return (y*10+(x-y)/(int)pow(10,z));
}
