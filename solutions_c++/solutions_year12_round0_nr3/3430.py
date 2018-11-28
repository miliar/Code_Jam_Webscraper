#include<stdio.h>
#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>

using namespace std;

int t,a,b,n,m,p,l;
string ts,ts2;

int main(){
    freopen("in.in","r",stdin);
    freopen("out2.txt","w",stdout);

    cin >> t;

    for(int ti=0;ti<t;ti++){
        cin >> a >> b;
        p=0;
        l=0;
        for(int i=a;i<=b;i++){
            stringstream tss;
            tss << i;
            n = i;
            ts = tss.str();
            //cout << ts << endl;
            for(int j=1;j<ts.size();j++){
                ts2 = ts.substr(j,ts.size()-j) + ts.substr(0,j);
                m = atoi(ts2.c_str());
                if(ts2[0] != '0' && n < m && m <= b && l!=m){
                    p++;
                    l = m;
                    //cout << "(" << n << "," << m << ")" << " " << endl;
                }
            }
            //cout << endl;
        }
        cout << "Case #" << (ti+1) << ": " << p << endl;
    }

}
