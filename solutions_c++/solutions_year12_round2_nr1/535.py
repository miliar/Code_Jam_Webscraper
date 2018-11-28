#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<sstream>
#include<queue>
#include<cstdio>

using namespace std;

int N,XX;
const int MX=1111;
int X[MX];

bool check(int x,double v)
{
    double value=X[x];
    value+=double(XX)*v;

    double all=double(XX)*(1.0-v);

    int i;

    for(i=0;i<N;i++)
        if(i!=x&&X[i]<value)
        {
            all-=value-double(X[i]);
        }
    return all<0;
}

void test()
{
    cin>>N;
    int i;
    XX=0;
    for(i=0;i<N;i++) cin>>X[i];
    for(i=0;i<N;i++) XX+=X[i];


    double a,b,c;

    for(i=0;i<N;i++)
    {
        a=0; b=1.0;
        c=(a+b)/2.0;

        while(b>a+1e-8)
        {

            c=(a+b)/2.0;
            if(check(i,c)) b=c;
            else a=c;
        }

        printf(" %.10lf",c*100);
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);



    int i,I;
    cin>>I;

    for(i=0;i<I;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        test();
        cout<<endl;
    }
    return 0;
}
