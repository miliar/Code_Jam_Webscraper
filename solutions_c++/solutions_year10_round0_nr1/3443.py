#include <iostream>
using namespace std;

int main()
{
    int i, n,j;
    long int k;
    int res;
    int casenum;
    
    freopen("A-large.in","r",stdin);
    freopen("A.txt","w",stdout);
    
    cin>>casenum;
    for ( i =0;i<casenum ;i++)
    {
        cin>>n>>k;
        for(j =0;j<n;j++)
        {
              res = k%2;
              if(res == 0) break;
              k=k/2;
        }
        if(j==n&&res==1)
        cout<<"Case #"<<i+1<<": ON"<<endl;
        else 
        cout<<"Case #"<<i+1<<": OFF"<<endl;
    }
    return 0;
}
