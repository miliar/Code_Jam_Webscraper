#include <iostream>
#include <cmath>

using namespace std;

long long calc(int p)
{    
    int tmp=p;
    int t=0;
    while(p%2==0) {
        p=p/2;
        t++;
        if(t==2)
            break;
    }
    p=tmp;
    int f=0;
    while(p%5==0) {
        p=p/5;
        f++;
        if(f==2)
            break;
    }
    
    long long x=1;
    if(t==0)
        x*=4;
    else if(t==1)
        x*=2;
        
    if(f==0)
        x*=25;
    else if(f==1)
        x*=5; 
    
    return x;
}

int main()
{
    int t,pd,pg;
    cin >> t;
    long long n,p,g;
        
    for(int i=1; i<=t; i++) {
        bool flag=0;
        cin >> n >> pd >> pg;
        p=calc(pd);        
        if(p>n) {
            flag=1;            
        }
        else {
            g=calc(pg);
            if(g<p) {
                flag=1;            
            }
            else {
                if(g==p && pd!=pg) {
                    flag=1;
                }
            }
        }
        
        if(flag)
            cout << "Case #" << i << ": Broken" << endl;
        else
            cout << "Case #" << i << ": Possible" << endl;            
    }
    return 0;
}
