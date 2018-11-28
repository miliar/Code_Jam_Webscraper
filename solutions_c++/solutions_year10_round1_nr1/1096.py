#include <vector>
#include <algorithm>
#include <cstdio>
#include <map>

using namespace std;

int main () {
    
    char grid[52][52];
    
    char rgrid[52][52];
    
    int numCases, kase;
    
    int k, n;
    
    scanf("%d", &numCases );
    
    for (kase=1; kase<=numCases; kase++) {
        
        scanf( "%d %d", &n, &k );
        
        for (int i=0;i<n;i++) {
            scanf("%s", grid[i]);
        }
        
        //printf("here\n");
        //rotate
        for (int i=0;i<n;i++) {
            for (int j=0; j<n; j++) {
                rgrid[i][j] = grid[n-1-j][i];
            }
        }
        //printf("here\n");
        
        //shift
        for (int i=0;i<n;i++) {
            int j=n-1;
            
            // copy the rest of the row down
            for (int kk=n-1; kk>=0; kk--,j--) {
                
                while (rgrid[j][i]=='.' && j>=0) j--;
                
                if (j<0) rgrid[kk][i] = '.';
                
                else {
                    rgrid[kk][i]=rgrid[j][i];
                }

            }
        }
        //printf("here\n");

        bool rwins = false, bwins = false;
        
        // check horiz
        for (int j=0; j<n; j++) {
            for (int i=0; i<=n-k; i++) {
                bool rrun=true, brun=true;
                for (int kk=0;kk<k;kk++) {
                    if (rgrid[j][i+kk] == '.') {
                        rrun = false; brun=false; break;
                    } else if (rgrid[j][i+kk]=='B') {
                        rrun = false;
                    } else if (rgrid[j][i+kk]=='R') {
                        brun= false;
                    }
                }
                if (brun) bwins = true;
                if (rrun) rwins = true;
            }
        }
        //printf("here\n");

        // check vert
        for (int j=0; j<n; j++) {
            for (int i=n-1; i>=k-1; i--) {
                bool rrun=true, brun=true;
                for (int kk=0;kk<k;kk++) {
                    if (rgrid[i-kk][j] == '.') {
                        rrun = false; brun=false;
                    } else if (rgrid[i-kk][j]=='B') {
                        rrun = false;
                    } else if (rgrid[i-kk][j]=='R') {
                        brun= false;
                    }
                }
                if (brun) bwins = true;
                if (rrun) rwins = true;
            }
        }
        //printf("here\n");

        // check forward
        for (int j=0; j<=n-k; j++) {
            for (int i=n-1; i>=k-1; i--) {
                bool rrun=true, brun=true;
                for (int kk=0;kk<k;kk++) {
                    if (rgrid[i-kk][j+kk] == '.') {
                        rrun = false; brun=false;
                    } else if (rgrid[i-kk][j+kk]=='B') {
                        rrun = false;
                    } else if (rgrid[i-kk][j+kk]=='R') {
                        brun= false;
                    }
                }
                if (brun) bwins = true;
                if (rrun) rwins = true;
            }
        }
        //printf("here\n");

        // check backward
        for (int j=n-1; j>=k-1; j--) {
            for (int i=n-1; i>=k-1; i--) {
                bool rrun=true, brun=true;
                for (int kk=0;kk<k;kk++) {
                    if (rgrid[i-kk][j-kk] == '.') {
                        rrun = false; brun=false;
                    } else if (rgrid[i-kk][j-kk]=='B') {
                        rrun = false;
                    } else if (rgrid[i-kk][j-kk]=='R') {
                        brun= false;
                    }
                }
                if (brun) bwins = true;
                if (rrun) rwins = true;
            }
        }
        
        printf("Case #%d: ", kase);
        if (bwins && rwins) printf("Both\n");
        else if (bwins) printf("Blue\n");
        else if (rwins) printf("Red\n");
        else printf("Neither\n");
    }
    
    
    return 0;
    
}
