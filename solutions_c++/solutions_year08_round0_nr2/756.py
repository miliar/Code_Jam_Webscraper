#include <iostream>
#include <algorithm>
using namespace std;
struct In
{
    int fr;
    int to;
}a[101],b[101];
int cmp1( const void *a , const void *b ) 
{ 
    struct In *c = (In *)a; 
    struct In *d = (In *)b; 
    if(c->fr != d->fr) return c->fr - d->fr; 
    else return c->to - d->to; 
} 
int cmp2( const void *a , const void *b ) 
{ 
    struct In *c = (In *)a; 
    struct In *d = (In *)b; 
    if(c->to != d->to) return c->to - d->to; 
    else return c->fr - d->fr; 
} 
int main()
{
    int N;
    cin>>N;
    for(int n=1;n<=N;n++)
    {
        int i,j,T,NA,NB,hh,mm;
        cin>>T>>NA>>NB;
        int asw1=NA,asw2=NB;
        for(i=0;i<NA;i++)
        {
            scanf("%d:%d",&hh,&mm);
            a[i].fr=hh*60+mm;
            scanf("%d:%d",&hh,&mm);
            a[i].to=hh*60+mm+T;
        }
        for(j=0;j<NB;j++)
        {
            scanf("%d:%d",&hh,&mm);
            b[j].fr=hh*60+mm;
            scanf("%d:%d",&hh,&mm);
            b[j].to=hh*60+mm+T;
        }
        qsort(a,NA,sizeof(a[0]),cmp2); 
        qsort(b,NB,sizeof(b[0]),cmp1);
        for(i=0,j=0;i<NA&&j<NB;)
        {
            if(a[i].to<=b[j].fr){asw2--;i++;}
            j++;
        }
        qsort(a,NA,sizeof(a[0]),cmp1); 
        qsort(b,NB,sizeof(b[0]),cmp2);
        for(i=0,j=0;i<NB&&j<NA;)
        {
            if(b[i].to<=a[j].fr){asw1--;i++;}
            j++;
        }
        cout<<"Case #"<<n<<": "<<asw1<<" "<<asw2<<endl;
    }
    return 0;
}