#include<iostream>
#include<fstream>

using namespace std;

ifstream fin("c-.in");
ofstream fout("c-.out");

unsigned long int r,k,n,a,t,db;

struct node{
    int x;
    node *elo, *kov;
} *kezd;

int betesz()
{
    node *p;
    p=new node;
    p->x=a;
    p->kov=kezd;
    p->elo=kezd->elo;
    kezd->elo=p;
    p->elo->kov=p;
    return 0;
}

unsigned long int szamol()
{
    unsigned long int db=0,m=0;
    node *p=kezd;
    while (r>0)
    {
        if(m+p->x<=k)
        {
            db=db+p->x;
            m=m+p->x;
        }
        else
        {
            m=p->x;
            r--;
            if(r!=0) db=db+p->x;
        }
        p=p->kov;
    }
    return db;
}

int felszab()
{
    node *p=kezd->kov;
    while(p!=kezd)
    {
        node *q=p;
        p=p->kov;
        free(q);
    }
    return 0;
}



int main()
{
    fin>>t;
    kezd=new node;
    for(unsigned long int j=1;j<=t;j++)
    {
        fin>>r>>k>>n;
        fin>>a;
        int sum=a;
        kezd->x=a;
        kezd->kov=kezd;
        kezd->elo=kezd;
        for(unsigned long int i=2;i<=n;i++)
        {
            fin>>a;
            sum=sum+a;
            betesz();
        }
        if(sum<=k)db=r*sum;
        else db=szamol();
        fout<<"Case #"<<j<<": "<<db<<"\n";
        /*node *p=kezd->kov;
        cout<<kezd->x<<" ";
        while(p!=kezd)
        {
            cout<<p->x<<" ";
            p=p->kov;
        }
        cout<<"\n";*/
        felszab();
    }
    return 0;
}
