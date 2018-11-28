#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

string sheet[501];

int main() {
    int r,c,d;
    int tc,testcase;
    cin>>testcase;
    for(int tc=1; tc<=testcase; ++tc) {
        cin>>r>>c>>d;
        for(int i=0; i<r; ++i) {
            cin>>sheet[i];
        }

        int ans = 0;
        for(int i=0; i<r; ++i) {
            for(int j=0; j<c; ++j) {
                int msize = min(i,j);
                msize = min(msize, min(c-j-1,r-i-1));
                double xsum = 0, ysum = 0;
                for(int size=1; size<=msize; ++size) {
                    xsum = 0,ysum = 0;
                    for(int k=i-size; k<=i+size; ++k)
                        for(int l=j-size; l<=j+size; ++l) {
//                            cout<<k<<" "<<l<<endl;
                            if(abs(k-i) == size && abs(l-j) == size) continue;
                            xsum += (k-i)*(sheet[k][l]-'0'+d);
                            ysum += (l-j)*(sheet[k][l]-'0'+d);
//                            if(i == 3 && j == 3) cout<<k<<" "<<l<<" "<<xsum<<" "<<ysum<<endl;
                        }

                    if(xsum == 0 && ysum == 0) {
//                        if(ans < 2*size+1) cout<<i<<" "<<j<<" "<<size<<endl;
                        ans = max(ans,2*size+1);
                    }
                }


                // // even size
                msize = min(i+1,j+1);
                msize = min(msize,min(r-i-1,c-j-1));

//                cout<<msize*2<<endl;
                msize *= 2;
                double cx = i+0.5,cy = j+0.5;
                for(int size=2; 2*size<=msize; size++) {
                    xsum = 0,ysum = 0;
                    for(int k=i-size+1; k<=i+size; ++k)
                        for(int l=j-size+1; l<=j+size; ++l) {
                            if(k == i-size+1 || k == i+size)
                                if(l == j-size+1 || l == j+size) continue;
                            xsum += (k-cx)*(sheet[k][l]-'0'+d);
                            ysum += (l-cy)*(sheet[k][l]-'0'+d);
                        }
                    if(xsum == 0 && ysum == 0) {
//                        if(ans < size) cout<<i<<" "<<j<<" "<<size<<endl;
                        ans = max(ans, 2*size);
                    }
                }
            }
        }


        if(ans == 0) printf("Case #%d: IMPOSSIBLE\n", tc);
        else printf("Case #%d: %d\n", tc, ans);
    }
}
