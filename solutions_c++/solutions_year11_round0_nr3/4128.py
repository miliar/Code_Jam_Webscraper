# include <iostream>
# include <stdio.h>
# include <string.h>
# include <ctype.h>
# include <vector>
using namespace std;
int main()
{
int cases,count=1;
cin>>cases;
int n,a[2000];
while(cases--)
{
    int res=0,sum=0,small=100000000;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
        sum+=a[i];
        if(a[i]<small)
        small=a[i];
        res=res^a[i];
    }
    if(res==0)
    {
        cout<<"Case #"<<count++<<": "<<sum-small<<"\n";
    }
    else
    {
        cout<<"Case #"<<count++<<": "<<"NO\n";
    }
}
    return 0;
}
