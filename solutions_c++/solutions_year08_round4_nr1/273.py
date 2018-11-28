#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<queue>
#include<deque>
#include<set>
using namespace std;

double PI =  3.14159265358979323846;
#define ll long long
#define VI vector<int>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back
#define VVI vector<VI >
#define vela 999999
int ls(int x) {
    return (x+1)*2-1;
}

int rs(int x) {
    return ls(x)+1;    
}

int combi(int lv,int rv,int t) {
    if (t==1) return lv*rv;
    if (lv!=0||rv!=0) return 1;
    return 0;
}

int main() {
    int cases;
    cin>>cases;
    for (int tt=0;tt<cases;tt++) {
        int m; cin>>m;
        int goal; cin>>goal;
        VI v0=VI(m,vela);        
        VI v1=VI(m,vela);
        VI change=VI(m/2,0);
        VI typ=VI(m/2,0);
        for (int i=0;i<m/2;i++) {
              cin>>typ[i]>>change[i];  
        }
        for (int i=m/2;i<m;i++) {
            int pom; cin>>pom;
            if (pom==0) v0[i]=0;
            else v1[i]=0;    
        }
        for (int i=m/2-1;i>=0;i--) {
            VI all;
            int z=0;
            if (typ[i]==0||change[i]) {
               if (typ[i]!=0) z=1; else z=0;                       
               all.PB(v0[ls(i)]+v0[rs(i)]+z);               
            }
            if (typ[i]==1||change[i]) {
               if (typ[i]!=1) z=1; else z=0;
               all.PB(v0[ls(i)]+v0[rs(i)]+z);               
               all.PB(v0[ls(i)]+v1[rs(i)]+z);
               all.PB(v1[ls(i)]+v0[rs(i)]+z);
            }
            sort(all.begin(),all.end());
            v0[i]=all[0]; if (v0[i]>vela) v0[i]=vela;
            
            all.clear();
            if (typ[i]==1||change[i]) {
               if (typ[i]!=1) z=1; else z=0;                       
               all.PB(v1[ls(i)]+v1[rs(i)]+z);               
            }
            if (typ[i]==0||change[i]) {
               if (typ[i]!=0) z=1; else z=0;
               all.PB(v1[ls(i)]+v1[rs(i)]+z);               
               all.PB(v0[ls(i)]+v1[rs(i)]+z);
               all.PB(v1[ls(i)]+v0[rs(i)]+z);
            }
            sort(all.begin(),all.end());
            v1[i]=all[0]; if (v1[i]>vela) v1[i]=vela;
        }
        //for (int i=0;i<m;i++) {
        //    cout<<i<<":  "<<v0[i]<<" "<<v1[i]<<endl;    
        //}
        
        int ret;
        if (goal==0) ret=v0[0]; else ret=v1[0];
        cout<<"Case #"<<tt+1<<": ";
        if (ret==vela) cout<<"IMPOSSIBLE"<<endl;
        else cout<<ret<<endl;
    }
}
