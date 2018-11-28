#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,t1;
    cin >> t1;
    
    bool flag;
    long temp;
    long a[1005],n;
    int i,j;
    long min1;
    __int64 sum;
    for(t=0;t<t1;t++)
    {
        temp=0;
        cin >> n;
        min1=1000005;
        sum=0;
        for(i=0;i<n;i++)
        {
            cin >> a[i];
            temp=temp xor a[i];
            if(a[i]<min1){min1=a[i];}
            sum+=a[i];
        }
        cout << "Case #" << t+1 << ": ";
        if(temp!=0){cout << "NO";} else 
        {
            cout << sum-min1;
        }
        cout << "\n";
    }
    return 0;
}
