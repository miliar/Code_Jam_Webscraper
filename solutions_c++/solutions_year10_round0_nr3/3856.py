
#include <iostream>
using namespace std;





int T, R, k, N;
int g[1000];
int pax = 0, ans = 0, cluster = 0, paxCluster = 0, lastCluster, nGroups = 0;
int acc[1001];
int offset[1001];


int process() {
    
}

int main() {
    cin>>T;
    for (int t=1; t<=T; t++) {
        ans = 0;
        pax = 0;
        nGroups = 0;
        memset(acc,0,1001);
        memset(offset,0,1001);
        cin>>R;
        cin>>k;
        cin>>N;
    
        for (int i=0; i<N; i++) {
            cin >> g[i];
        }
        bool endloop = false;
        int r = 0;
        while (!endloop) {
            
            for (int i=0; i <N; i++) {
                
                if ((pax + g[i] > k) || (nGroups == N)) {
                    acc[i]+= pax;
                    ans += pax;
                    //cerr << ans << endl;
                
                /*
                    if (i = N-1) {
                        offset[i] = k - pax;
                        
                        for (int j=0; j<=r; j++) {
                            if (offset[i] == 0) {
                                cluster = i;
                                paxCluster = acc[i];
                                endloop = true;
                                break;
                            }
                            else if (offset[i] == offset[j]) {
                                cluster = j - i;
                                paxCluster = acc[j] - acc[i];
                                endloop = true;
                                break;   
                            }
                            
                        }
                    }
                    */
                    nGroups = 1;
                    pax = g[i];
                    r++;
                  
                }
                else {
                    if (nGroups <= N) {
                        pax+=g[i];
                        nGroups++;
                    }
                }
                  if (r == R) {
                        endloop = true;
                        break;
                    }
                    
            }
        }
        /*
        cerr << ans << endl;
        if (r < R) {
            int left = R - r;
            int clustersLeft = left / cluster;
            ans += clustersLeft*paxCluster;
            int lastCluster = left % cluster;
        }
        cerr << ans << endl;
         for (int j = 0; j < lastCluster; j++) {
            for (int i=0; i <N; i++) {
                if (pax + g[i] > k) {
                    ans += pax;
                }
                else pax+= g[i];
            }       
        }
        cerr << ans << endl;
        */    
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
  return 0;

}
