#include<stdio.h>
#include<algorithm>
using namespace std;

class node
{
    public :
    int a , b;
};

bool cmp(node a , node b)
{
    if(a.a != b.a) return a.a < b.a;
    return a.b < b.b;
}

FILE * in = fopen("in.in","r");
FILE * out = fopen("out.out","w");

int n;
node t[1001];

int main()
{
    int i , a , k , caseID = 0 , ret;
    fscanf(in,"%d",&k);
    while(k--)
    {
        fprintf(out,"Case #%d: ",++caseID);
        fscanf(in,"%d",&n);
        for(i=0;i<n;i++) fscanf(in,"%d %d",&t[i].a,&t[i].b);
        sort(t,t+n,cmp);
        ret = 0;
        for(i=0;i<n;i++)
        {
            for(a=0;a<i;a++)
                if(t[a].b > t[i].b) ret++;
        }
        fprintf(out,"%d\n",ret);
    }
    return 0;
}
