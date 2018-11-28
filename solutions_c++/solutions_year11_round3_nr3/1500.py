#include <iostream>
using namespace std;

void work(int t) {
    int n,l,m,i,j,k;
    cin>>n>>l>>m;
    int *p  =   new int[n];
    for(i=0;i<n;i++)
        cin>>p[i];
    for(j=l;j<=m;j++)
    {
        for(k=0;k<n;k++)
            if(p[k]%j && j%p[k])
                break;
        if(k==n){
            cout<<"Case #"<<t<<": "<<j<<endl;break;}
    }
    if(j==m+1)
        cout<<"Case #"<<t<<": "<<"NO"<<endl;
}

int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
        work(i+1);
    return 0;
}

