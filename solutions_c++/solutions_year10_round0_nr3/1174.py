#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<deque>
#include<set>
using namespace std;
#define ll long long
#define VI vector<int>
#define VS vector<string>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back

int main() {
 int t; cin>>t;
 for (int tt=0;tt<t;tt++) {
     cout<<"Case #"<<tt+1<<": ";
     ll R,K,N;
     cin>>R>>K>>N;
     VI g=VI(N,0);
     for (int i=0;i<N;i++) cin>>g[i];
     ll pocet=0;
     VI zr=VI(N,-1);
     VI zp=VI(N,-1);
     int pointer=0;
     for (ll r=0;r<R;r++) {
         ll up=pointer;
//         cout<<pointer<<" "<<r<<" "<<pocet<<endl;
        ll k=0;
        if (zr[pointer]==-1) {
           zr[0]=r;
           zp[0]=pocet;                     
        } else {
           ll step = zr[pointer]-r;
           ll poc = (R-r)/step;
           if (poc>0) {
              r+=step*poc;
              pocet+=poc*(zp[pointer]-pocet);
              //zr[pointer]=r;
              //zp[pointer]=pocet;
              continue;       
           } 
        }
        while (k+g[pointer]<=K) {
              k+=g[pointer];
              pocet+=g[pointer];  
              pointer++;
              pointer%=N;
              if (pointer==up) break;
    
        }           
     }
     
     cout<<pocet<<endl;
        
 }   
}
