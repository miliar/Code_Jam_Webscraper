#include<iostream>
#include<math.h>
#include<conio.h>
using namespace std;
int main()
{
    int n,k;
 freopen("logfile.txt", "a+", stdout);
    int t;
    cin>>t;
    int ct=1;
    int arr[10003];
    while(ct<=t)
    {
    cin>>n>>k;
    int pl=pow(2,n);
    if((k+1)%pl==0)
                           arr[ct-1]=1;
    else
        arr[ct-1]=0;
                           
    ct++;
    } 
    for(int i=0;i<t;i++)
    {
    if(arr[i]==1)
                 cout<<"Case #"<<i+1<<": ON";
    else
        cout<<"Case #"<<i+1<<": OFF";
    cout<<endl;
    
    }
 //   getch();
    return 1;
}
