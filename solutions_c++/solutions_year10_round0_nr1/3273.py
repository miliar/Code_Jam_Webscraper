#include <iostream>
#include <math.h>
using namespace std;
int main(){
    int t;
    cin >> t;
    for(int i=0;i<t;i++){
            short int n;
            unsigned long int k;
            cin >> n >> k;
            int p=int(pow(2,n);
            if(k%p)==p-1) cout << "Case #" << i+1<<": ON" <<endl;
            else cout << "Case #" << i+1<<": OFF" <<endl;
    }  
	return 0;
}
