#include <iostream>
using namespace std;

const int maxi = 256*100;

int D,I,M;
int n;
int a[110];

int cost[110][260];

int abs(int x) {
    return x>=0 ? x : -x;
}

int min(int x, int y, int z) {
    return min(min(x,y),z);
}

int up(int x, int y) {
    if(y==0) return maxi;
    return (x+y-1)/y;
}

int dis(int x, int y) {
    int z = abs(x-y);
    if( z==0 ) return 0;
    if (M==0) return maxi;
    return (z-1)/M;
}

void level(int x) {
    for(int i=0;i<256;i++) {
        for(int j=0;j<256;j++) {
            int uu = up(abs(i-j),M);
            int ad;
            if (uu>=maxi) ad = maxi;
            else ad = I*uu;
            cost[x][i] = min(cost[x][i], cost[x][j] + ad );
        }
    }
}

int go () {
    for(int i=0;i<256;i++) {
        cost[0][i] = min(D, abs(i-a[0]) );
    }
    level(0);
    for(int i=1;i<n;i++) {
        for(int j=0;j<256;j++) {
            //cost[i][j] = ?
            cost[i][j] = cost[i-1][j] + min(D, abs(a[i]-j));
            for(int k=0;k<256;k++) {
                int uu=dis(j,k);
                int j2k;
                if (uu>=maxi) j2k = maxi;
                else j2k = I*uu;

                cost[i][j] = min( cost[i][j], cost[i-1][k] + D + I + j2k,
                       cost[i-1][k] + abs(a[i]-j) + j2k );
            }
        }
        level(i);
    }

    int res = (n-1)* D;
    for(int i=0;i<256;i++) {
        res = min( res, cost[n-1][i] );
    }

//    for(int i=0;i<n;i++) {
//        for(int j=0;j<10;j++) cerr<<cost[i][j]<<" ";
//        cerr<<endl;
//    }
    return res;
}

int main() {
    int CASEN;
    cin>>CASEN;
    for(int ci=1;ci<=CASEN;ci++) {

        cin>>D>>I>>M>>n;
        for(int i=0;i<n;i++) cin>>a[i];

        cerr<<ci<<endl;
        cout<<"Case #"<<ci<<": "<<go()<<endl;
    }

    return 0;
}

