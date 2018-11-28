#include <iostream>

using namespace std;

int main(){
    int t,n,k;
    cin >> t ;
    for (int i=0 ; i!= t; i++){
        cin >> n >> k;    
        cout << "Case #" << i+1 << ": "<<((++k%(1<<n))?"OFF":"ON")<<endl;
        }    
    return 0;
}
