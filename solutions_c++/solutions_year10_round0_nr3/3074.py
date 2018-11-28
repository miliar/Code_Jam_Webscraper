#include <iostream>

using namespace std;

int main()
{
    int nc = 0;
    int arr[1000];
    cin>>nc;
    for (int i=0; i<nc; i++){
        int r,k,n,g,piv=0,st=0;

        cin>>r>>k>>n;
        for (int j=0; j<n; j++){
            cin>>g;
            arr[j]=g;
        }
        for (int j=0; j<r; j++){
            int sp=0;
            int pivi=piv;
            while (sp<=k){
                if (pivi == piv && sp>0) break;
                sp+=arr[piv%n];
                if (sp>k){
                   sp-=arr[piv%n];
                   break;
                }
                piv++;
                piv%=n;
            }
            st+=sp;
        }
        cout<<"Case #"<<i+1<<": "<<st<<endl;
    }
    return 0;
}
