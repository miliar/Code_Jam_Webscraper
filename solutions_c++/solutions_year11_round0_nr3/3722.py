#include <iostream>

#include <vector>

using namespace std;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("output-large1.out", "w", stdout);
    int T;
    cin>>T;
    int Case = 1;
    while(T--) {   
        int N;
        cin>>N;
        vector<int> a(N);
        vector<int> act;
        long long s=0,t=0;
        for(int i=0; i<N; ++i) {
            cin>>a[i];
//            s += a[i];
 //           t ^= a[i];
        }
        sort(a.begin(), a.end());
        for(int i=0; i<N; ++i) {
            s += a[i];
            t ^= a[i];
        }
        long long p=0;
        bool nc = true;
        for(int i=0; i<N; ++i) {
            p ^= a[i];
            t = t^a[i];
            s = s - a[i];
            if(p==t) {
                nc = false;
                cout<<"Case #"<<Case++<<": "<<s<<endl;
                break;
            }
        }
        if(nc) {
            cout<<"Case #"<<Case++<<": NO"<<endl;
        }
    }
    //while(true);
    return 0;
}
