#include <iostream>
#include <algorithm>

using namespace std;

int main ()
{
int x,a[100],b[100][100],sum=0,p,k,l,L;
for(int i=0;i<100;i++) a[i]=0;
for(int i=0;i<100;i++) for(int j=0;j<100;j++) b[i][j]=0;
cin>>x;
for(int abc=0;abc<x;abc++)
        {
        sum=0;
        cin>>p;
        cin>>k;
        cin>>l;
        L=l;
        for(int i=0;i<l;i++) cin>>a[i];
        sort(a,a+l);
        //for(int i=0;i<l;i++) cout<<a[i]<<" ";
        for(int i=0;i<p;i++) 
                for(int j=0;j<k;j++) { b[i][j]=a[L-1]; L--; }
        for(int i=0;i<p;i++) 
                for(int j=0;j<k;j++) { sum=sum+b[i][j]*(i+1); }
        cout<<"Case #"<<abc+1<<": "<<sum<<endl;
        }
return 0;
}
