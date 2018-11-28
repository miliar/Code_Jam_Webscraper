#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int n;
    
    cin >> n;
    
    for(int test_case_num = 1; test_case_num <= n; ++test_case_num) {
        int n,m,a;
        cin>>n>>m>>a;
        
        float x0=0,y0=0,x1,y1,x2,y2;
        bool found = false;
        
        for(x1=0;x1<=n;++x1) {
            for(x2=0;x2<=n;++x2) {
                for(y1=0;y1<=m;++y1) {
                    for(y2=0;y2<=m;++y2) {
                        float s = fabs(0.5*(x1*(y2-y0)+x2*(y0-y1)));
                        if(s == float(a)/2) {
                            found = true;
                            goto found;
                        }
                    }
                }
            }
        }
found:
        if(found)
            cout<<"Case #"<<test_case_num<<": "<<x0<<" "<<y0<<" "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<endl;
        else
            cout<<"Case #"<<test_case_num<<": IMPOSSIBLE"<<endl;
    }    
}