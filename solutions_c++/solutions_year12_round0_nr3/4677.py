#include<iostream>
#include<cstdio>

using namespace std;

int digit(long int a)
{
    int d=0;
    while(a>0)
    {
        d++;
        a=a/10;
    }
    return d;

}
long int multi(int a)
{
    long int res=1,i=0;
    while(i!=a)
    {
        res*=10;
        i++;
    }
    return res;

}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("probc.out","w",stdout);
    long int a,b,t,i,j,k,mult,temp,tempj,dig,f,count;
    cin>>t;

    for(i=0;i<t;i++)
    {
        cin>>a>>b;
        count=0;
        for(j=a;j<b;j++)
        {

            for(k=j+1;k<=b;k++)
            {
                tempj=j;
                dig=digit(tempj);
                for(f=1;f<=dig-1;f++)
                {
                    tempj=j;
                    mult=multi(f);
                    temp=tempj%mult;
                    temp=temp*multi(dig-f);
                    tempj=tempj/mult;
                    temp+=tempj;
                    if(temp==k){count++;break;
                    }
                }

            }
        }
        printf("Case #%ld: %ld\n",i+1,count);

    }

}
