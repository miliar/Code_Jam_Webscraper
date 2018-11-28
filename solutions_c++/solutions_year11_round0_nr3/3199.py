#include <iostream>

using namespace std;

int n;
int a,b,c,d,res;
bool flg;
int inp[1003];


void myf(int x,int a,int b,int c,int d)
{

    if(x==n)
    {
        //cout<<"v"<<a<<":"<<b<<":"<<c<<":"<<d<<":"<<res<<endl;
        if(c!=0 && d!=0 && a==b)
        {
            flg=true;
            //cout<<"v"<<a<<":"<<b<<":"<<c<<":"<<d<<":"<<res<<endl;
            res=max(res,max(c,d));
        }
        return;
    }
    myf(x+1,a^inp[x],b,c+inp[x],d);
    myf(x+1,a,b^inp[x],c,d+inp[x]);
    return;
}



int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int t,ti;
    cin>>t;
    for(ti=1;ti<=t;ti++)
    {
        cin>>n;
        for(int i=0;i<n;i++) {cin>>inp[i];}
        a=0;b=0;c=0;d=0;res=0;
        flg=false;
        myf(0,a,b,c,d);
        cout<<"Case #"<<ti<<": ";
        if(!flg) cout<<"NO\n";
        else cout<<res<<endl;
    }
    return 0;
}
