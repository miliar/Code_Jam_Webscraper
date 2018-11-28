#include<iostream>
#include<vector>
#include<fstream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cmath>


using  namespace std;

int main()
{
    freopen("A2.in","r",stdin);
    freopen("output1.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 0 ; i < t; i++){
        int ans = 0;
        int to = 1, tb = 1,lc = 9999;
        int toa =0,tba = 0;
        int n;
        scanf("%d",&n);
        for(int i=0; i<n;i++){
            char c;
            int d ;
           // scanf("%c%d",&c,&d);
           cin>>c;
           cin>>d;
            if(c == 'O'){
                if((lc == 9999) || (lc == 0)){
                     ans += abs(d - to ) +1;
                     to = d;
                     toa = ans;
                }
                else{
                    int k  = 0;
                    k = abs(d-to) - (ans - toa)  ;
                    k = max(k,0);
                    ans += k +1;
                    to = d;
                    toa = ans;
                }
                lc = 0;
            }
            else if(c == 'B'){
                if((lc == 9999) || (lc == 1)){
                     ans += abs(d - tb ) +1;
                     tb = d;
                     tba = ans;
                }
                else{
                    int k  = 0;
                    k = abs(d-tb) - (ans - tba)  ;
                    k = max(k,0);
                    ans += k +1;
                    tb = d;
                    tba = ans;
                }
                lc = 1;
            }
        //    cout<<"ans = " << ans<<endl; 
        }
        cout<<"Case #"<<i+1<<": " << ans<<endl; 
    }
    return 0;
}
