#include<iostream>

using namespace std;

int main()
{
    freopen("input.txt", "rt", stdin); 	freopen("output.txt", "wt", stdout);
    
    int nooftest;
    int n,k,oo;
    int run;
    bool arr[2000],fl;
    cin>>nooftest;
    oo=nooftest;
    while((nooftest--)>0){
    cin>>n;
    cin>>k;
    
    
    for(int i=0;i<n;i++)
    arr[i]=0;
    
    
    while((k--)>0){
    
    for(int j=0;j<n;j++){
    
        if(arr[j]==1){
        arr[j]=0;             
        }
        else {
        arr[j]=1;
        break;
        }
    
    }
        
        
    }
    run=0;
    fl=0;
    while(run<n)
    {
                if(arr[run]==0){
                cout<<"Case #"<<oo-nooftest<<": "<<"OFF"<<endl;
                fl=1;
                break;
                }
                run++;
                }
    if(fl==0)
    cout<<"Case #"<<oo-nooftest<<": "<<"ON"<<endl;
    
    }
    return 0;
}
