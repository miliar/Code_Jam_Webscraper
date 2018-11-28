#include <stack>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    ifstream cin("C-large.in");
    ofstream cout("C_RET_Large.txt");
    int ncase;
    cin>>ncase;
    for(int kcase=1;kcase<=ncase;kcase++){
        cout<<"Case #"<<kcase<<": ";
        int n;
        int a[1001]={0};
        cin>>n;
        cin>>a[0];
        int b=a[0];
        long sum=a[0];
        int min_v=a[0];
        for(int i=1;i<n;i++){
            cin>>a[i];
            b^=a[i];
            if(min_v>a[i]) min_v=a[i];
            sum+=a[i];
        }
        if(b==0){
            cout<<sum-min_v<<endl;
        }else{
            cout<<"NO"<<endl;
        }
    }
}
