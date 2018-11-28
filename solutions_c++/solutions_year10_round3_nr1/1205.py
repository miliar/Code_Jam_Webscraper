#include <iostream>

using namespace std;

int main(){
    int t, n ;
    int a[1001],b[1001];
    
    cin >> t;
    for (int i=0;i<t;i++){
        cin >> n ;
        for (int j=0;j<n;j++)
            cin >> a[j] >> b[j];

        for (int j=0;j<n;j++)
            for (int k=j+1;k<n;k++)
                if (a[j]>a[k]){
                   int tmp=a[j];
                   a[j]=a[k];
                   a[k]=tmp;
                   tmp=b[j];
                   b[j]=b[k];
                   b[k]=tmp;
                   }

        int count=0;
        for(int j=0;j<n;j++)
           for (int k=0;k<n;k++)
           if (k!=j)
               if ((a[j]<a[k])&&(b[j]>b[k]))
                  count++;

        cout << "Case #"<<i+1<<": "<<count <<endl;
    }
    
    return 0;
}
