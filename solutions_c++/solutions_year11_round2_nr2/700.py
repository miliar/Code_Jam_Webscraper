#include<iostream>
#include<string>
#include<cstring>
#include<vector>
#include<cstdio>
#include<queue>
#include<deque>
using namespace std;

//A

const int maxn=100+10;

char ch[maxn][maxn];
int n;

int win[maxn],lose[maxn],unknow[maxn];
int ask( char c) {
    if( c=='1' ) return -1;
    return 0;
}

double wp[maxn],owp[maxn],oowp[maxn];

void diao() {
     for(int i=0;i<n;i++) win[i]=lose[i]=unknow[i]=0;
     for(int i=0;i<n;i++) {
             for(int j=0;j<n;j++) {
                     if( ch[i][j]=='1' ) ++win[i];
                     else if( ch[i][j]=='0' ) ++lose[i];
                     else ++unknow[i];
             }
     }
     for(int i=0;i<n;i++) {
             wp[ i ]= 1.*win[i]/(win[i]+lose[i]);
             
             double ans2= 0.;
             for(int j=0;j<n;j++) {
                     if( ch[i][j]=='.' ) continue;
                     ans2 += 1.*(ask( ch[j][i] ) + win[j] )/( win[j]+lose[j]-1);
             }
             ans2 = ans2/(lose[i]+win[i]) ;
             
             owp[ i ] = ans2;
     }
     for(int i=0;i<n;i++) {
             double ans=0.;
             for(int j=0;j<n;j++) {
                     if( ch[i][j]=='.' ) continue;
                     ans+= owp[j];
             }
             ans/= win[i]+lose[i];
             oowp[ i ]= ans;
     }
     
     for(int i=0;i<n;i++) {
             printf("%.12lf\n",0.25*wp[i] + 0.5*owp[i]+ 0.25*oowp[i]);
     }
}
     

int main(void) {
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int T;
    cin>>T;
    for(int Cs=1;Cs<=T;Cs++) {
            cin>>n;
            for(int i=0;i<n;i++) scanf("%s",ch[i]);
            printf("Case #%d:\n",Cs);
            diao();
    }
    return 0;
}    
