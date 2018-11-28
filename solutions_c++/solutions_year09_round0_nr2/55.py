#include <iostream>
#include <fstream>

using namespace std;

int numMaps;
int H, W;
char letter;
int alt[105][105];
char bas[105][105];

char flow(int h, int w);

int main() {
    cin>>numMaps;
    for(int z=1; z<=numMaps; z++) {
        cin>>H>>W;
        letter = 'a';
        for(int h=0; h<H; h++)
            for(int w=0; w<W; w++) {
                cin>>alt[h][w];
                bas[h][w] = 0;
            }
        for(int h=0; h<H; h++)
            for(int w=0; w<W; w++)
                flow(h,w);
        cout<<"Case #"<<z<<":"<<endl;
        for(int h=0; h<H; h++) {
            for(int w=0; w<W; w++)
                cout<<bas[h][w]<<" ";
            cout<<endl;
        }
    }
    return 0;
}

char flow(int h, int w) {
    if(bas[h][w]) return bas[h][w];
    const int dh[] = {-1,0,0,1};
    const int dw[] = {0,-1,1,0};
    int nh=h, nw=w;
    int bestAlt = 10000;
    for(int a=0; a<4; a++) {
        if(h+dh[a]>=0 && h+dh[a]<H && w+dw[a]>=0 && w+dw[a]<W) {
            if(alt[h+dh[a]][w+dw[a]]<bestAlt) {
                bestAlt = alt[h+dh[a]][w+dw[a]];
                nh = h+dh[a]; nw = w+dw[a];
            }
        }
    }
    if(bestAlt < alt[h][w]) {
        bas[h][w] = flow(nh,nw);
    } else {
        bas[h][w] = letter;
        letter++;
    }
    return bas[h][w];
}
