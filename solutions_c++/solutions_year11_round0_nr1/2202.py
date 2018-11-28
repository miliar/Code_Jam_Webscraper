#include <iostream>
#include <cstring>
#include <cmath>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <stack>
#include <deque>
#include <queue>

#define min(a,b) (((a) < (b)) ? (a) : (b))
#define max(a,b) (((a) > (b)) ? (a) : (b))
using namespace std;
int n,i,j,t,a,b, d[1001],s,ta,tb,k,test;
char c[1001];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    cin>>test;
    for(k=0;k<test;++k){

        cin>>n;
        for(i=0;i<n;++i) cin>>c[i]>>d[i];

        a = b = 1;
        s=t=0;
        ta=tb=0;
        for(i=0;i<n;++i){

            if (c[i]=='O') {
                t = abs(d[i]-a);
                a = d[i];
                if (t>ta) t-=ta;
                else t=0;
                t++;
                s+=t;
            //    cout<<i<<' '<<s<<endl;
                ta=0;
                tb+=t;
            }
            else {
                t  = abs(d[i]-b) ;
                b = d[i];
                if (t>tb) t-=tb;
                else t=0;
                t++;
                s+=t;
//                cout<<i<<' '<<s<<endl;

                tb = 0;
                ta += t;

            }
        }

        cout<<"Case #"<<k+1<<": "<<s<<endl;
        }


	return 0;
}
