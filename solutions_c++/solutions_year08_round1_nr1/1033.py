#include<iostream>
#include<vector>
#include<fstream>
using namespace std;

int main()
{
    ofstream out("F:\\t\\1.txt");
    
    int t;
    cin >> t;
    int x = 1;
    while(t>0) {
        
        int n;
        cin >> n;
        
        vector<long long> a(n,0);
        vector<long long> b(n,0);
        for(int i = 0; i < n; i++) {
            cin >> a[i];
        }
        
        for(int i = 0; i < n; i++) {
            cin >> b[i];
        }
        
        sort(a.begin(),a.end());
        sort(b.rbegin(),b.rend());
        
        long long r = 0;
        
        for(int i = 0; i < n; i++) {
            r += a[i]*b[i];
        }
        
        //cout << "Case #"<<x<<": "<<r<<endl;
        out << "Case #"<<x<<": "<<r<<endl;
        x++;
        t--;
    }
    
    out.close();
    system("pause");
    return 0;
}
        
        
