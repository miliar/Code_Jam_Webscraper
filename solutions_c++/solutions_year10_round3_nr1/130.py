#include<fstream>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int a[1001],b[1001],c[1001];
bool cmp(const int&x, const int&y)
{
    return a[x]<a[y];
}    
main()
{
    int t,n,m,i,j,k;
    
    ifstream in("a.txt");
    ofstream out("a.out");
    int temp;
    int ans;
    in>>t;
    for(int tt=1;tt<=t;tt++)
    {
        in>>n;
        ans=0;
        for(i=0;i<n;i++)
        {
            in>>a[i]>>b[i];   
            c[i]=i;         
        }    
        sort(c,c+n,cmp);
        for(i=0;i<n;i++)
        {
            for(j=0;j<i;j++)
            {
                if(b[c[i]]<b[c[j]])ans++;
            }    
        }    
        out<<"Case #"<<tt<<": "<<ans<<endl;
    }    
}    
