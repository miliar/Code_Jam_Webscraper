#include <iostream>
using namespace std;

#define MAX 1001

bool overlap(int x1,int y1,int x2,int y2,int a1,int b1,int a2,int b2){
    if (a1 > (x2+1)) return false;
    if (x1 > (a2+1)) return false;
    if (y1 > (b2+1)) return false;
    if (b1 > (y2+1)) return false;
    if (a1 > x2 && b1>y2) return false;
    if (x1 > a2 && y1>b2) return false;
    return true;
    
}

int main(){
    int test, t;
    cin >> t;
    test = 0;
    while (test ++ < t){
        int x1[MAX];
        int x2[MAX];
        int y1[MAX];
        int y2[MAX];
        int fx2[MAX];
        int fy2[MAX];
        int r;
        cin >> r;
        for (int i=0;i<r;i++){
            cin >>x1[i] >> y1[i]>>x2[i]>>y2[i];
            fx2[i] = x2[i];
            fy2[i] = y2[i];
        }
        bool change = true;
        while (change){
            change = false;
            for (int i=0;i<r;i++)
            for (int j=i+1;j<r;j++){
                if (overlap(x1[i],y1[i],x2[i],y2[i],
                    x1[j],y1[j],x2[j],y2[j])){
                        if (fx2[i] != fx2[j]){
                            fx2[i] = max(fx2[i],fx2[j]);
                            fx2[j] = fx2[i];
                            change = true;
                        }
                        if (fy2[i] != fy2[j]){
                            fy2[i] = max(fy2[i],fy2[j]);
                            fy2[j] = fy2[i];
                            change = true;
                        }
                    }
            }
        }
        int result = 0;
        for (int i=0;i<r;i++){
            if (result < fx2[i]-x1[i]+fy2[i]-y1[i]){
                result = fx2[i]-x1[i]+fy2[i]-y1[i];
            }
        }
        cout << "Case #"<<test<<": " <<result+1<< endl; 
    }
    return 0;
}
