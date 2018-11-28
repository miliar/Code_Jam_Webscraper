#include <iostream>
#include <string>

using namespace std;

int arr[41];

int main(){
    int ncases;
    cin >> ncases;
    for(int x=1;x<=ncases;x++){
        int n;
        cin >> n;
        string temp;
        for(int i=0;i<n;i++){
            cin >> temp;
            arr[i]=0;
            for(int j=temp.size()-1;j>=0;j--){
                if(temp[j] == '1'){
                    arr[i]=j;
                    break;
                }
            }
        }
        bool complete=false;
        int count=0;
        while(!complete){
            complete = true;
            for(int i=0;i<n;i++){
                if(arr[i]>i){
                    complete = false;
                    for(int j=i+1;j<n;j++){
                        if(arr[j]<=i){
                            for(int k=j;k>i;k--){
                                int tmp = arr[k];
                                arr[k] = arr[k-1];
                                arr[k-1] = tmp;
                                count++;
                            }
                            break;
                        }
                    }
                    break;
                }
            }
        }
        cout << "Case #" << x << ": " << count << endl;
    }
}
                             