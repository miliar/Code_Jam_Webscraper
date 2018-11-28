#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n,k;
        string s ="";
        cin>>n>>k;
        int a=k,b=n;
        while(a%2)
        {
            a=a/2;
            b--;
            if(b==0)
                break;
        }
        if(b==0)
            cout<<"Case #"<<i+1<<": ON"<<endl;
        else
            cout<<"Case #"<<i+1<<": OFF"<<endl;
    }
//    system("pause");
    return 0;
}
