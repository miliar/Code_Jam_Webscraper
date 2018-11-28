#include <iostream>
using namespace std;
#include <cmath>

inline double max(double a, double b) {return(a>b)?a:b;}

bool incircle(double x, double y, double r, double xr, double yr, double rr){
    double tmp = sqrt((x-xr)*(x-xr) + (y-yr)*(y-yr));
    if(tmp+r<=rr)
        return true;
    else
        return false;
}

int main(void){
    int cases;
    cin >> cases;
    for(int c=0;c<cases;++c){
        int n;
        double x[40];
        double y[40];
        double r[40];
        
        cin >> n;
        for(int i=0;i<n;++i){
            cin >> x[i] >> y[i] >> r[i];
        }
        double minr = 100000000.0;
        if(n==1){
            minr = r[0];
            cout << "Case #" << c+1 << ": " << minr << endl;
            continue;
        }
        if(n==2){
            minr = max(r[0], r[1]);
            cout << "Case #" << c+1 << ": " << minr << endl;
            continue;
        }
        if(n==3){
            double tmp = sqrt((x[1]-x[0])*(x[1]-x[0]) + (y[1]-y[0])*(y[1]-y[0]));
            double r1 = (tmp+r[1]+r[0])/2.0;
            if(max(r1,r[2]) < minr)
                minr = max(r1,r[2]);
            tmp = sqrt((x[2]-x[0])*(x[2]-x[0]) + (y[2]-y[0])*(y[2]-y[0]));
            r1 = (tmp+r[2]+r[0])/2.0;
            if(max(r1,r[1]) < minr)
                minr = max(r1,r[1]);
            tmp = sqrt((x[2]-x[1])*(x[2]-x[1]) + (y[2]-y[1])*(y[2]-y[1]));
            r1 = (tmp+r[2]+r[1])/2.0;
            if(max(r1,r[0]) < minr)
                minr = max(r1,r[0]);
            cout << "Case #" << c+1 << ": " << minr << endl;
            continue;
        }
        for(int i=0;i<n;++i){
            for(int j=i+1;j<n;++j){
                double tmp = sqrt((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]));
                double r1 = (tmp+r[i]+r[j])/2.0;
                double ax = (x[i]-x[j])/tmp;
                double ay = (y[i]-y[j])/tmp;
                double rx = (x[i]+r[i]*ax + (x[j]-r[j]*ax))/2.0;
                double ry = (y[i]+r[i]*ay + (y[j]-r[j]*ay))/2.0; 
                //cout << "c1:" << i <<" " << j << " " << r1 << endl;
                for(int i2 = i+1;i2<n;++i2){
                    if(i2==j||incircle(x[i2],y[i2],r[i2],rx,ry,r1)) continue;
                    for(int j2 = i2+1;j2<n;++j2){
                        if(j2==j||incircle(x[j2],y[j2],r[j2],rx,ry,r1)) continue;
                        tmp = sqrt((x[i2]-x[j2])*(x[i2]-x[j2]) + (y[i2]-y[j2])*(y[i2]-y[j2]));
                        double r2 = (tmp+r[i2]+r[j2])/2.0;
                        double ax2 = (x[i2]-x[j2])/tmp;
                        double ay2 = (y[i2]-y[j2])/tmp;
                        double rx2 = (x[i2]+r[i2]*ax2 + (x[j2]-r[j2]*ax2))/2.0;
                        double ry2 = (y[i2]+r[i2]*ay2 + (y[j2]-r[j2]*ay2))/2.0;
                        int k;
               // cout << "c2:" << i2 <<" " << j2 << " " << r2 << endl;
                        for(k=0;k<n;++k){
                            if(k!=i && k!=j && k!=i2 && k!=j2){
                                if(!incircle(x[k],y[k],r[k],rx,ry,r1) && !incircle(x[k],y[k],r[k],rx2,ry2,r2))
                                    break;
                            }
                        }
                        //cout << k << endl;
                        if(k==n){
                            //cout << "contain!" << endl;
                            if(max(r1,r2)<minr)
                                minr = max(r1,r2);
                        }
                    }
                }
            }
        }
        cout << "Case #" << c+1 << ": " << minr << endl;
    }
    return 0;
}
