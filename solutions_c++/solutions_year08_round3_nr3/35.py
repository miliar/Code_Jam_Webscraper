#include <fstream>

using namespace std;

ifstream fin("speed.in");
ofstream fout("speed.out");

struct data
{
    long order,h;
};


struct pdata
{
    long long key;
    long l,r;
};

long long n,m,X,Y,Z;
data a[500000];
long long A[500000];
pdata p[4000001];


void qsort(long l,long r)
{
    long i=l,j=r;
    data mid=a[(l+r)/2];
    while (i<j)
    {
        while (a[i].h<mid.h||(a[i].h==mid.h&&a[i].order>mid.order))
            i++;
        while (a[j].h>mid.h||(a[j].h==mid.h&&a[j].order<mid.order))
            j--;
        if (i<=j)
        {
            data temp=a[i];
            a[i]=a[j];
            a[j]=temp;
            i++;j--;
        }
    }
    if (i<r)
        qsort(i,r);
    if (l<j)
        qsort(l,j);
}


void init()
{
    fin>>n>>m>>X>>Y>>Z;
    for (long i=0;i!=m;i++)
        fin>>A[i];
    for (long i=0;i!=n;i++)
    {
        a[i].h=A[i%m];
        a[i].order=i+1;
        A[i%m]=(A[i%m]*X+Y*(i+1))%Z;
    }
    qsort(0,n-1);
}

void create(const long &k,const long &l,const long &r)
{
    p[k].key=0;
    p[k].l=l;
    p[k].r=r;
    if (l==r)
        return;
    create(k*2,l,(l+r)/2);
    create(k*2+1,(l+r)/2+1,r);
}

void add(const long &k,const long &key,const long &num)
{
    p[k].key=(p[k].key+num)%1000000007;
    if (p[k].l==p[k].r)
        return;
    if (key<=(p[k].l+p[k].r)/2)
        add(k*2,key,num);
    if (key>(p[k].l+p[k].r)/2)
        add(k*2+1,key,num);
}

long getnum(const long &k,const long &l,const long &r)
{
    if (r<p[k].l||p[k].r<l||l>r)
        return 0;
    if (l<=p[k].l&&p[k].r<=r)
        return p[k].key;
    return (getnum(k*2,l,r)+getnum(k*2+1,l,r))%1000000007;
}

void run()
{
    create(1,1,n);
    for (long i=0;i!=n;i++)
    {
        long temp=getnum(1,1,a[i].order-1);
        add(1,a[i].order,temp+1);
    }
    fout<<getnum(1,1,n)<<endl;
}


int main()
{
    long T;
    fin>>T;
    for (long i=1;i<=T;i++)
    {
        init();
        fout<<"Case #"<<i<<": ";
        run();
    }
    return 0;
}
