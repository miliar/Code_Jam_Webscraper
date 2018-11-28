
#include <iostream>
#define CMAX 1000000
#define NMAX 1000

using namespace std;
int T, N;


int array[NMAX];
int main() {
    cin>>T;
    for (int t=1; t<=T; t++) {
        
        cin>>N;
        
        int resultxor = 0;
        int min = CMAX+1;
        long int sum = 0;
        for (int n=0; n<N; n++) {
            cin >> array[n];
            if (array[n] < min)
                min = array[n];
            resultxor ^= array[n];
            sum+=array[n];       
        }
        if (resultxor == 0)
            cout<<"Case #"<<t<<": "<<sum-min<<endl;
        else
            cout<<"Case #"<<t<<": NO"<<endl;         
    }
  return 0;

}
