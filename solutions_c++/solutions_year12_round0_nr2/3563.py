#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    int count=0;
    string s;
    int n;
    while(t!=count)
    {
        cin>>n;
        int a[n];
        int s,p;
        cin>>s;
        cin>>p;
        count++;
        int sat=0;
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
            if(((a[i]-p))>=2*(p-1) && (a[i]-p)>=0){
          //         cout<<a[i]<<" ";
                   sat++;
            }
            else if(s>0 && (a[i]-p)>=0 && (a[i]-p)>=2*(p-2)){
                 s--;
                 sat++;
            }
        }
        
        cout<<"Case #"<<count<<":"<<" ";
        cout<<sat<<endl;
    }
    return 0;
} 
