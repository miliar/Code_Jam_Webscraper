#include<iostream>
using namespace std;


int t,tt,n,k,i,j,flag,power[31]={1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824};

int main()
{
    FILE *in,*out;
    in=freopen("A-large.in","r",stdin);
    out=freopen("A-large.txt","w",stdout);
    cin>>t;
    for (tt=1;tt<=t;tt++)
    {
        cin>>n>>k;
        flag=0;
        k++;
        if (k%power[n]==0)
            flag=1;
        if (flag)
            cout<<"Case #"<<tt<<": ON"<<endl;
        else
            cout<<"Case #"<<tt<<": OFF"<<endl;
    }
    fclose(in);
    fclose(out);    
    return 0;
}
