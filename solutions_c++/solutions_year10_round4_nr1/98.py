#include <iostream>
#include <cstdlib>
using namespace std;

#define MAX 155

int isbe(int a[][MAX],int k,int i,int j, int value){
    if (i<1 || i>2*k-1) return true;
    if (j<1 || j>2*k-1) return true;
    if (a[i][j] == 10) return true;
    return (a[i][j] == value);
}

bool dxdoc(int a[][MAX], int x, int k){
    for (int i=1;i<2*k;i++){
        for (int j=1;j<x;j++)
            if (a[i][j] != 10)
            if (!isbe(a,k,i,2*x-j,a[i][j])) return false;
    }
    return true;
}

bool dxngang(int a[][MAX], int x, int k){
    for (int i=1;i<2*k;i++){
        for (int j=1;j<x;j++)
            if (a[i][j] != 10)
            if (!isbe(a,k,2*x-j,i,a[j][i])) return false;
    }
    return true;
}

int main(){
    int test, t;
    int k;
    int a[MAX][MAX];
    int result;
    
    cin >> t;
    test = 0;
    while (test ++ < t){
        result = 1000000000;
        // Read in
        cin >> k;
        for (int i=1;i<2*k;i++){
            for (int j=1;j<2*k;j++){
                a[i][j] = 10;
            }
        }
        for (int i=1;i<=k;i++){
            for (int j=k+1-i;j<=(k-1+i);j+=2)
                cin >> a[i][j];
        }
        for (int i=k+1;i<2*k;i++){
            for (int j=i+1-k;j<=3*k-i-1;j+=2)
                cin >> a[i][j];
        }
        /*/ debug
        for (int i=1;i<=2*k-1;i++){
            for (int j=1;j<=2*k-1;j++){
                cout << a[i][j];
            }
            cout << endl;
        }
        */
        for (int i=1;i<=2*k-1;i++){
            if (dxdoc(a,i,k)){
                for (int j=1;j<=2*k-1;j++){
                    if (dxngang(a,j,k)){
                        int temp = abs(i-k)+abs(j-k)+k;
                        if (result > temp*temp){
                            result = temp*temp;
                        }
                    }
                }
            }
        }
        cout << "Case #"<<test<<": " <<result -k*k<< endl;
    }
    return 0;
}
