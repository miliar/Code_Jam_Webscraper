#include<iostream>
#include<fstream>

using namespace std;
ifstream fin("QC.in");
ofstream fout("QC.out");

long r,c,f,x1,x2,y1,y2,ans;
bool a[200][200],b[200][200];

int main() {
    fin >> c;
    for (int i=0;i<c;i++) {
        fin >> r;
        memset(b,sizeof(b),false);
        for (int j=0;j<r;j++) {
            fin >> x1 >> y1 >> x2 >> y2;
            for (int xx=x1;xx<=x2;xx++) {
                for (int yy=y1;yy<=y2;yy++) {
                    b[xx][yy]=true;
                    a[xx][yy]=true;
                }
            }
        }
        bool flag=true;
        ans=0;
        do {
            flag=false;
            for (int j=1;j<101;j++) {
                for (int k=1;k<101;k++) {
                    if (a[j][k]) {
                       if ((!a[j-1][k]) && (!a[j][k-1])) {b[j][k]=false;} 
                    }
                    else {
                       if ((a[j-1][k]) && (a[j][k-1])) {b[j][k]=true;}   
                    }
                }
            }
            for (int j=1;j<101;j++) {
                for (int k=1;k<101;k++) {
                    a[j][k]=b[j][k];
                    if (a[j][k]) {flag=true;}
                }
            }     
            ans++;       
        } while (flag);
        fout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}
