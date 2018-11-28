#include <iostream>
#include <fstream>

#pragma optimize("O2",on)
using namespace std;

__int64 a[3][3];

int main() {
#ifndef ONLINE_JUDGE
	ifstream cin("A-large.in");
    ofstream cout("A-large.out");
#endif
    int T; cin>>T;
    for (int o=1; o<=T; o++) {
        __int64 n,A,B,C,D,x0,y0,M,X,Y;
        cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
        memset(a,0,sizeof a);
        a[x0%3][y0%3]++;
        for (int i=1; i<n; i++) {
            X=(A*x0+B)%M;
            Y=(C*y0+D)%M;
            a[X%3][Y%3]++;
            x0=X; y0=Y;
        }
        __int64 res=0,add=1;
        for (int x1=0; x1<3; x1++) for (int y1=0; y1<3; y1++)
            if (a[x1][y1]>0) {
                add*=a[x1][y1]; a[x1][y1]--;
                for (int x2=0; x2<3; x2++) for (int y2=0; y2<3; y2++)
                    if (a[x2][y2]>0) {
                        add*=a[x2][y2]; a[x2][y2]--;
                        for (int x3=0; x3<3; x3++) for (int y3=0; y3<3; y3++)
                            if (a[x3][y3]>0 && (x1+x2+x3)%3==0 && (y1+y2+y3)%3==0)
                                res+=add*a[x3][y3];
                        a[x2][y2]++; add/=a[x2][y2];
                    }
                a[x1][y1]++; add/=a[x1][y1];
            }
        cout<<"Case #"<<o<<": "<<res/6<<endl;
    }
	return 0;
}