//	ID : pallab81
// 	PROG : A
// 	LANG : C++
// 	2011-05-21-22.21.53 Saturday
//
// 	"I have not failed, I have just found 10000 ways that won't work.
//


#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <functional>
#include <bitset>

#include <cstdio>
#include <cmath>
#include <cstring>
#include <climits>
#include <cstring>

using namespace std;

#define  CI( x ) scanf( "%d", &x )

#define VI vector<int>
#define VVI vector<VI >
#define VS vector<string>
#define VC vector<char>
#define VVC vector<VC >
#define VB vector<bool>
#define VVB vector<VB >
#define PAIR pair<int,int>
#define VP vector<PAIR >
#define fo(i,st,ed) for(int i = st; i < ed ; ++i)
#define foE(i,st,ed) for(int i = st; i <= ed ; ++i)
#define foit(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define bip system("pause")
#define mk make_pair
#define f first
#define s second
#define pb push_back
#define SZ(X) (int)(X).size()
#define LN(X) (int)(X).length()
#define ll long long
#define IO ifstream cin(".in") ; ofstream cout(".out");

VVC vt;
int N;
inline void read(){
    cin>>N;
    vt.assign(N+5, VC(N+5,' ') );
    fo(i,0,N){
        fo(j,0,N){
            cin>>vt[i][j];
        }
    }
}
//WP (Winning Percentage) is the fraction of your games that you have won.
vector< double > wp;
inline void WP(){
    wp.clear();
    fo(p,0,N){
        int w=0;
        int l=0;
        fo(i,0,N){
            if(i==p)continue;
            if(vt[p][i]=='1')++w;
            if(vt[p][i]=='0')++l;
        }
        double v = (double)w/ ( (double)w+l ) ;
        wp.pb( v );
    }
}
//OWP (Opponents' Winning Percentage) is the average WP of all your opponents
//after first throwing out the games they played against you.
vector< double > owp;
inline void OWP(){
    owp.clear();
    fo( me,0,N){
        int total=0;
        double res=0;
        fo(op,0,N){
            int w=0;
            int l=0;
            if(me==op)continue;
            if(vt[me][op]=='.')continue;

            fo(i,0,N){
                if(op==i)continue;
                if(me==i)continue;
                if( vt[op][i]=='1')w++;
                if( vt[op][i]=='0')l++;
            }
            total++;
            double v = (double)w/ ( (double)w+l) ;
            res+=v;
        }
        if(total==0){
            res=0;
        }
        else{
            res = res/total;
        }
        //cout<<me+1<<" "<<res<<" "<<total<<"\n";bip;
        owp.pb(res);
    }
}
//OOWP (Opponents' Opponents' Winning Percentage) is
//the average OWP of all your opponents
vector<double> oowp;
inline void OOWP(){
    oowp.clear();
    fo(me,0,N){
        int total=0;
        double res=0;
        fo(op,0,N){
            if(me==op)continue;
            if( vt[me][op]=='.' )continue;

            total++;
            res+=owp[ op ];
        }
        if(total==0){
            res=0;
        }
        else{
            res = res/total;
        }
        oowp.pb( res );
    }
}
//RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
vector< double >rpi;
inline void RPI(){
    rpi.clear();
    fo(me,0,N){
        double v = (wp[me]*0.25) + (owp[me]*0.50) +( oowp[me]* 0.25 );
        rpi.pb( v );
    }
}

inline void print(int case_){
    printf("Case #%d:\n",case_);
    fo(i,0,N){
        printf("%.12lf\n",rpi[i]);
    }
}

int main(){

    int case_;
    cin>>case_;
    foE(i,1,case_){
        read();
        WP();
        OWP();
        OOWP();
        RPI();
        print(i);
    }
return 0;
}

