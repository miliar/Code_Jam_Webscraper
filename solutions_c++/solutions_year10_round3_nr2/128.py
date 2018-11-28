#include<fstream>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
main()
{
    int n,m,i,j,l,p,k,b,t,c;
    int max;
    ifstream in("b.txt");
    ofstream out("b.out");
    int temp;
    int ans;
    int x[100],v[100],d[100];
    double a[100];
    in>>t;
    for(int tt=1;tt<=t;tt++)
    {
        in>>l>>p>>c;
        ans=0;
        n=0;
        while(p>l)
        {
            a[n++]=p;
            i=(p%c)!=0;
            p/=c;
            p+=i;
        }    
        a[n++]=p;
        i=0;j=n-1;
        while(i<j-1)
        {
            j=(i+j)/2+(i+j)%2;
            ans++;
        }    
        out<<"Case #"<<tt<<": "<<ans<<endl;        
    }    
}    
