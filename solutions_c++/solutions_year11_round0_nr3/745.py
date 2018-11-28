#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    freopen("out.txt","w",stdout);
    freopen("C-large.in","r",stdin);
    int t,i,n,j,test;
    cin>>t;
    int array[1010];
    bool level5;
    for (i = 1; i<=t; i++)
    {
        cin>>n;
        for (j = 0; j<n; j++)
            cin>>array[j];
        test = 0;
        level5 = 0;
        for (j = 0; j < n-1; j++)
        {
            test = test ^ array[j];
        }
        if (test == array[n-1])
           level5 = true;
        if (level5)
        {
           sort(array, array+n);
           int answer = 0;
           for (j = n-1; j>=1; j--)
             answer = answer + array[j];
           cout<<"Case #"<<i<<": "<<answer<<endl;
        }
        else
        {
            cout<<"Case #"<<i<<": NO"<<endl;
        }
    }
    return 0;
}
