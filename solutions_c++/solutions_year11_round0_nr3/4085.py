#include <iostream>

using namespace std;

int candies[2000];

int main() {
    int T;
    cin >> T;
    for(int t=1; t<=T; t++) {
        int N, max = 0;
        cin >> N;
        for(int i=0; i<N; i++)
            cin >> candies[i];

        for(int i=1; i<(1<<(N)); i++) {
            int young =0, old=0, sum=0;
            int ts=1;
            for(int j=0; j<N; j++) {
                if((i&ts) >0) {
                    young = young ^ candies[j];
                } else {
                    old = old ^ candies[j];
                    sum += candies[j];
                }
                ts *= 2;
            }
            if(young == old && sum > max) {
                max = sum;
            }
        }
        cout<<"Case #"<<t<<": ";
        if(max == 0)
            cout<<"NO"<<endl;
        else
            cout<<max<<endl;
    }
}
