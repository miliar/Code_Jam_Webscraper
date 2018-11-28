#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>

using namespace std;

int min_scalar_product(vector<int>& v1,vector<int>& v2) {
    sort(v1.begin(),v1.end());
    sort(v2.begin(),v2.end());
    int product = 0;
    int size = v1.size();
    for (int i=0; i<size; i++) {
        product += v1[i]*v2[size-i-1];
    }
    return product;
}

int main(int argc, int** argv) {
    int n;
    cin>>n;

    for (int i=0; i<n; i++) {
        int s;
        cin>>s;
        vector<int> v1;
        vector<int> v2;
        for (int j=0; j<s; j++) {
            int temp;
            cin>>temp;
            v1.push_back(temp);
        }
        for (int j=0; j<s; j++) {
            int temp;
            cin>>temp;
            v2.push_back(temp);
        }
        
        int result = min_scalar_product(v1,v2);
        
        cout<<"Case #"<<i+1<<": ";
        cout<<result<<'\n';
    }
    return 0;
}
