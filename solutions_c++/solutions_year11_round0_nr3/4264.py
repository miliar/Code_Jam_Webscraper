#include <cstdlib>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main() {
    FILE *f1,*f2;
    f1=freopen("C-large.in", "r", stdin);
    f2=freopen("C.txt", "w", stdout);
    int t;
    int n;
    int ans;
    int min;
    int sum;
    cin >> t;
    int *arr;
    for(int i=0;i<t;i++){
        cin >> n;
        arr=new int [n];
        cin >> arr[0];
        ans=arr[0];
        min=arr[0];
        sum=arr[0];
        for(int j=1;j<n;j++){
            cin >> arr[j];
            ans=ans^arr[j];
        }
        if(ans!=0)
            cout << "Case #" << i+1 << ": NO" << endl;
        else{
            for(int j=1;j<n;j++){
                sum+=arr[j];
                if(arr[j]<min)
                    min=arr[j];
            }
            cout << "Case #" << i+1 << ": " << sum-min << endl;
        }
    }
    fclose(f1);
    fclose(f2);
    return 0;
}

