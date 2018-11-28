// theme park, mrozik, 2010

#include <iostream>
#include <algorithm>
using namespace std;

int G[1000];
long long GS[2002];
int rr, k, n;

int main() {
    ios_base::sync_with_stdio(false);
    
    int tt; cin>>tt;
    for (int t=1; t<=tt; t++) {
        
        cin>>rr>>k>>n;
        for (int i=0; i<n; i++)
            cin>>G[i];
        
        GS[0]=0;
        for (int i=1; i<=2*n+1; i++)
            GS[i] = GS[i-1] + G[(i-1)%n];
        long long allGroups = GS[n];
        
        long long euros = 0;
        if (allGroups<=k) {
            euros = allGroups*rr;
        }
        
        else {
            int gix = 0;
            for (int r=0; r<rr; r++) {
                int ix = lower_bound(GS+gix, GS+gix+n, GS[gix]+k) - GS;
                if (GS[ix]>GS[gix]+k)
                    ix--;
                euros += GS[ix]-GS[gix];
                gix = ix%n;
            }
        }
        
        cout<<"Case #"<<t<<": "<<euros<<endl;
    }
    
    return 0;
}
