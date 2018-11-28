#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>
#include<algorithm>
#include<map>

using namespace std;

class INT
{
    public:
        double p;
        string feature;
};

int N,n,L,A,i,j,Q;
string name;
char c;
map<string,int> M;
INT T[10000];
double k;

void read(int i)
{
    char c;
    string s="";
    scanf("%c",&c);
    while(c!='(') scanf("%c",&c);
    scanf("%lf",&T[i].p);
    T[i].feature="";
    scanf("%c",&c);
    while(c==' ') scanf("%c",&c);
    while(c!=')' && c!='\n')
    {
        s+=c;
        scanf("%c",&c);
    }
    remove(s.begin(),s.end(),' ');
    if(s!="")
    {
        T[i].feature=s;
        read(i*2);
        read(i*2+1);
    }
    if(c!=')')
    {
        scanf("%c",&c);
        while(c!=')') scanf("%c",&c);
    }
}

void query(int i)
{
    k*=T[i].p;
    if(T[i].feature=="") return;
    if(M[T[i].feature]==1) query(i*2);
    else query(i*2+1);
}

main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&N);
    for(Q=1;Q<=N;Q++)
    {
        scanf("%d\n",&L);
        read(1);
        printf("Case #%d:\n",Q);
        scanf("%d",&A);
        for(i=0;i<A;i++)
        {
            cin>>name;
            M.clear();
            scanf("%d",&n);
            for(j=0;j<n;j++)
            {
                cin>>name;
                M[name]=1;
            }
            k=1;
            query(1);
            printf("%.7f\n",k);
        }
    }
}
