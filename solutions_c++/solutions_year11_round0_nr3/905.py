#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int q=1; q<=t; q++) {
        int n;
        cin >> n;
        unsigned long long int sum=0;
        int psum=0;
        int min=2000000;
        for (int i=0; i<n; i++) {
            int x;
            cin>>x;
            sum+=x;
            psum^=x;
            if (x<min) min=x;
        }
        cout << "Case #"<<q<<": ";
        if (psum) cout <<"NO"<<endl;
        else cout << sum-min << endl;

    }
    return 0;
}
