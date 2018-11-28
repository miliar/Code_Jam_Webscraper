#include <iostream>
#include <string>
using namespace std;


string a[100];
int n,K;

void right() {
    for(int i=0;i<n;i++) {
        for(int j=n-1;j>=0;j--) {
            if(a[i][j] != '.') {
                for(int l=j+1;l<n;l++) {
                    if(a[i][l]!='.') break;
                    swap(a[i][l-1], a[i][l]);
                }
            }
        }
    }
}

int d[][2] = { {1,0}, {1,1}, {0,1}, {-1,1} };

bool val(char c) {
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) {
        if(a[i][j] == c) {
            for(int t=0;t<4;t++) {
                int x= i, y=j;
                int match = 1;
                for(int l=1;l<K;l++) {
                    x+=d[t][0]; y+=d[t][1];
                    if( 0<=x && x<n && 0<=y && y<n) {
                        if(a[x][y] != c) {
                            match=-1;
                            break;
                        }
                        match++;
                    } else {
                        match = -1;
                        break;
                    }
                }
                if(match>=K) return true;
            }
        }
    }
    return false;
}

int main() {
    int CASEN;
    cin>>CASEN;
    for(int ci=1;ci<=CASEN;ci++) {
        cin>>n>>K;
        for(int i=0;i<n;i++) cin>>a[i];
        right();
        for(int i=0;i<n;i++) cerr<<a[i]<<endl;

        bool red, blue;
        red = val('R');
        blue = val('B');

        cout<<"Case #"<<ci<<": ";
        if(red && blue) cout<<"Both"<<endl;
        else if(red) cout<<"Red"<<endl;
        else if(blue) cout<<"Blue"<<endl;
        else cout<<"Neither"<<endl;
    }

    return 0;
}

