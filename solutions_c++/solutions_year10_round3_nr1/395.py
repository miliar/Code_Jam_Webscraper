#include<iostream>
using namespace std;

FILE *in,*out;

long long  i,j,n,t,tt,a[10000],b[10000],counting;

void qsort(int l,int r)
{
    int i,j,mid,k;
    i = l; j = r;
    mid=a[(i+j)/2];
    do
    {
        while (a[i]<mid)
            i++;
        while (a[j]>mid)
            j--;
        if (i<=j)
        {
            k=a[i];
            a[i]=a[j];
            a[j]=k;
            k=b[i];
            b[i]=b[j];
            b[j]=k;
            i++;
            j--;
        }
    }while (i<=j);
    if (i<r)
        qsort(i,r);
    if (j>l)
        qsort(l,j);
}


int main()
{
	in=freopen("A-large(4).in","r",stdin);
    out=freopen("A-large.out","w",stdout);
    
    cin>>t;
    for (tt=1;tt<=t;tt++)
    {
        cin>>n;
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        for (i=0;i<n;i++)
            cin>>a[i]>>b[i];
        qsort(0,n-1);
        counting=0;
        for (i=0;i<n-1;i++)
            for (j=i+1;j<n;j++)
                if (b[j]<b[i])
                    counting++;
        cout<<"Case #"<<tt<<": "<<counting<<endl;
    }
    fclose(in);
    fclose(out);
	return 0;
}

