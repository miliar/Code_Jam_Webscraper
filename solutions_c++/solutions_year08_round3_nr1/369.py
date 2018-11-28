#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>

using namespace std;



int main(int argc, int** argv) {
    int n;
    cin>>n;

    for (int i=0; i<n; i++) {
        int p;
        cin>>p;
        int k;
        cin>>k;
        int l;
        cin>>l;
        vector<long long> freqs;
        for (int j=0; j<l; j++) {
            int temp;
            cin>>temp;
            freqs.push_back(temp);
        }
        sort(freqs.begin(),freqs.end(),greater<long long>());
        
        int keypress = 1;
        int key = 0;
        long long result = 0;
        for (int j=0; j<l; j++) {
            if (key == k) {
                key = 0;
                keypress++;
                if (keypress > p) {
                    cout<<"Case #"<<i+1<<": ";
                    cout<<"Impossible"<<endl;
                }
            }
            result += freqs[j]*keypress;
            key++;
            
        }
        
        cout<<"Case #"<<i+1<<": ";
        cout<<result<<endl;
    }
    return 0;
}
