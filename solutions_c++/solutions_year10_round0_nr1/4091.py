#include<iostream.h>
#include<fstream.h>
#include<conio.h>
long int pow(int a,int b)
{
    int i;
    long int c=1;
    for(i=0;i<b;i++)
    {
        c=a*c;
    }
    return c;
}

int main()
    {
        freopen("A.in","rt",stdin);
        freopen("N.out","w",stdout);
        int t,i=0,n;
        long int k;
        cin>>t;
        for(i=1;i<=t;i++)
        {
            cin>>n;cin>>k;
            long int p;
            p=pow(2,n);
            long int check=((k-(p-1))%p);
            if(check==NULL)
            {
                    cout<<"Case #"<<i<<": "<<"ON"<<endl;
            }
            else
            {
                    cout<<"Case #"<<i<<": "<<"OFF"<<endl;
            }
        }

        return 0;
    }
