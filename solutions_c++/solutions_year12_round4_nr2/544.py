#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

    int T, t;
    int n,w,l;
    int r[1010], id[1010];
    double x[1010], y[1010];
    int line[1010];
    double tx, ty;
    
    
bool judge(int current, double tx, double ty) {
    int j;
    if (!(tx<=w && ty<=l)) return false;
    for (j=0;j<n;++j) {
        if (x[j] == -1) continue;
        if (!((tx>=x[j]+r[j]+r[current] || ty>=y[j]+r[j]+r[current]) && tx<=w && ty<=l)) return false;
    }
    return true;
}
double findMinX(int lin) {
    int j;
    double min=w;
    for (j=0;j<n;++j) {
        if (x[j] == -1) continue;
        if (x[j]+r[j]<min && line[j]==lin) {
            min = x[j] + r[j];
        }
    }
    return min;
}
int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    
    int i,j,k,cline;
    cin>>T;
    for (t=0;t<T;++t) {
        cin>>n>>w>>l;

        for (i=0; i<n; ++i) {
            cin>>r[i];
            x[i] = -1;
            y[i] = -1;
            id[i] = i;
            line[i] = -1;
        }

        for (i=0; i<n-1; ++i) {
            for (j=i+1; j<n; ++j)
                if (r[j]>r[i]) {
                    swap(r[i],r[j]);
                    swap(id[i],id[j]);
                }
        }

        x[0] = 0; y[0] = 0; cline = 0; line[0] = 0;
        for (i=1; i<n; ++i) {
            tx = x[i-1]+r[i-1]+r[i]; ty = y[i-1];

            if (tx>w) {
                tx = findMinX(cline);
                ++cline;
            }

            k = i-1;
            while (!judge(i, tx,ty)) {
                if (line[k] != cline-1) break;
                ty = y[k]+r[k]+r[i];
                k--;
            }

            if (!judge(i, tx,ty)) { cout<<"Impossible!"<<endl; break; }

            x[i] = tx; y[i] = ty; line[i] = cline;
        }

        cout<<"Case #"<<t+1<<":";

        for (i=0; i<n; ++i) {
            for (j=0; j<n; ++j) if (id[j]==i) break;
            cout<<fixed <<" "<<x[j]<<" "<<y[j];
        }
        cout<<endl;
    }
    return 0;
}
