#include<iostream>

using namespace std;
long t,h,w,counter;
long a[200][200];
long b[200][200];
bool v[200][200];
char ch,c[20000];

const int dx[4]={-1,0,0,1};
const int dy[4]={0,-1,1,0};

void dfs (int x,int y) {
     int mini,minx,miny;
     minx=x;
     miny=y;
     mini=a[x][y];
     v[x][y]=true;
     for (int i=0;i<4;i++) {
         if (a[x+dx[i]][y+dy[i]]<mini) {
            mini=a[x+dx[i]][y+dy[i]];
            minx=x+dx[i];
            miny=y+dy[i];
         }
         //cout << x << ' ' << y << ' ' << dx[i] << ' ' << dy[i] << ' ' << a[x+dx[i]][y+dy[i]] << ' ' << mini << endl;            
     }
     //cout << x << ' ' << y << ' ' << minx << ' ' << miny << endl;     
     if ((minx!=x) || (miny!=y)) {
        if (v[minx][miny]) {b[x][y]=b[minx][miny];}
        else {dfs(minx,miny);b[x][y]=b[minx][miny];}
     }
     else {
          //cout << x << ' ' << y << endl;          
          b[x][y]=counter;
          counter++;
     }
}

int main() {
    cin >> t;
    for (int i=0;i<t;i++) {
        for (int j=0;j<200;j++) {
            for (int k=0;k<200;k++) {
                a[j][k]=100000;
            }           
        }
        cin >> h >> w;
        for (int j=1;j<=h;j++) {
            for (int k=1;k<=w;k++) {
                cin >> a[j][k];
            }
        }   
        memset(b,0,sizeof(b));
        memset(v,false,sizeof(v));
        memset(c,'!',sizeof(c));
        counter=1;
        for (int j=1;j<=h;j++) {
            for (int k=1;k<=w;k++) {
                if (!v[j][k]) {dfs(j,k);}
            }
        }
        ch='a';
        cout << "Case #" << i+1 << ":" << endl;
        for (int j=1;j<=h;j++) {
            for (int k=1;k<=w;k++) {
                if (c[b[j][k]]=='!') {c[b[j][k]]=ch;ch++;}
                cout << c[b[j][k]] << ' ';
            }
            cout << endl;
        }
    }
    //system("pause");
    return 0;
}
