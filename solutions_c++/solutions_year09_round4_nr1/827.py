#include <iostream>
using namespace std;
#include <string>

void swap(int &a, int &b){
    int tmp = a;
    a = b;
    b= tmp;
    return;
}

int swapto(int *arr, int from, int to){
    if(from == to)
        return 0;
    int cnt = 0;
    for(int i=from;i>to;--i){
        swap(arr[i], arr[i-1]);
    }
    return from - to;
}

int main(void){
    int cases;
    cin >> cases;
    
    for(int c=0;c<cases;++c){
        int n;
        string str;
        int arr[40], col[40];
        memset(col, 0, sizeof(col));
        cin >> n;
        for(int i=0;i<n;++i){
            cin >> str;
            arr[i]=0;
            for(int j=n-1;j>=0;--j){
                if(str[j]=='1'){
                    arr[i] = j;
                    col[j]++;
                    break;
                }
            }
        }
        //for(int i=0;i<n;++i)
        //    cout << arr[i] << " ";
        //cout << endl;
        int count = 0;
        for(int i=0;i<n;++i){
            for(int j=i;j<n;++j){
                if(arr[j]<=i){
                    count += swapto(arr,j,i);
                    //cout << count << endl;
                    break;
                }
            }
        }
        cout << "Case #" << c+1 << ": " << count << endl;
    }
    return 0;
}
