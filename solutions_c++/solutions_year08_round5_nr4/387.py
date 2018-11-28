#include <iostream>
#include <fstream>

#pragma optimize("O2",on)
using namespace std;

int a[110][110],b[110][110];

int main() {
#ifndef ONLINE_JUDGE
	ifstream cin("D-small.in");
    ofstream cout("D-small.out");
#endif
    int T; cin>>T;
    for (int o=1; o<=T; o++) {
        int h,w,R;
        cin>>h>>w>>R;
        memset(a,0,sizeof a);
        memset(b,0,sizeof b);
        for (int i=0; i<R; i++) {
            int r,c;
            cin>>r>>c;
            b[r][c]=1;
        }
        a[1][1]=1;
        for (int i=1; i<=h; i++)
            for (int j=1; j<=w; j++)
            if (b[i][j]==0){
                if (i-1>0 && j-2>0)
                    a[i][j]+=a[i-1][j-2];
                if (i-2>0 && j-1>0)
                    a[i][j]+=a[i-2][j-1];
                a[i][j]%=10007;
            }
        cout<<"Case #"<<o<<": "<<a[h][w]<<endl;
    }
	return 0;
}