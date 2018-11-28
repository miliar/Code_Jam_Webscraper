#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    int t,c,d,n;
    cin >> t;
    string s;

    for(int i=1; i<=t; i++) {
        cin >> n;
        vector<string> bot(n);
        vector<int> b(n);        
        for(int j=0; j<n; j++) {
            cin >> bot[j] >> b[j];
        }
        long long time=0;
        int p1=1;
        int p2=1;
        long long w1=0;
        long long w2=0;
        for(int j=0; j<b.size(); j++) {
            if(bot[j]=="O") {
                int d=int(fabs(b[j]-p1));
                if(d>=w1)
                    d-=w1;
                else
                    d=0;
                time+=(d+1);
                w2+=(d+1);
                w1=0;                    
                p1=b[j];
            }
            else {
                int d=int(fabs(b[j]-p2));
                if(d>=w2)
                    d-=w2;
                else
                    d=0;
                time+=(d+1);
                w1+=(d+1);
                w2=0;   
                p2=b[j];                                 
            }
        }
        cout << "Case #" << i << ": " << time << endl;
    }

    return 0;
}
